from ollama import chat

class LanguageModel:
    def __init__(self, model_name="deepseek-r1:8b"):
        self.model_name = model_name


    def determine_change(self, original_filename, original_paragraph, current_filename, current_paragraph, new_filename, new_paragraph):
        response = chat(model=self.model_name, messages=[{
            'role': 'user',
            "content": f"""Analyze evalutation document filename and paragraph and determine if you should replace the paragraph with new one based on recency. 
                Original filename: '{original_filename}'
                Original paragraph: '{original_paragraph}'
                Current filename: '{current_filename}'
                Current paragraph: '{current_paragraph}'
                New filename: '{new_filename}'
                New paragraph: '{new_paragraph}'
                Answer YES or NO
            """
        }])
        response = response["message"]["content"]

        if "deepseek" in self.model_name:
            response = response.split("</think>\n\n")[1]

        print(response)
        return "YES" in response and "NO" not in response