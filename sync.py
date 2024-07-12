#!/usr/bin/env python3

from os import system as run, unlink, getcwd, environ
from os.path import join

if __name__ == "__main__":
    with open('.username', 'r+') as ufile:
        username = ufile.read().replace("\n", '')
    
    unlink(join(getcwd(), '.username'))

    with open('.repo', 'r+') as rfile:
        repo = rfile.read().replace("\n", '')
    
    unlink(join(getcwd(), '.repo'))

    run(f"git push https://{username}:{environ['GITHUB_TOKEN']}@github.com/{username}/{repo}.git")