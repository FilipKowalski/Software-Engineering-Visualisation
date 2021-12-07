# a a script to clear the db

print("Clearing MongoDB");

import pymongo              # for mongodb access
import pprint               # for pretty printing db data

#Let's get the user object from the db

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB

db.githubuser.delete_many({})
