import openai
import time

class OpenAIAPI:
    def __init__(self, settings):
        self.settings = settings
        openai.api_key = self.settings["key"]
    
    def gpt_response(self, message):
        try:
            response = openai.Completion.create(
                        prompt=message,
                        temperature=self.settings['temperature'],
                        max_tokens=self.settings['max_tokens'],
                        model=self.settings['model']
                    )
            gpt_answer = response['choices'][0]['text'].strip("\n").lower()
            return gpt_answer
        
        except openai.error.RateLimitError as e:
            # Handle rate limit error
            print(f"Rate limited. Error message: {e}")
            # Wait for the recommended duration before retrying
            wait_time = e.http_response.headers.get("Retry-After")
            if wait_time:
                print(f"Waiting for {wait_time} seconds before retrying.")
                time.sleep(int(wait_time))
            # Retry the API call
            return self.gpt_response(message)

    def chatgpt_response(self, message):
        try:
            response = openai.ChatCompletion.create(
                        model=self.settings['model'],
                        messages=[
                            {"role": "user", "content": message}
                            ]
                    )
            chatgpt_answer = response['choices'][0]['message']['content'].strip("\n").lower()
            return chatgpt_answer
        except openai.error.RateLimitError as e:
            # Handle rate limit error
            print(f"Rate limited. Error message: {e}")
            # Wait for the recommended duration before retrying
            wait_time = e.response.headers.get("Retry-After")
            if wait_time:
                print(f"Waiting for {wait_time} seconds before retrying.")
                time.sleep(int(wait_time))
            # Retry the API call
            return self.chatgpt_response(message)
    
    def generate_response(self, data, prompt, model):
        i = 0
        result = []

        for sent in data:
            if len(sent)==0: break
            
            print(i)
            message = prompt.format(sent)

            if model=='gpt3' or model=='gpt4':
                answer = self.gpt_response(message)
            elif model=='chatgpt':
                answer = self.chatgpt_response(message)
            result.append(answer)
            i += 1  
        print('---Done')
        return result