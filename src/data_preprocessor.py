#!/usr/bin/env python3
import re


def preprocess_data(df):
    # Remove all samples with insignificant context
    ids = []
    substr1 = "На этой странице"
    substr2 = "Эти ресурсы посвящены"
    for i in range(df.shape[0]):
        if substr1 not in df.iloc[i]["context"] and substr2 not in df.iloc[i]["answer"]:
            ids.append(i)
    df = df.iloc[ids,:]

    for col in df.columns:
        if col == "answer_start":
            continue
        # Lowercase
        df[col] = [elem.lower() for elem in df[col]]
        df[col] = [elem.replace('вопрос:', '') for elem in df[col]]
        df[col] = [elem.replace('резюме:', '') for elem in df[col]]
        df[col] = [elem.replace('резюме', '') for elem in df[col]]
        df[col] = [elem.replace('краткое описание:', '') for elem in df[col]]
        df[col] = [elem.replace('фальк:', '') for elem in df[col]]
        df[col] = [elem.replace('фалько:', '') for elem in df[col]]
        df[col] = [elem.replace('falco:', '') for elem in df[col]]
        df[col] = [elem.replace('описание', '') for elem in df[col]]

        df[col] = [re.sub('[-–—\n\t\(\)\[\]]', '', elem) for elem in df[col]]
        df[col] = [re.sub(' +', ' ', elem) for elem in df[col]]
        
    
    return df

    