# README #

This is a very basic graphql application in which you can perform Query and Mutations 
In this application authentication and unittest cases are also covered.

### Dependencies ###

* Python 3.8
* SqlLite

### Getting Started ###

* Right now there no other db are integrated with this application so we can go with default sqllite3


### Virtual Environment Setup ###

* If you're on linux/mac OS then for creating virtual environment use "virtualenv -p python3 venv"
* If you're on Windows OS then for creating virtual environment use "virtualenv python venv"
* Move to virtualenv and activate its environment for linux "source venv\bin\activate" for windows "venv\Scripts\activate"


### GitHub Repository Setup ###

* Go to the link: https://github.com/<OWNER_NAME>/<REPO_NAME>
* Fork the original git repository in this case it is "https://github.com/styam/django_graphene.git"
* Using Command Line, navigate to the repository
* Create a new branch with existing branch 


### Dependency Setup ###

* Install requirements: "pip install -r requirements.txt".
* Run migrations: "python manage.py migrate"
* Create superuser: "python manage.py createsuperuser".


### Running Sample GraphQl API###

* Go to http://127.0.0.1:8000/graphql/
* Go to http://127.0.0.1:8000/home/ 

### Running Test Cases###
* For running the unittest cases you don't need to run the django server
* Just type pytest or py.test on terminal that's it :)
* One folder with the name"htmlcov" get generated in your root directory
* In "htmlcov" open "index.html" here you can see all Coverage report: with %

### Contribution guidelines ###

* Running tests: "coverage run --source='.' manage.py test"
* Checking tests coverage: "coverage report"
* Checking tests lines missing/covered: "coverage report -m"
* Checking code quality "pylint "
* Double checking the diff quality before commit "git diff-index --name-only HEAD | grep .py| xargs pylint"


### Push-Pull and PR Understanding ###

* To pull the code from upstream (Get changes from the original repo to your forked repo) : 
        
        1) git fetch upstream <BRANCH_NAME (if required)>
        2) git merge upstream/<BRANCH_NAME> <BRANCH_NAME>
        3) git push origin <BRANCH_NAME> (This is done to push the changes captured from original repository to your forked repository)


* To push the code (Push your changes): 
        
        1) git push origin <BRANCH_NAME>


* To create a pull request: 

        1) Go to bitbucket link: https://github.com/<USER_NAME>/<REPO_NAME>.
        2) Select Pull Requests.
        3) Create a Pull Request (** Please be 100% sure about the source and destination code repo and branch where you want to generate the pull request **).
