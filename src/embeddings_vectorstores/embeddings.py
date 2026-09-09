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

load_dotenv(PROJECT_ROOT / ".env")

def main() -> None:
    print_title("Embeddings")
    file_path = str(PROJECT_ROOT / "data" / "input" / "sample.txt")
    loader = TextLoader(file_path)
    import os
    if not os.getenv("GOOGLE_API_KEY") and not os.getenv("GEMINI_API_KEY"):
        print("\n[ERROR] GOOGLE_API_KEY is not set.")
        print("Please add your Gemini API key to the .env file:")
        print("    GOOGLE_API_KEY=your_gemini_api_key_here")
        print("You can get a free key at: https://aistudio.google.com/app/apikey\n")
        return

    embedding = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    text = "LangChain makes it easy to build applications powered by LLMs"
    embed_text = embedding.embed_query(text)
    print(f"Embedding dimension: {len(embed_text)}")
    print_separator()
    print(embed_text)
    print_separator()

if __name__ == "__main__":
    main()