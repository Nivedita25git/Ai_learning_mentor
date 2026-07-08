import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_documents():

    all_docs = []

    folder = "rag/documents"

    for file in os.listdir(folder):

        if file.endswith(".pdf"):

            loader = PyPDFLoader(
                os.path.join(folder, file)
            )

            docs = loader.load()

            all_docs.extend(docs)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(all_docs)

    print(f"Loaded {len(all_docs)} pages")

    print(f"Created {len(chunks)} chunks")

    return chunks


if __name__ == "__main__":

    load_documents()