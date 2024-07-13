#!/usr/bin/env python3

from os.path import exists as there, join
from os import getcwd, unlink, listdir
from re import match

class Requirements:
    def __init__(self):
        self.directory = getcwd()
        self.files = listdir(self.directory)
        self.check = False
        for file in self.files:
            if file.lower() == "requirements.txt" or file.lower() == "requirements":
                self.check = True
                self.file = file
                break
    
    @property
    def transfer(self):
        if self.check:
            with open(join(self.directory, self.file), "r+") as rfile:
                lines = rfile.readlines()
            
            for i in range(len(lines)):
                lines[i] = lines[i].replace("\n", "")
            
            with open('pyproject.toml', 'r+') as toml:
                toml_ = toml.readlines()
            
            toml__ = []
            for x in toml_:
                if match(r"^\s*version\s*(.*)", x):
                    toml__.append(x.replace("\n", "")+"\n")
                    toml__.append(f"dependencies = {lines}\n\n")
                else:
                    toml__.append(x)
            
            with open('pyproject.toml', 'w+') as tomlfile:
                tomlfile.writelines(toml__)
            
            unlink(join(self.directory, self.file))

if __name__ == "__main__":
    requiements = Requirements()
    requiements.transfer