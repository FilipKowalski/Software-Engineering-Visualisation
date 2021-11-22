#inport Githum from the PyGithub library
from github import Github
#we initialise a PyGithub Github object with our access token
githubObject = Github("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")

#getting a user object and printing some trivial details
user = githubObject.get_user()
print("user:    " + user.login)
print("fullname:" + user.name)
print("location:" + user.location)
print("company: " + user.login)
