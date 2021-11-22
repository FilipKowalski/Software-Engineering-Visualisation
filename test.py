#inport Githum from the PyGithub library
from github import Github
import json                 #for dictionary to string

#we initialise a PyGithub Github object with our access token
githubObject = Github("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")

#getting a user object and building a data dictionary
user = githubObject.get_user()

userDict = {'user': user.login,
            'fullname': user.name,
            'location': user.location,
            'company': user.company
            }

print ("dictionary is " + json.dumps(userDict))
