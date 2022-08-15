from os import listdir
import os
from os.path import join, isdir, abspath


def directory_walk(root_directory):
    def directory_walk_internal(current_directory):
        print(root_directory)
        if not isdir(root_directory):
            return
        contents = sorted([d for d in listdir(root_directory) if d not in ["venv", ".git"]])

        for content in contents:
            directory_walk(join(current_directory, content))

    return directory_walk_internal(abspath(root_directory))


directory_walk("./")

print("-" * 20)

directory_walk("../")
