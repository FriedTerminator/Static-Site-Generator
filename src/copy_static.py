import os
import shutil

def copy_recursive(src, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        if os.path.isdir(src_path):
            copy_recursive(src_path, dest_path)
        


def copy_static():
    static_path = 'static'
    docs_path = 'docs'

    if not os.path.exists(static_path):
        raise Exception("Source directory does not exist")
    
    if os.path.exists(docs_path):
        shutil.rmtree(docs_path)
    
    copy_recursive(static_path, docs_path)