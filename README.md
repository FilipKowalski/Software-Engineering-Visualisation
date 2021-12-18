# Software-Engineering-Visualisation

This Visualisation is used to visualise the total changes to a repository in a commit using a line graph that graphs changes made in a commit versus the date a commit was made for a given repository.

# Dependencies
-Python3

# How To Run
Once the Visualisation is running, it can be viewed on http://localhost:8000/

if running for the first time -
  run the firstTimeRun.sh script,
  this script will download all needed python packages,
  launch a docker container running a MongoDB in the background,
  and finally collect and visualise the data, this will be displayed on http://localhost:8000/

for consecutive runs -
 simply run the run.sh script which will collect and visualise the data and display this on http://localhost:8000/
