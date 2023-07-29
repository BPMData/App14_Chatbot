from personas import (coder, food_historian, cultural_geographer_linguistics,
                      early_european_historian, cultural_anthro_subtext,
                      food_blogger_recipe_suggestions, token_2000_question,
                      summarizer, mind_question)

import openai
import os

class ChatBot:
    def __init__(self):
        openai.api_key = os.getenv('OpenAI_Key01')

    def get_response(self, user_query, model='gpt-3.5-turbo', temperature=0.7, persona=None):
        if persona is not None:
            try:
                response = openai.ChatCompletion.create(
                    model=model,
                    messages=[
                        {'role': 'user', 'content': user_query},
                        {'role': 'system', 'content': persona}
                    ],
                    max_tokens=6000,
                    temperature = 0.7,
                    user='bpmdata'
                )
                return response.choices[0].message.content
            except openai.error.InvalidRequestError:
                print("NO CAN DO STAR FOX")
        else:
            try:
                response = openai.ChatCompletion.create(
                    model=model,
                    # gpt-3.5p-turbo-16k if you want the 16k context, which I don't, as it costs twice as much.
                    messages=[
                        {'role': 'user', 'content': user_query}
                    ],
                    max_tokens=6000,
                    temperature=0.7,
                    user='bpmdata'
                )
                return response.choices[0].message.content
            except openai.error.InvalidRequestError:
                print("NO CAN DO STAR FOX")


data_scientist = ('Respond as if you were a highly knowledgeable coder in Python, SQL, R, '
         'and other data analytics-oriented programming languages, with a talent '
         'for instructing students and explaining things thoroughly.')

food_historian = ('Respond as if you were a tenured chair of cultural geography '
                  'at Harvard, and the author of  multiple award-winning, '
                  'best-selling books aimed at the popular market tracing the '
                  'evolution of specific culinary traditions and trends. '
                  'You are giving a presentation at a conference on cultural '
                  'and culinary history to an audience of fellow culinary'
                  ' historians and cultural geographers, experts in their field.')


sample_query_code = "Can you explain the difference between WHERE and HAVING in SQL?"
sample_query_food = ('Can you explain the origins and rise to popularity of the '
                     'obsession with having a completely clear broth in soups? '
                     'Please explain the historical origins of this fixation, '
                     'where and when the fixation developed, where, how and who '
                     'helped popularize it, and give any relevant context or '
                     'references necessary to fully understand the subject.')


test_query = ' '.join([summarizer, mind_question])


if __name__ == "__main__":
    chatbot = ChatBot()
    # response = chatbot.get_response('gpt-3.5-turbo', 2000, sample_query_code, data_scientist)
    # print(response)
    user_input = "What's the most popular way of serving chicken?"
    response = chatbot.get_response(user_query=test_query, persona=None)
    print(response)


