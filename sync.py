#!/usr/bin/env python3

from git import Repo
from os import getcwd, unlink
from os.path import join

class Sync:
    def __init__(self) -> None:
        with open('.inter', "r+") as interfile:
            self.run_check = interfile.read().replace("\n", "")
        unlink(join(getcwd(), '.inter'))

    
    @property
    def run(self):
        if self.run_check == "True":
            self.repo = Repo(getcwd())
            try:
                # add
                self.repo.index.add("*")

                # commit
                self.repo.index.commit("STRUCTURE UPDATE (pps@v4)")

                # get origin
                origin = self.repo.remote()
                
                # push
                origin.push()

                print("Structure Updated")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    sync = Sync()
    sync.run