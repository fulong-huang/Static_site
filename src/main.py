import os
import shutil


def main():
    dir_list = os.listdir("public")
    empty_public_folder()
    

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

