#!/usr/bin/env python3

from os import listdir, getcwd
from os.path import join, isdir, isfile, basename

class Check:
    def __init__(self):
        self.directory = getcwd()
        self.files = listdir(self.directory)

        self.checks = {}
    
    @property
    def run(self):
        # check src
        if "src" in self.files and isdir(join(self.directory, "src")):
            self.checks["src"] = "present"
        elif "src" in self.files and isfile(join(self.directory, "src")):
            self.checks["src"] = "partial"
        else:
            self.checks["src"] = "not_present"
        
        # check toml file
        if "pyproject.toml" in self.files and isfile(join(self.directory, "pyproject.toml")):
            self.checks["TOML"] = "present"
        elif "pyproject.toml" in self.files and isdir(join(self.directory, "pyproject.toml")):
            self.checks["TOML"] = "partial"
        else:
            self.checks["TOML"] = "not_present"
        
        # check tests dir
        if "tests" in self.files and isdir(join(self.directory, "tests")):
            self.checks["tests"] = "present"
        elif "tests" in self.files and isfile(join(self.directory, "tests")):
            self.checks["tests"] = "partial"
        else:
            self.checks["tests"] = "not_present"
        
        # for i in range(len(self.files)):
        #     self.files[i] = join(self.directory, self.files[i])

        # generate an intermediate file named .inter

        with open(".inter", "w+") as interfile:
            interfile.write(f"src:{self.checks['src']}\n")
            interfile.write(f"toml:{self.checks['TOML']}\n")
            interfile.write(f"tests:{self.checks['tests']}")

if __name__=="__main__":
    check = Check()
    check.run