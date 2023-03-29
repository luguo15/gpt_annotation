import pandas as pd
import json

def load_data(dir):
    return pd.read_csv(dir)

def load_sentences(dir, colname):
    data = pd.read_csv(dir)
    return data[colname]

def load_settings(dir, model):
    with open(dir) as f:
        setting = json.load(f)

    if model=='gpt3':
        setting['model'] = 'text-davinci-003'
    elif model=='gpt4':
        setting['model'] = 'gpt-4'
    elif model=='chatgpt':
        setting['model'] = 'gpt-3.5-turbo'
    return setting

def load_prompt(dir):
    with open(dir) as f:
        prompt = "".join(f.readlines())
    return prompt