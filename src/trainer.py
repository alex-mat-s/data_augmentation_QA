from tqdm import tqdm
import torch
import locale
locale.getpreferredencoding = lambda: "UTF-8"
#from rouge_score import rouge_scorer
import evaluate
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from rouge import Rouge
import seaborn as sns
sns.set_style("whitegrid")

class Trainer():

    def __init__(
            self,
            model, 
            epochs, 
            path, 
            train_loader, 
            val_loader, 
            optimizer,
            device,
            tokenizer, 
            q_len,
            t_len,
            scheduler=None
    ):
        """
        Initialize Trainer class for ruT5-base model fine-tuning.

        Arguments:
            path (str): the path to save the best model
        """
        self.train_loss_lst = []
        self.valid_loss_lst = []

        self.model = model
        self.n_epochs = epochs
        self.checkpoint_path = path
        self.train_loader = train_loader
        self.valid_loader = val_loader
        self.device = device
        self.optimizer = optimizer
        self.tokenizer = tokenizer
        self.scheduler = scheduler
        self.max_sequence_len = q_len
        self.max_target_len = t_len
        
    
    def fit(self):
        best_val_loss = float('inf')
        self.model = self.model.to(self.device)
        self.train_loss = []
        self.valid_loss = []
        
        for epoch in range(self.n_epochs):
            train_loss = 0.0
            self.model.train()
            for batch in tqdm(self.train_loader, desc="Training batches"):
                input_ids = batch["input_ids"].to(self.device)
                attention_mask = batch["attention_mask"].to(self.device)
                labels = batch["labels"].to(self.device)
                decoder_attention_mask = batch["decoder_attention_mask"].to(self.device)
                # Clear gradients
                self.optimizer.zero_grad()
                # Make a prediction
                outputs = self.model(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    labels=labels,
                    decoder_attention_mask=decoder_attention_mask
                )
                # Calculate gradients
                outputs.loss.backward()
                # Update weights
                self.optimizer.step()
                # Calculate losss
                train_loss += outputs.loss.item()
            
            if self.scheduler is not None:
                self.scheduler.step(train_loss/len(self.train_loader))
            
            # Evaluation
            val_loss = 0.0
            self.model.eval()

            # Validation loop
            with torch.no_grad():
                for batch in tqdm(self.valid_loader, desc="Validation batches"):
                    input_ids = batch["input_ids"].to(self.device)
                    attention_mask = batch["attention_mask"].to(self.device)
                    labels = batch["labels"].to(self.device)
                    decoder_attention_mask = batch["decoder_attention_mask"].to(self.device)
                    
                    outputs = self.model(
                        input_ids=input_ids,
                        attention_mask=attention_mask,
                        labels=labels,
                        decoder_attention_mask=decoder_attention_mask
                    )
                    val_loss += outputs.loss.item()
            
            self.train_loss_lst.append(train_loss / len(self.train_loader))
            self.valid_loss_lst.append(val_loss / len(self.valid_loader))
            
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                self.model.save_pretrained(self.checkpoint_path)
                self.tokenizer.save_pretrained(self.checkpoint_path)

            print(f'Epoch: {epoch}\t\tTrain loss: {train_loss/len(self.train_loader)}\t\t'
                  f'Validation loss: {val_loss/len(self.valid_loader)}')
            
    def predict_answer(self, context, question, ref_answer=None, print_text=False):
        inputs = self.tokenizer(
            question, 
            context, 
            max_length=self.max_sequence_len, 
            padding="max_length", 
            truncation=True, 
            add_special_tokens=True
        )

        input_ids = torch.tensor(inputs["input_ids"], dtype=torch.long).to(self.device).unsqueeze(0)
        attention_mask = torch.tensor(inputs["attention_mask"], dtype=torch.long).to(self.device).unsqueeze(0)

        outputs = self.model.generate(input_ids=input_ids, attention_mask=attention_mask, max_length=128)

        predicted_answer = self.tokenizer.decode(outputs.flatten(), skip_special_tokens=True)   
        predicted_answer = predicted_answer.replace("<extra_id_0>", "")

        if ref_answer:
            answer_encoding = self.tokenizer(
                ref_answer,
                max_length=self.max_target_len,
                padding="max_length",
                truncation=True,
                return_attention_mask=True,
                add_special_tokens=True,
                return_tensors="pt"
            )

            labels_embed = answer_encoding["input_ids"]
            labels = self.tokenizer.decode(labels_embed.flatten(), skip_special_tokens=True)

            # Load the Bleu metric
            bleu = evaluate.load("google_bleu")
            score = bleu.compute(predictions=[predicted_answer],
                                references=[labels])
            
            # Load Rouge metric
            rouge = Rouge()
            scores = rouge.get_scores(predicted_answer, labels)

            if print_text:
                print(context)
                print(question)
                print(predicted_answer)

            return {
                "Reference Answer: ": labels,
                "Predicted Answer: ": predicted_answer,
                "BLEU Score: ": score,
                "RougeL (precision): ": scores[0]["rouge-l"]["p"]
            }
        else:
            return predicted_answer
        
    def calc_avg_metrics(self, test_data):
        bleu_metric = 0.0
        rouge_metric = 0.0

        for i in range(len(test_data)):
            test_sample = test_data.iloc[i]
            test_context = f"Контекст: {test_sample['context']}"
            test_question = f"Вопрос: {test_sample['question']}"
            test_answer = f"Ответ: {test_sample['answer']}"

            pred = self.predict_answer(test_context, test_question, test_answer)

            bleu_metric += pred["BLEU Score: "]["google_bleu"]
            rouge_metric += pred["RougeL (precision): "]

        return bleu_metric / len(test_data), rouge_metric / len(test_data)
       
    def plot_loss(self, filepath=False):
        if filepath:
            data_loss = pd.read_csv(filepath, sep="\t", header=None)
            data_loss = data_loss[[0, 2, 4]]
            data_loss.columns = ["Epoch", "Train loss", "Validation loss"]

            data_loss["Epoch"] = [int(text.replace("Epoch: ", "")) for text in data_loss["Epoch"]]
            data_loss["Train loss"] = [float(text.replace("Train loss: ", "")) for text in data_loss["Train loss"]]
            data_loss["Validation loss"] = [float(text.replace("Validation loss: ", "")) for text in data_loss["Validation loss"]]

            plt.plot(data_loss["Train loss"], label="train_loss")
            plt.plot(data_loss["Validation loss"], label="val_loss")
            plt.legend()
            plt.show()
        
        else:  
            plt.plot(self.train_loss_lst, label="train_loss")
            plt.plot(self.valid_loss_lst, label="val_loss")
            plt.legend()
            plt.show()