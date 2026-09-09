import os
import shutil
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from utils.helpers import print_separator, print_title
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma

load_dotenv(PROJECT_ROOT / ".env")

def main():
    print_title("Chroma VectorStore")
    
    file_path = str(PROJECT_ROOT / "data" / "input" / "small_text.txt")
    loader = TextLoader(file_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200, 
        chunk_overlap=0
    )
    chunks = text_splitter.split_documents(docs)
    print("chunks are :", len(chunks))
    print_separator()
    
    # model to embeddings
    embedding = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    chroma_db_path = PROJECT_ROOT / "data" / "chroma_db"
    
    if chroma_db_path.exists():
        shutil.rmtree(chroma_db_path)
        
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=str(chroma_db_path),
        collection_name="langchain_demo"
    )
    print("chroma db created successfully at", chroma_db_path)
    print_separator()

    print("documents count in collection :", vectorstore._collection.count())
    print_separator()

    query = " what is langchain"
    returned_docs = vectorstore.similarity_search(query, k=3)
    print("returned documents :", len(returned_docs))
    print_separator()

    for idx, doc in enumerate(returned_docs, start=1):
        print(f"Result {idx}:\n{doc.page_content}\n")
        print_separator()


if __name__ == "__main__":
    main()
    
 

    