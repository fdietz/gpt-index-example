import os

# specify your OpenAI API key
# os.environ["OPENAI_API_KEY"]

from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex(documents)

# save to disk
index.save_to_disk('index.json')