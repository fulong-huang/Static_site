import os
import shutil

from generate_page import *


def main():
    empty_public_folder()
    copy_content("static", "public")
    print("main")
    #generate_page("content/index.md", "template.html", "public/index.html")
    generate_page_recursive("content", "template.html", "public")
    print("FINISH")
    
def copy_content(from_dir, to_dir):
    for fse in os.listdir(from_dir):
        print(f"{from_dir}/{fse}")
        if os.path.isfile(f"{from_dir}/{fse}"):
            shutil.copy(f"{from_dir}/{fse}", to_dir)
        else:
            os.mkdir(f"{to_dir}/{fse}")
            copy_content(f"{from_dir}/{fse}", f"{to_dir}/{fse}")


def empty_public_folder():
    folder = "./public"
    for fse in os.listdir(folder):
        path = os.path.join(folder, fse)
            
        try:
            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path)
        except Exception as e:
            print(e)



main()

