# Author: Sijie Yu
# Course: SSW-567A

import requests
import json
import unittest

def github_api(userID):
    # get the whole data from the specific user
    data = requests.get("https://api.github.com/users/%s/repos" % userID)

    # convert it into json
    response = data.json()

    # check invalid user or non repo
    if data.status_code != 200:
        print("User Not Found")
        return False

    if len(response) == 0:
        print("Zero Repo")
        return False

    # traversal the whole data, get the repoName by the array index
    # then get the commit in json by splitting the str to remove the symbol
    for i in range(len(response)):
        repoName = response[i]['name']
        # commits_url = requests.get("https://api.github.com/users/%s/%s" % userID, repoName)
        commits = len(requests.get(response[i]['commits_url'].split("{")[0]).json())
        print("Repo: " + repoName + " Numbers of commits: " + str(commits))

    return True

# testcase
class TestGithubApi(unittest.TestCase):
    def testGithubApi1(self):
        self.assertEqual(github_api('yclover'), True)

    def testGithubApi2(self):
        self.assertEqual(github_api('EmanAlOmar'), True)

    def testGithubApi3(self):
        self.assertEqual(github_api('francescaseverino'), True)



if __name__ == '__main__':
   unittest.main()




