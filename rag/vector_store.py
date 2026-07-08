import os
from dotenv import load_dotenv

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from rag.ingest import load_documents

# Load environment variables
load_dotenv()

# Create Local Embedding Model (No API Key Required)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def create_vector_store():

    print("Loading documents...")

    chunks = load_documents()

    print("Creating embeddings...")

    vector_db = FAISS.from_documents(
        chunks,
        embeddings
    )

    print("Saving FAISS Index...")

    vector_db.save_local("rag/faiss_index")

    print("✅ Vector Store Created Successfully!")


if __name__ == "__main__":
    create_vector_store()