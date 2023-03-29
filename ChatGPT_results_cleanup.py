import pandas as pd
data = pd.read_csv('results/chatgpt_results.csv')

def categorize_answer(answer):
    if answer == "the sentence describes a correlative research finding." or answer == "yes, it describes a research finding that smoking is correlated with decreased life expectancy." or answer == "causal/correlational: correlational.":
        return 1
    elif answer == "yes, the sentence describes a research finding about the effectiveness of a combination therapy for a rare deadly cancer caused by asbestos.":
        return 3
    else:
        if 'correlational' in answer and 'causal' not in answer:
            return 1
        elif 'causal' in answer and 'correlational' not in answer:
            return 3
        else:
            return 0

data['chatGPT_labels'] = data['chatgpt-results'].apply(lambda x: categorize_answer(x))
data.to_csv("results/chatGPT_full_labels.csv", index=False)


# Yuheun's code
# def categorize_answer(answer):
#     if 'correlational' in answer and 'causal' not in answer:
#         return 'correlational'
#     elif 'causal' in answer and 'correlational' not in answer:
#         return 'causal'
#     else:
#         return 'norel'

# data['answers2'] = data['chatgpt-results'].apply(lambda x: categorize_answer(x))

# label = {'norel': 0, 'correlational': 3, 'causal': 1}
# data['chatGPT_labels'] = data['answers2'].apply(lambda x: label[x])

# data2 = data.drop('answers2', axis=1)
# data2.to_csv("chatGPT_full_labels.csv", index=False)