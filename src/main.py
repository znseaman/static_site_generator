import os
import shutil
import sys

from copy_static import copy_files_recursive
from generate_page import generate_pages_recursive

working_directory = "."
dir_path_static = "static"
dir_path_docs = "docs"
dir_path_public = "public"
dir_path_content = "content"
template_path = "template.html"

def main():
    print(f"verify sys.argv: {sys.argv}")
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
        
    abs_working_dir = os.path.abspath(working_directory)
    dir_path_docs_abs_path = os.path.normpath(os.path.join(abs_working_dir, dir_path_docs))

    if os.path.exists(dir_path_docs_abs_path):
        print(f"Deleting {dir_path_docs} directory...")
        shutil.rmtree(dir_path_docs_abs_path)

    print("Copying static files to public directory...")
    copy_files_recursive(working_directory, dir_path_static, dir_path_docs)
    
    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)

if __name__ == "__main__":
    main()

