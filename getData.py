from github import Github   #github api access
from faker import Faker     #for anonimysing names
from collections import defaultdict
from datetime import datetime
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

repoCommits = repo.get_commits()

for commit in repoCommits:
    commitFiles = commit.files
    fileChanges = 0

    for file in commitFiles:
        fileChanges += file.additions + file.deletions + file.changes

    comDct = {
        'commitAuthor': commit.commit.author.name,
        'commitDateString':   (commit.commit.author.date).strftime("%Y/%m/%d"),
        'totalChangesInCommit': fileChanges
    }
    for k, v in dict(comDct).items():
        if v is None:
            del comDct[k]
    print("commit: " + json.dumps(comDct))
