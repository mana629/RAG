from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter 
from utils.helpers import print_separator, print_title

def main() -> None: 
    print_title("Markdown Header Text Splitter")
    file_path = str(PROJECT_ROOT / "data" / "input" / "medium_text.txt")
    with open(file_path,'r', encoding = "utf-8") as f:
        markdown_text = f.read()
    # loader = TextLoader(file_path)
    # document = loader.load()
    print(f"Original document character count: {len(markdown_text)}")
    print_separator()
    splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
            
        ],
    )
    chunks = splitter.split_text(markdown_text)
    print(f"Split into {len(chunks)} chunks")
    print_separator()
    for index, chunk in enumerate(chunks, start=1):
        print(f"--- Chunk {index} (Length: {len(chunk.page_content)}) ---")
        print(chunk.page_content)
        print_separator()

if __name__ == "__main__":
    main()