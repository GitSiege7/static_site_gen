import os
import shutil

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

main()