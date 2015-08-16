#!/usr/bin/python

# Arduino Package Manager
import requests
import config
import git
from git import Repo
import sys


def find_repo(word):
    repositories = requests("https://api.github.com/search/repositories?q="+word+"+arduino+library&sort=forks&order=desc")
    myrepo = repositories["item"][0]["clone_url"]
    return myrepo


def download(repodir):
    try:
        Repo.clone_from(repodir, config.arduinohome)
    except git.GitCommandError:
        print "git url error"


print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
