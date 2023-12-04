# Data generation for Q&A dataset augmentation in healthcare
ITMO'23 ANLP Course Project

## Main goal:
Compare different methods of data augmentation for the Q&A task

## Team
[Igor Chernov](https://link-url-here.org): Fine-tuning Q&A<br />
[Alexandra Matveeva](https://github.com/alex-mat-s): ruT5-base Fine-Tuning for Q&A<br />
Dariya Murova: data parsing, data augmentation<br />
[Alexander Semiletov](https://github.com/kinoooshnik): data augmentation<br />

## QA models

### ruT5-base
#### MedQAModel2 

**Dataset**<br />
MedQuAD_Rus_clean

**Parameters**
- BATCH_SIZE: 4
- Epochs: 91
- Train set: 781
- Validation set: 196
- Test set: 20
- Max input len: 512
- Max output len: 32

**Metrics on test**<br />

*BLEU:* 0.08575324940726765<br />
*RougeL:* 0.005295566502463054<br />

**Example**<br />
![MedQAModel2 example](https://github.com/alex-mat-s/data_augmentation_QA/blob/main/img/img1.png)

#### MedQAModel4<br />
**Dataset**<br />
MedQuAD_clean

**Parameters**
- BATCH_SIZE: 4
- Epochs: 100
- Train set: 872
- Validation set: 48
- Test set: 23
- Max input len: 512
- Max output len: 128

**Metrics on test**<br />
*BLEU:* 0.14194473035391136<br />
*RougeL:* 0.06521739130434782<br />

**Loss**<br />
![MedQAModel4 loss](https://github.com/alex-mat-s/data_augmentation_QA/blob/main/img/img15.jpg)
<br />**Examples**<br />
![MedQAModel4 example1](https://github.com/alex-mat-s/data_augmentation_QA/blob/main/img/img16.png)
![MedQAModel4 example2](https://github.com/alex-mat-s/data_augmentation_QA/blob/main/img/img3.png)
![MedQAModel4 example3](https://github.com/alex-mat-s/data_augmentation_QA/blob/main/img/img4.png)
![MedQAModel4 example4](https://github.com/alex-mat-s/data_augmentation_QA/blob/main/img/img5.png)

#### MedQAModel_aug_ans
**Dataset**<br />
MedQuAD_answers_augmented_concat

**Parameters**
- BATCH_SIZE: 4
- Epochs: 56
- Train set: 1036
- Validation set: 259
- Test set: 27
- Max input len: 512
- Max output len: 128

**Metrics on test**<br />
*BLEU:* 0.2098802666579037<br />
*RougeL:* 0.037037037037037035<br />

**Loss**<br />
![MedQAModel_aug_ans loss](https://github.com/alex-mat-s/data_augmentation_QA/blob/main/img/img6.png)
<br />**Examples**<br />
![MedQAModel_aug_ans example1](https://github.com/alex-mat-s/data_augmentation_QA/blob/main/img/img7.png)
![MedQAModel_aug_ans example2](https://github.com/alex-mat-s/data_augmentation_QA/blob/main/img/img8.png)
![MedQAModel_aug_ans example3](https://github.com/alex-mat-s/data_augmentation_QA/blob/main/img/img9.png)
![MedQAModel_aug_ans example4](https://github.com/alex-mat-s/data_augmentation_QA/blob/main/img/img10.png)

#### MedQAModel_generated
**Dataset**<br />
MedQuAD_answers_augmented_concat

**Parameters**
- BATCH_SIZE: 4
- Epochs: 22
- Train set: 5021
- Validation set: 1256
- Test set: 129
- Max input len: 512
- Max output len: 128

**Metrics on test**<br />
*BLEU:* 0.6652164170527515<br />
*RougeL:* 0.054325089208810136<br />

**Loss**<br />
![MedQAModel_generated loss](https://github.com/alex-mat-s/data_augmentation_QA/blob/main/img/img11.png)
<br />**Examples**<br />
![MedQAModel_generated example1](https://github.com/alex-mat-s/data_augmentation_QA/blob/main/img/img12.png)
![MedQAModel_generated example2](https://github.com/alex-mat-s/data_augmentation_QA/blob/main/img/img13.png)
![MedQAModel_generated example3](https://github.com/alex-mat-s/data_augmentation_QA/blob/main/img/img14.png)
