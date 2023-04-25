import os

import openai
from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader

from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


input_data = os.path.join("app", "data")
documents = SimpleDirectoryReader(input_data).load_data()
index = GPTSimpleVectorIndex.from_documents(documents)

embeddings = os.path.join("app", "embeddings", "index.json")
index.save_to_disk(embeddings)
