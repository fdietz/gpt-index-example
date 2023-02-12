import os

# specify your OpenAI API key
# os.environ["OPENAI_API_KEY"]

from gpt_index import GPTSimpleVectorIndex

# load from disk
index = GPTSimpleVectorIndex.load_from_disk('index.json')

print(index.query("What does the future of Devops look like in the next 5 years?"))