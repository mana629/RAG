from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import TokenTextSplitter
from utils.helpers import print_separator, print_title

def main() -> None: 
    print_title("Token Text Splitter")
    file_path = str(PROJECT_ROOT / "data" / "input" / "medium_text.txt")
    loader = TextLoader(file_path)
    document = loader.load()
    print(f"Original document character count: {len(document[0].page_content)}")
    print_separator()
    splitter = TokenTextSplitter(
        chunk_size=512,
        chunk_overlap=128,
    )
    chunks = splitter.split_documents(document)
    print(f"Split into {len(chunks)} chunks")
    print_separator()
    for index, chunk in enumerate(chunks, start=1):
        print(f"--- Chunk {index} (Length: {len(chunk.page_content)}) ---")
        print(chunk.page_content)
        print_separator()

if __name__ == "__main__":
    main()