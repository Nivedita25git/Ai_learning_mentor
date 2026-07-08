import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="text-embedding-004",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

result = embeddings.embed_query("What is DBMS?")

print("Success!")
print(len(result))