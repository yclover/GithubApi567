import requests
import json
import unittest

def github_api(userID):
    data = requests.get("https://api.github.com/users/%s/repos" % userID)
    response = data.json()

    if data.status_code != 200:
        print("User Not Found")
        return False

    if len(response) == 0:
        print("Zero Repo")
        return False

    for i in range(len(response)):
        repoName = response[i]['name']
        # commits_url = requests.get("https://api.github.com/users/%s/%s" % userID, repoName)
        commits = len(requests.get(response[i]['commits_url'].split("{")[0]).json())
        print("Repo: " + repoName + " Numbers of commits: " + str(commits))

    return True

class TestGithubApi(unittest.TestCase):
    def testGithubApi1(self):
        self.assertEqual(github_api('yclover'), True)



if __name__ == '__main__':
   unittest.main()




