from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from langchain_community.document_loaders import TextLoader
from utils.helpers import print_separator, print_title

def main() -> None:
    print_title("Text Loader")
    file_path = str(PROJECT_ROOT / "data" / "input" / "sample.txt")
    loader = TextLoader(file_path=file_path)
    documents = loader.load()
    print(f"Total documents loaded : {len(documents)}")

    print_separator()

    document = documents[0]
    print(f"Document metadata:\n{document.metadata}")

    print_separator()

    print(f"Document page content:\n{document.page_content}")


if __name__ == "__main__":
    main()


    