from llama_index import SimpleDirectoryReader,LLMPredictor
import os
import openai
from langchain import OpenAI
from llama_index import GPTListIndex
import yaml
from prompt import load_prompt
# from llama_index.langchain_helpers.memory_wrapper import GPTIndexChatMemory
# from llama_index import GPTSimpleVectorIndex

def load_yaml_config(path):
    with open(path) as f:
        config = yaml.full_load(f)
    return config


config=load_yaml_config('config.yaml')
os.environ['OPENAI_API_KEY'] = config['api_key']

QA_PROMPT_TMPL=load_prompt()

def document_index():
    documents = SimpleDirectoryReader('data').load_data()

    llm1=OpenAI(temperature=config['model_config']['temperature'], model_name=config['model_config']['model_name'],
                openai_api_key=config['api_key'])
    # define LLM
    llm_predictor = LLMPredictor(llm=llm1)

    # build index
    index = GPTListIndex(documents, llm_predictor=llm_predictor,text_qa_template=QA_PROMPT_TMPL)
    
    if os.path.exists('index'):
        index.save_to_disk("index/index.json")
    else:
        os.mkdir('index')
        index.save_to_disk("index/index.json")
    return "Documnet Index file uploaded Sucessfully."

if __name__=="__main__":
    ans=document_index()
    print(ans)
    
    

