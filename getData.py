from github import Github           #github api access
from collections import defaultdict #for storing data
from datetime import datetime       #for changing datetime object to a string
import json                         #for dictionary to string
import pymongo                      #for mongodb access
import os                           #for getting envoiroment variable

def getCommitsInRepoAndStoreToDb(repoName, DB, gitHubObject):
    #getting a repository
    repo = githubObject.get_repo(repoName)

    #getting the commits from that repository
    repoCommits = repo.get_commits()

    for commit in repoCommits:
        commitFiles = commit.files
        fileChanges = 0

        for file in commitFiles:
            fileChanges += file.additions + file.deletions + file.changes

        comDct = {
            'commitedInRepoId': repo.id,
            'commitAuthor': commit.commit.author.name,
            'commitDateString':   (commit.commit.author.date).strftime("%Y/%m/%d"),
            'totalChangesInCommit': fileChanges
        }

        print(dict(comDct).items())

        #if there are null values, delte them
        for k, v in dict(comDct).items():
            if v is None:
                del comDct[k]

        #dont store commits that are greater than 10000 to avoid massive files added being added to total changes
        if comDct.get('totalChangesInCommit') <= 10000:
            print("commit: " + json.dumps(comDct))
            db.commits.insert_many([comDct])


if __name__ == "__main__":
    #we initialise a PyGithub Github object with our access token
    token = os.getenv("TOKEN")
    print(token)
    githubObject = Github(token)

    #establish connection
    conn  ="mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)

    #create a database
    db = client.classDB

    getCommitsInRepoAndStoreToDb("FilipKowalski/Software-Engineering-Visualisation", db, githubObject)
#    getCommitsInRepoAndStoreToDb("lzfellipe/SWENG_project_22", db)
