from github import Github   #github api access
import json                 #for dictionary to string
import pymongo              #for mongodb access

#we initialise a PyGithub Github object with our access token
githubObject = Github("")

#getting a user object and building a data dictionary
user = githubObject.get_user()

userDict = {'user': user.login,
            'fullname': user.name,
            'location': user.location,
            'company': user.company
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
