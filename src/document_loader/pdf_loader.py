from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from langchain_community.document_loaders import PyPDFLoader
from utils.helpers import print_separator, print_title


def main() -> None: 
    print_title("PDF Loader")
    file_path = PROJECT_ROOT / "data" / "input" / "sample.pdf"
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    print(f"Total documents loaded : {len(documents)}")

    print_separator()

    first_page = documents[0]
    print(f"Document metadata:\n{first_page.metadata}")

    print_separator()

    print(f"Document page content:\n{first_page.page_content}")


if __name__ == "__main__":
    main()
