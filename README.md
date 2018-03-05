[![CircleCI](https://circleci.com/gh/asn10038/AutoIntern-Django.svg?style=svg)](https://circleci.com/gh/asn10038/AutoIntern-Django)
---
# AutoIntern

A banking workflow app with more to come. Currently under construction.
https://autointern-prod.appspot.com/
---
# How To Use

### Git Clone
Here we are cloning the repo to your file system
1. Open Terminal
2. Navigate to where you want this repo
3. "git clone https://github.com/asn10038/AutoIntern-Django.git"

### Create a Git Branch And Open a Pull Request
Note: ALL WORK should be done on your own github branch. When you want to make a change to the repo make sure you are doing it on your own branch and then creating a pull request.
1. Create a branch and switch to it using "git checkout -b branch_name". Either name your branch after yourself (i.e. nicks_branch) or after a feature you are working on.
2. Edit code and "git add" as normal!
3. Commit the code using "git commit -m " < Message > "". Note: Make sure your commit messages are informational (*cough cough* Anthony). This saves time in the future if we have to revert your crappy changes.
4. When you are ready to push changes use "git push -u origin branch_name". Note: You will only have to do this the first time per branch you make, afterwords you can use "git push" as usual. If you do not do this the first time, however, it will simply push your changes to master and we do not want this.
5. Navigate to https://github.com/asn10038/AutoIntern-Django and go to "Pull Requests" and create one from your branch to master! Make sure to assign people to the pull request and DO NOT ACCEPT YOUR OWN PR.

### Making A Virtual Enviornment
Here we are making a virtual enviornment, something that we use to make sure the enviornment we are coding in is standard across all programmers. More info: https://www.python.org/dev/peps/pep-0405/
1. In /AutoIntern-Django type "python3 -m venv autointernvenv". This creates an enviornment called autointernvenv at /AutoIntern-Django. You need to do this once. Note: You will see a directory called autointernvenv, this stores the enviornment. Don't mess with it. It will also not be committed because it is in our .gitignore file.
2. Type "source autointernvenv/bin/activate" to activate the environment. Your commandline will change to note that the enviornment is different than default. All coding and testing should be done with this enviornment. (so you'll have to use this command every time you make changes or test).
3. Type "pip install -r requirements.txt". This downloads the packages in our enviornment to the enviornment on your machine. You will only have to run this command when the requirements.txt changes (and when setting up the enviornment).
4. To deactivate the enviornment type "deactivate". It's that simple.

### Start The Database Proxy
This connects your local machine to the database. Currently, it connects it to our production database (this will change ASAP), so don't mess with it yet. However, to run the code locally you will have to first start the database proxy.
1. Follow the instructions here <a href='https://cloud.google.com/sdk/downloads#interactive'>Google Cloud SDK</a> for downloading the interactive installer. You will have to do this once.
2. To start the Proxy, open a new terminal window and direct it to /AutoIntern-Django. Then type "./cloud_sql_proxy_unix -instances="autointern-196523:us-east1:terndb1"=tcp:5432" if on a unix machine (mac) and "./cloud_sql_proxy_linux -instances="autointern-196523:us-east1:terndb1"=tcp:5432" if on a unix machine. Leave this running to test the code locally.

### Start the Application
Here we will run the application and allow you to connect to it locally.
1. Make sure you have the database proxy running in another terminal window.
2. Make sure your virtual environment is active.
3. Type "python manage.py runserver".
4. Go to "http://localhost:8000/" to see the website!

### Run All Tests
Using Django there is a handy trick to running all of the tests written.
1. "python manage.py test"

### Configure Your Database to be the Model Database
This only has to be done if the model changes. Very infrequently.
1. "python manage.py makemigrations"
2. "python manage.py migrate"


## Licensing

TODO
