from copy_static import copy_static
from page_creation import generate_pages_recursive
import sys

if __name__ == "__main__":
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    if not basepath.endswith("/"):
        basepath += "/"

    copy_static()
    generate_pages_recursive("content", "template.html", "docs", basepath)