import os
import shutil

from copy_static import copy_files_recursive
from generate_page import generate_pages_recursive

working_directory = "."
dir_path_static = "static"
dir_path_public = "public"
dir_path_content = "content"
template_path = "template.html"

def main():
    abs_working_dir = os.path.abspath(working_directory)
    dir_path_public_abs_path = os.path.normpath(os.path.join(abs_working_dir, dir_path_public))

    if os.path.exists(dir_path_public_abs_path):
        print("Deleting public directory...")
        shutil.rmtree(dir_path_public_abs_path)

    print("Copying static files to public directory...")
    copy_files_recursive(working_directory, dir_path_static, dir_path_public)
    
    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

if __name__ == "__main__":
    main()

