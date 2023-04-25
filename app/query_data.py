import os

import openai
from gpt_index import GPTSimpleVectorIndex

from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

embeddings = os.path.join("app", "embeddings", "index.json")
index = GPTSimpleVectorIndex.load_from_disk(embeddings)

result = index.query("Tell me about the Guru.")
print(result)

result = index.query("Tell me about the Healer.")
print(result)
