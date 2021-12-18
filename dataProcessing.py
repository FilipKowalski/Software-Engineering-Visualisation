
#a script to optain the data from the MongoDB and print it out to a file in csv format

import pymongo              # for mongodb access
import pprint               # for pretty printing db data

print("Current data in the DB is");

#Let's get the Commit from the db

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

# now that we have data we want to generate an output that works for a visualisation
#im generating a line graph, for this i will need a CSV file containing the date of commit and the number of lines changed
#it will be in this format
#Date,RepoCount,

#get the commits in the repo of id 430669465 which is a group project for an algorithms and
#data structures module in 2nd year

#write the data about commits done by me in this repository

with open('DataOnSoftwareVisualisationRepo.csv', 'w') as f:
    f.write('Date,TotalChanges\n')
    dct = db.commits.find({'commitAuthor': "FilipKowalski",
                              'commitedInRepoId': 430669465
                            })
    for commit in dct:
        pprint.pprint(commit)
        print()
        f.write(commit['commitDateString'] + ',' + str(commit['totalChangesInCommit']) + '\n')
