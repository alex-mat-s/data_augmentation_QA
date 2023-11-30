#!/usr/bin/env python3
import re


def preprocess_data(df):
    df["question"] = [elem.replace('Вопрос:', '') for elem in df["question"]]
    df["answer"] = [elem.replace('Резюме:', '') for elem in df["answer"]]
    df["answer"] = [elem.replace('Краткое описание:', '') for elem in df["answer"]]

    # Remove all samples with insignificant context
    ids = []
    substr = "На этой странице Основные сведения"
    for i in range(df.shape[0]):
        if substr not in df.iloc[i]["context"]:
            ids.append(i)
    df = df.iloc[ids,:]

    for col in df.columns:
        if col == "answer_start":
            continue
        df[col] = [re.sub('[-—\n\t]', '', elem) for elem in df[col]]
        df[col] = [re.sub(' +', ' ', elem) for elem in df[col]]
        # Lowercase
        df[col] = [elem.lower() for elem in df[col]]
    
    return df

    