from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from langchain_community.document_loaders import CSVLoader
from utils.helpers import print_separator, print_title


def main() -> None:
    """Demonstrate CSV Loader"""
    print_title("CSV Loader")
    file_path = str(PROJECT_ROOT / "data" / "input" / "employees.csv")
    loader = CSVLoader(file_path=file_path)
    documents = loader.load()
    print(f"Total rows loaded : {len(documents)}")

    print_separator()

    first_row = documents[0]
    print(f"Content :\n{first_row.page_content}")
    print_separator()
    print(f"Row metadata:\n{first_row.metadata}")

    print_separator()

    print(f"First row page content:\n{first_row.page_content}")


if __name__ == "__main__":
    main()

      

   