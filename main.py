from fastapi import FastAPI
from sentence_transformers import SentenceTransformer


app = FastAPI()

@app.get("/")
def root():
    return "Hello World"

@app.post("/query")
def complete_query(query:str):
    sentens_transformer=SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    print(sentens_transformer.encode([query]))
    return {"ok":True}