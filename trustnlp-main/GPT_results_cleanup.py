import pandas as pd
data = pd.read_csv('results/gpt3_results.csv')

def relabel(sent):
    if sent.startswith('this sentence does not'):
        return 0
    elif sent.startswith('no, this sentence does not'):
        return 0
    elif sent.startswith("no, the sentence does not"):
        return 0
    else:
        if 'correlational' in sent:
            return 3
        elif 'causal' in sent:
            return 1
        else:
            return 0

data['gpt3_label'] = data['gpt3-results'].apply(lambda x: relabel(x))

data.to_csv('results/gpt3_full_label.csv', index=False)