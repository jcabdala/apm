#!/usr/bin/python

# Arduino Package Manager
import requests
import config
import git
from git import Repo
import os
import sys
import os.path


def find_repositories(word):
    dircc = "https://api.github.com/search/repositories?q="+word+"+arduino+library&sort=forks&order=desc"
    print dircc
    repositories = requests.get(dircc)
    return repositories.json()


def get_repo(repositories, index):
    myrepo = repositories["items"][index]["clone_url"]
    namerepo = repositories["items"][index]["name"]
    nameuser = repositories["items"][index]["owner"]["login"]
    return myrepo, namerepo, nameuser


def downloadrepo(repourl, name, user):
    home_folder = os.path.expanduser('~')
    repodir = home_folder + config.arduinolib + name + "-" + user
    print repodir
    try:
        Repo.clone_from(repourl, repodir)
        print "git ok"
    except git.GitCommandError:
        print "git url error"


def freeze():
    libraries = []
    for dirname, dirnames, filenames in os.walk(config.arduinohome):
        if '.git' in dirnames:
            # don't go into any .git directories.
            # dirnames.remove('.git')
            library = os.path.basename(dirname)
            libraries.append(library)
            print '{} - {}'.format(os.path.basename(dirname), dirname)
    return sorted(libraries)


def main(argv):
    if argv[1] == "install":
        repositories = find_repositories(argv[3])
        #`print repositories
        if argv[2] == "-lucky":
            repo, name, user = get_repo(repositories, 0)
            downloadrepo(repo, name, user)
            print "The example's dir name is: ", name, "-", user
        # else:


main(sys.argv)
