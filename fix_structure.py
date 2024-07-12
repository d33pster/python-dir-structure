#!/usr/bin/env python3

from os import getcwd, makedirs, rename, unlink, popen
from os.path import join, basename
from colorama import init as color, Fore as _

class Fix:
    def __init__(self):
        color()
        self.directory = getcwd()

        with open(".inter", "r+") as interfile:
            self.report = interfile.readlines()
        
        unlink(join(self.directory, ".inter"))
        
        self.__rep__ = {}
        
        # print report
        print(f"{_.GREEN}Structure Report ~{_.RESET}")
        for line in self.report:
            title = line.split(":")[0]
            stat = line.split(":")[1].replace("\n", "")
            if stat == "partial":
                if title == "src" or title == "tests":
                    status = "Directory expected but File found."
                else:
                    status = "File expected but File found."
            else:
                status = stat
            
            print(f"{title}: {status}"),
            self.__rep__[title] = status
    
    @property
    def run(self):
        self.__change__: bool = False

        # fix src
        if self.__rep__["src"] == "not_present":
            makedirs(join(self.directory, "src"))
            print(f"{_.GREEN}@Created{_.RESET} Dir - {_.BLUE}{join(self.directory, 'src')}{_.RESET}")
            self.__change__ = True
        elif self.__rep__["src"] == "partial":
            print(f"{_.RED}@Already-Present!{_.RESET} {join(self.directory, 'src')} {_.BLUE}(FILE){_.RESET}")
            rename(join(self.directory, "src"), join(self.directory, "src.file"))
            print(f"{_.BLUE}@Renamed{_.RESET} File - {join(self.directory, 'src')} {_.GREEN}{join(self.directory, 'src.file')}{_.RESET}")
            makedirs(join(self.directory, "src"))
            print(f"{_.GREEN}@Created{_.RESET} Dir - {_.BLUE}{join(self.directory, 'src')}{_.RESET}")
            self.__change__ = True
        else:
            pass

        # fix tests
        if self.__rep__["tests"] == "not_present":
            makedirs(join(self.directory, "tests"))
            print(f"{_.GREEN}@Created{_.RESET} Dir - {_.BLUE}{join(self.directory, 'tests')}{_.RESET}")
            self.__change__ = True
        elif self.__rep__["tests"] == "partial":
            print(f"{_.RED}@Already-Present!{_.RESET} {join(self.directory, 'tests')} {_.BLUE}(FILE){_.RESET}")
            rename(join(self.directory, "tests"), join(self.directory, "tests.file"))
            print(f"{_.BLUE}@Renamed{_.RESET} File - {join(self.directory, 'tests')} {_.GREEN}{join(self.directory, 'tests.file')}{_.RESET}")
            makedirs(join(self.directory, "tests"))
            print(f"{_.GREEN}@Created{_.RESET} Dir - {_.BLUE}{join(self.directory, 'tests')}{_.RESET}")
            self.__change__ = True
        else:
            pass
        
        # fix toml
        if self.__rep__["toml"] == "not_present":
            with open("pyproject.toml", "w+") as toml:
                toml.write("[build-system]\nrequires = [\"setuptools>=61.0\"]\nbuild-backend = \"setuptools.build_meta\"\n\n")
                toml.write(f"[project]\nname = \"{basename(self.directory)}\"\nversion = \"0.1\"\n\n")
                toml.write(f"[project.urls]\nGitHub = \"{popen('git remote get-url origin').read().replace('\n', '')}\"")
            print(f"{_.GREEN}@Created{_.RESET} {join(self.directory, 'pyproject.toml')}")
            self.__change__ = True
        elif self.__rep__['toml'] == "partial":
            print(f"{_.RED}@Already-Present!{_.RESET} {join(self.directory, 'pyproject.toml')} {_.BLUE}(DIR){_.RESET}")
            rename(join(self.directory, "pyproject.toml"), join(self.directory, "pyproject.toml.dir"))
            print(f"{_.BLUE}@Renamed{_.RESET} Dir - {join(self.directory, 'pyproject.toml')} {_.GREEN}{join(self.directory, 'pyproject.toml.dir')}{_.RESET}")
            with open("pyproject.toml", "w+") as toml:
                toml.write("[build-system]\nrequires = [\"setuptools>=61.0\"]\nbuild-backend = \"setuptools.build_meta\"\n\n")
                toml.write(f"[project]\nname = \"{basename(self.directory)}\"\nversion = \"0.1\"\n\n")
                toml.write(f"[project.urls]\nGitHub = \"{popen('git remote get-url origin').read().replace('\n', '')}\"")
            print(f"{_.GREEN}@Created{_.RESET} {join(self.directory, 'pyproject.toml')}")
            self.__change__ = True
        else:
            pass

        with open(".inter", "w+") as interfile:
            if self.__change__:
                interfile.write("True")
            else:
                interfile.write("False")
            

if __name__ == "__main__":
    fix = Fix()
    fix.run