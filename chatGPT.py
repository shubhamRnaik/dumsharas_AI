from llama_index import SimpleDirectoryReader,GPTListIndex,GPTVectorStoreIndex,LLMPredictor,PromptHelper
from langchain import OpenAI
import sys
import os
import cachetools


os.environ["OPENAI_API_KEY"] = "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"



def createIndex(path):
    max_input = 4096
    tokens = 200
    chunk_size = 600
    max_chunk_overlap = 1
    
    promptHelper = PromptHelper(max_input,tokens,max_chunk_overlap,chunk_size_limit=chunk_size)
    
    llmPredictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-ada-001",max_tokens=tokens))

    if not os.path.exists(path):
        raise ValueError(f"Directory {path} does not exist.")
      
    docs = SimpleDirectoryReader(path).load_data()
    
    vectorIndex = GPTVectorStoreIndex(documents=docs,llm_predictor=llmPredictor,prompt_helper=promptHelper)
    vectorIndex.save_to_disk('vectorIndex.json')
    return vectorIndex


data = createIndex('DATA')

def answerMe(vectorIndex):
  vIndex = GPTVectorStoreIndex.load_from_disk(vectorIndex)
  while True:
    input = input('Please ask: ')
    response = vIndex.query(input,response_mode='compact')
    print(f'Response: {response} \n')
    

answerMe(data)

