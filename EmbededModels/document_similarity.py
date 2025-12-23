from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large", dimensions=300)

documents =[
" Virat Kohli is one of crickets most prolific batsmen, known for his intensity, consistency, and world-class chase-mastery.",

"Rohit Sharma is a stylish Indian opener famed for his effortless timing and record number of double centuries in ODIs.",

"Jasprit Bumrah is Indias premier fast bowler, recognized for his unorthodox action, deadly yorkers, and unmatched accuracy.",

"Lionel Messi is a football legend celebrated for his extraordinary dribbling, playmaking genius, and record-breaking achievements.",

"Cristiano Ronaldo is a global sports icon known for his athleticism, goal-scoring excellence, and unmatched longevity at the top level."

]

query = "Tell me about ronaldo"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]
print(query)
print(documents[index])

            