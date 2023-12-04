# Data generation for Q&A dataset augmentation in healthcare
ITMO'23 ANLP Course Project

## Main goal:
Compare different methods of data augmentation for the Q&A task

## QA models
### MedQAModel2 

*Dataset*\n
MedQuAD_Rus_clean

*Parameters*
- BATCH_SIZE: 4
- Epochs: 91
- Train set: 781
- Validation set: 196
- Test set: 20
- Max input len: 512
- Max output len: 32

*Metrics on test*

**BLEU** 0.08575324940726765\n
**RougeL** 0.005295566502463054

*Example*\n
[![MedQAModel2 example]([https://github.com/alex-mat-s/data_augmentation_QA/img/blob/main/img1.png?raw=true)](https://github.com/alex-mat-s/data_augmentation_QA/blob/main/img/img1.png)](https://github.com/alex-mat-s/data_augmentation_QA/blob/main/img/img1.png)

*MedQAModel3*
Dataset: MedQuAD_clean
Parameters:
- BATCH_SIZE: 4
- Epochs: 63
- Train set: 872
- Validation set: 48
- Test set: 23
- Max input len: 512
- Max output len: 128
Metrics on test:
BLEU: 0.14117568971024988
RougeL: 0.06521739130434782
Loss
![MedQAModel3 loss](https://https://github.com/alex-mat-s/data_augmentation_QA/img/blob/main/img1.jpg?raw=true)
Examples
![MedQAModel3 example1](https://github.com/alex-mat-s/data_augmentation_QA/img/blob/main/img2.jpg?raw=true)
![MedQAModel3 example2](https://github.com/alex-mat-s/data_augmentation_QA/img/blob/main/img3.jpg?raw=true)
![MedQAModel3 example3](https://github.com/alex-mat-s/data_augmentation_QA/img/blob/main/img4.jpg?raw=true)
![MedQAModel3 example4](https://github.com/alex-mat-s/data_augmentation_QA/img/blob/main/img5.jpg?raw=true)

*MedQAModel_aug_ans*
Dataset: MedQuAD_answers_augmented_concat
Parameters:
- BATCH_SIZE: 4
- Epochs: 56
- Train set: 1036
- Validation set: 259
- Test set: 27
- Max input len: 512
- Max output len: 128
Metrics on test:
BLEU: 0.2098802666579037
RougeL: 0.037037037037037035
Loss
![MedQAModel_aug_ans loss](https://https://github.com/alex-mat-s/data_augmentation_QA/img/blob/main/img6.jpg?raw=true)
Examples
![MedQAModel_aug_ans example1](https://github.com/alex-mat-s/data_augmentation_QA/img/blob/main/img7.jpg?raw=true)
![MedQAModel_aug_ans example2](https://github.com/alex-mat-s/data_augmentation_QA/img/blob/main/img8.jpg?raw=true)
![MedQAModel_aug_ans example3](https://github.com/alex-mat-s/data_augmentation_QA/img/blob/main/img9.jpg?raw=true)
![MedQAModel_aug_ans example4](https://github.com/alex-mat-s/data_augmentation_QA/img/blob/main/img10.jpg?raw=true)

*MedQAModel_generated*
Dataset: MedQuAD_answers_augmented_concat
Parameters:
- BATCH_SIZE: 4
- Epochs: 22
- Train set: 5021
- Validation set: 1256
- Test set: 129
- Max input len: 512
- Max output len: 128
Metrics on test:
BLEU: 0.6652164170527515
RougeL: 0.054325089208810136
Loss
![MedQAModel_generated loss](https://https://github.com/alex-mat-s/data_augmentation_QA/img/blob/main/img11.jpg?raw=true)
Examples
![MedQAModel_generated example1](https://github.com/alex-mat-s/data_augmentation_QA/img/blob/main/img12.jpg?raw=true)
![MedQAModel_generated example2](https://github.com/alex-mat-s/data_augmentation_QA/img/blob/main/img13.jpg?raw=true)
![MedQAModel_generated example3](https://github.com/alex-mat-s/data_augmentation_QA/img/blob/main/img14.jpg?raw=true)
