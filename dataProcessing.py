
# a script to do python based access to the github api
# step 4 - Let's store our data in a mongodb

print("Current data in the DB is");


import pymongo              # for mongodb access
import pprint               # for pretty printing db data

#Let's get the user object from the db

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

for user in db.githubuser.find({'location': {'$exists': True}}):
    pprint.pprint(user)
    print()
