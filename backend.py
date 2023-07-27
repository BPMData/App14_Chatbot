import openai
import os

class ChatBot:
    def __init__(self):
        openai.api_key = os.getenv('OpenAI_Key01')

    def get_response(self, user_query):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", # gpt-3.5p-turbo-16k if you want the 16k context, which I don't, as it costs twice as much.
            messages=[
                {'role': 'user', 'content': user_query},
                {'role': 'system', 'content': 'Respond as if you were a highly knowledgeable coder in Python, SQL, R, and other data analytics-oriented programming languages, with a talent for instructing students and explaining things thoroughly.'}
            ],
            max_tokens=1000,
            temperature = 0.7,
            user='bpmdata'
        )
        return response.choices[0].message


harvard_tempeh_question = """
Respond as if you were a tenured chair of cultural geography at Harvard, and the author of  multiple award-winning, best-selling books aimed at the popular market tracing the evolution of specific culinary traditions and trends. You are giving a presentation at a conference on cultural and culinary history to an audience of fellow culinary historians and cultural geographers, experts in their field.

Please explain the history of the invention and mass popularization of tempeh. Focus on the reasons that provided the impetus for its invention, where and when it was invented, and whether it was intended primarily for a vegetarian audience or intended for meat eaters to consume as a complement for meat protein in one's diet. Please try to include references or quotations when possible.
"""

if __name__ == "__main__":
    chatbot = ChatBot()
    response = chatbot.get_response("Can you explain the difference between WHERE and HAVING in SQL?")
    print(response)