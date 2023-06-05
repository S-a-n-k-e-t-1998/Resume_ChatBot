# from llama_index import SimpleDirectoryReader
import os
from llama_index import GPTListIndex
from prompt import load_prompt
from train import load_yaml_config
import logging
 
 # Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


config=load_yaml_config('config.yaml')

os.environ['OPENAI_API_KEY'] = config['api_key']
QA_PROMPT_TMPL=load_prompt()


def AssistantBot():    
    try:
        index=GPTListIndex.load_from_disk('index/index.json')
        print("file load succesfully")
        if index:
            while True:
                Question=input("Enter Your Question :: Exit >> 1  ::")
                if Question!='1':
                    response=index.query(Question,text_qa_template=QA_PROMPT_TMPL)
                    print("Answer :: ",response.response)
                else:
                    break
        else:
            raise "file indexing not found"
    except Exception as e:
        logging.exception(e)
    

if __name__=='__main__':
    AssistantBot()      
        