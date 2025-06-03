import os
import shutil
from generate_page import generate_pages_recursive

def recursive_copy(source, destination):
    shutil.rmtree(destination)
    os.mkdir(destination)

    for item in os.listdir(source):
        if(os.path.isfile(source + "/" + item)):
            shutil.copy(source + "/" + item, destination)
        else:
            os.mkdir(destination + "/" + item)
            recursive_copy(source + "/" + item, destination + "/" + item)
    return


def main():
    recursive_copy("/home/siege/workspace/python/static_site_gen/static", "/home/siege/workspace/python/static_site_gen/public")

    generate_pages_recursive("/home/siege/workspace/python/static_site_gen/content", 
                             "/home/siege/workspace/python/static_site_gen/template.html",
                             "/home/siege/workspace/python/static_site_gen/public")


main()