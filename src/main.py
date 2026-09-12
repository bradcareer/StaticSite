import os
import shutil
import sys
 
from gencontent import generate_pages_recursive
from copystatic import copy_files_recursive

dir_path_static = "./static"
dir_path_docs = "./docs"
basepath = "/"


def main() -> None:
    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)
    if len(sys.argv)>1:
        basepath =  sys.argv[1]
    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)
    from_path = 'content/'
    template_path = 'template.html'
    dest_path = 'docs/'
    generate_pages_recursive(from_path, template_path, dest_path, basepath)

main()
