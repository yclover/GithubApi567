# Author: Sijie Yu
# Course: SSW-567A

import requests
import json
import urllib.parse
from urllib import response


repoURL = "https://api.github.com/users/EmanAlOmar/repos"
commitsURL = "https://api.github.com/users/EmanAlOmar/repos/commits"
def getApi():
    response = requests.get(repoURL)

    if response.ok:
        return response
def getCommits():
    response = requests.get(commitsURL)
    if response.ok:
        return response
    else:
        return None





