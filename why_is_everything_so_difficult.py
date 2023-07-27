import openai
import os

class ChatBot:
    def __init__(self):
        openai.api_key = 'NOPE'

    def get_response(self, user_query):
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt = user_query,
            max_tokens = 1000,
            temperature = 0.7

        )
        return response.choices[0].text


if __name__ == "__main__":
    chatbot = ChatBot()
    response = chatbot.get_response('Write a joke about the Barbie movie.')
    print(response)