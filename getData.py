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
token = os.getenv('GITHUB_PAT')
print(token)
githubObject = Github(token)

#getting a user object and building a data dictionary
user = githubObject.get_user("sfdye")

userDict = {'user':         names[user.login].replace(" ",""), #anonimysing
            'fullname':     names[user.name],
            'location':     user.location,
            'company':      user.company,
            'public_repos': user.public_repos
            }

print ("dictionary is " + json.dumps(userDict))

#store the dictionary in a mongodb

#first we need to remove all null fields from the dictionary, because
#if we dont we will end up with null fiends in the db. this will cause us
#lots of debugging problems later. only store actual data in the database

for k, v in dict(userDict).items():
    if v is None:
        del userDict[k]

print ("cleaned dictionary is " + json.dumps(userDict))

#now lets store the data

#establish connection
conn  ="mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

#create a database
db = client.classDB

db.githubuser.insert_many([userDict])

# now for demo purposes we'll get some data. We'll get the accounts followers
# and for each of them we'll get and add a count of the number of repos they have
fc = user.followers
print ("followers: " + str(fc))

# now lets get those followers
fl = user.get_followers()

for f in fl:
    dct = {'user':         names[f.login].replace(" ",""),
           'fullname':     names[f.name],
           'location':     f.location,
           'company':      f.company,
           'public_repos': f.public_repos
           }
    for k, v in dict(dct).items():
        if v is None:
            del dct[k]

    print("follower: " + json.dumps(dct))
    #adding followers to the database
    db.githubuser.insert_many([dct])
