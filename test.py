#inport Githum from the PyGithub library
from github import Github
#we initialise a PyGithub Github object with our access token
githubObject = Github("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")

#getting a user object and printing some trivial details
user = githubObject.get_user()
print("user:     " + user.login)

if user.name is not None :
    print("fullname: " + user.name)

if user.location is not None :
    print("location: " + user.location)

if user.company is not None :
    print("company:  " + user.company)
