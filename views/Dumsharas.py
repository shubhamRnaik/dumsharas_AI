
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os
from secret_key import openai_api_key
print(openai_api_key)
os.environ['OPENAI_API_KEY'] = openai_api_key
llm = OpenAI(temperature='0.3')



def AI_MOVIE_NAME_GENERATIR(Language):
    PromptTemplateName = PromptTemplate(
    input_variables=['language'],
    template="name any 5  Indian {language} movie from 1990 to 2023 for dumsharas game in comma seperated  list with actor and actress name"
    )
    chain = LLMChain(llm=llm, prompt=PromptTemplateName)
    Response = chain.run(Language)
    return Response
    

