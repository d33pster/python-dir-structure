#!/usr/bin/env python3

from os import environ, getcwd
from os.path import join
from git import Repo

class Sync:
    def __init__(self):
        self.__token = environ['GITHUB_TOKEN']
    
    @property
    def execute(self) -> bool:
        path = getcwd()
        repo = Repo(path)

        if repo.is_dirty():
            repo.index.add('*')
            with open(join(environ['action_path'], "version"), "r+") as versionfile:
                version = versionfile.read().replace("\n", "")
            repo.index.commit(f"Structure Update (pps@v{version})")
            origin = repo.remote()
            origin.push()
            return True
        else:
            return False

def main():
    sync = Sync()
    if sync.execute:
        print("Updated!")
    else:
        print("No changed this time! All good.")

if __name__ == "__main__":
    main()