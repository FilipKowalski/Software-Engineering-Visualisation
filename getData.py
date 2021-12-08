from github import Github   #github api access
from faker import Faker     #for anonimysing names
from collections import defaultdict
import json                 #for dictionary to string
import pymongo              #for mongodb access
import os

#load the faker and its providers
faker = Faker()
names = defaultdict(faker.name)

#we initialise a PyGithub Github object with our access token
token = os.getenv("TOKEN")
print(token)
githubObject = Github(token)

#getting a repo object
repo = githubObject.get_repo("nadineel/CSU22012-Algorithm-Data-Structure-Group-Project")

repoDict = {
    'id':           repo.id,
    'name':         repo.name,
    'owner_login':  repo.owner.login,
    'language':     repo.language
}

#deleting null values from the dictionary

print ("dictionary is " + json.dumps(repoDict))

for k, v in dict(repoDict).items():
    if v is None:
        del repoDict[k]

print ("cleaned dictionary is " + json.dumps(repoDict))


repoCommits = repo.get_commits()

for commit in repoCommits:
    comDct = {'commitAuthor': commit.author.name
    }
    for k, v in dict(comDct).items():
        if v is None:
            del comDct[k]
    print("commitAuthor: " + json.dumps(comDct))
