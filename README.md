# Trust-nlp

## Run API Call
These arguments are the default settings which executes GPT3 API model. You can simply run `python main.py` to get the same result.
```python
python main.py --work='api' \
               --model='gpt3' \
               --data-path='./data/pubmed_causal_language_use2.csv' \
               --settings='./settings.json' \
               --prompt='./gpt-prompt.txt' \
               --output-path='./results/{}_results.csv'
```

To use different models such as GPT4 and chatGPT, arguements can be modified like the following:

**--GPT4**
```python
python main.py --model='gpt4'
```
**--chatGPT**
```python
python main.py --model='chatgpt' \
               --prompt='prompt.txt'
```

## Run Statistics Test
To run the statistics test, your dataset should include integer label values from the second column. 

Below is the sample code to run statistics from `final_result.csv` and save the statistics text file into `./results/stats/` folder.
**--chatGPT**
```python
python main.py --work='quant' \
               --data-path="./results/calcu_chatGPT_final_result_remove_unclear.csv" \
               --output-path="./results/stats/"
```
**--GPT3**
```python
python main.py --work='quant' \
               --data-path="./results/calcu_gpt3_final_result.csv" \
               --output-path="./results/stats/"
```
