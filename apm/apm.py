#!/usr/bin/python

# Arduino Package Manager
import requests
import config
import git
from git import Repo
import os
import sys
import os.path
from prettytable import PrettyTable

GITHUB_URL = 'https://api.github.com/'

# Custom user agent
headers = {'User-Agent': 'jcabdala/apm'}

sources = {'Adafruit': 'adafruit'}


def find_repositories(word):
    dircc = GITHUB_URL + "search/repositories?q=" + word + "+arduino+library&sort=forks&order=desc"
    print dircc
    repositories = requests.get(dircc)
    return repositories.json()


def search_library(limit=30):
    results = []
    for source in sources:
        payload = {'q': 'arduino+library',
                   'sort': 'forks',
                   'order': 'desc',
                   'per_page': limit}
        r = requests.get(GITHUB_URL + 'search/repositories',
                         params=payload,
                         headers=headers)

        for i, repo in enumerate(r.json()['items']):
            name = repo['name']
            forks = repo['forks_count']
            r2 = requests.get(repo['url'])
            stars = r2.json()['stargazers_count']
            print stars
            print '{}) {}/{} [{}]{}'.format(i + 1, source, name, forks, '*' * stars)
            results.append(repo)
    return results


def display_repo(repositories):
    t = PrettyTable(['Index', 'name', 'user', 'forks', 'starts', "last update"])
    for rep in repositories["items"][:5]:
        t.add_row(["1", rep["name"], rep["owner"]["login"], rep["forks"], rep["stargazers_count"], rep["updated_at"]])
    print t


def get_repo(repositories, index):
    myrepo = repositories["items"][index]["clone_url"]
    namerepo = repositories["items"][index]["name"]
    nameuser = repositories["items"][index]["owner"]["login"]
    return myrepo, namerepo, nameuser


def download_repo(repourl, name, user):
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


def uninstall(library_name):
    libraries = []
    for dirname, dirnames, filenames in os.walk(config.arduinohome):
        if library_name in dirnames:
            libraries.append(library_name)
    return sorted(libraries)


def main(argv):
    if argv[1] == "install":
        repositories = find_repositories(argv[3])
        # print repositories
        if argv[2] == "-lucky":
            repositories = find_repositories(argv[3])
            repo, name, user = get_repo(repositories, 0)
            download_repo(repo, name, user)
            print "The example's dir name is: ", name, "-", user

        else:
            repositories = find_repositories(argv[2])
            display_repo(repositories)
            try:
                num = int(raw_input('"Select librery by Index [1-5]: "'))
            except ValueError:
                print "Not a number"
            repo, name, user = get_repo(repositories, num)
            download_repo(repo, name, user)
            print "The example's dir name is: ", name, "-", user


main(sys.argv)
