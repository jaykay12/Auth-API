## Building and Running on Dev Environment
+ Clone the repo and check python and pip version on machine using `python --version` and `pip --version`
+ Install virtualenv on machine using `pip install virtualenv` and verify using `virtualenv --version`
+ Configure virtualenv for project
  - Change into project subdirectory using `cd service`
  - Create a python virtual environment for the project using `virtualenv venv`
  - Load virtual environment using `source venv/bin/activate`
  - Install project dependencies using `pip install -r ../requirements.txt`
  - You can unload virtual environment using `deactivate`
 + Create a file **api.env** with following content:   
 `export SECRET_KEY='<API-SECRET-KEY>'`   
 `export DEVELOPMENT_DATABASE_URL='sqlite:///auth.db'`    
 `export ENV='DEVELOPMENT'`
 + Run on dev environment using `bash start-dev.sh`


## Running on Stage Environment
+ Install PostgreSQL on machine using `sudo apt-get install postgresql` and verify using `psql --version`
+ Configure PostgreSQL on local machine.
  - Login to postgres console using `sudo -u postgres psql`
  - Create role using `CREATE USER <POSTGRES_USER> WITH PASSWORD '<POSTGRES_PASS>'`
  - Create DB using `CREATE DATABASE <POSTGRES_DB>`
  - Grant permissions using `GRANT ALL PRIVILEGES ON DATABASE <POSTGRES_DB> TO <POSTGRES_USER`
  - Close postgres console using `\q`
+ Add the following line to the file **api.env**   
`export STAGE_DATABASE_URL='postgresql+psycopg2://<POSTGRES_USER>:<POSTGRES_PASS>@localhost/<POSTGRES_DB>'`
+ Run on stage environment using `bash start-stage.sh`

## Running on Production Environment
+ Install Heroku CLI on machine using `curl https://cli-assets.heroku.com/install-ubuntu.sh | sh` and verify using `heroku --version`
+ Configure Heroku deploy on local machine.
  - Login to heroku account using `heroku login`
  - Create heroku app using `heroku create auth-api-flask`
  - Set buildpack for the app using `heroku buildpacks:set heroku/python`
  - Create Procfile with the content as  
  `web: cd service && gunicorn app:app`
+ Login to Heroku platform and add `Heroku Postgres` as an add-on.
+ Modify config vars as follows:  
 `PRODUCTION_DATABASE_URL = <HEROKU-PROVIDED-URL>`    
 `ENV = 'PRODUCTION'`     
 `SECRET_KEY = <API-SECRET-KEY>`
+ Push the project to Heroku platform using `git push heroku master`
+ Configure aut-deploy from GitHub hooks.

## Running tests and Travis CI integration
+ Add the following line to the file **api.env**   
`export TESTING_DATABASE_URL='sqlite:///:memory:'`
+ Run tests on dev environment using `bash run-tests.sh`
+ Signup to Travis CI using GitHub and toggle the button to ON for Auth-API from `https://travis-ci.org/github/jaykay12/Auth-API`
+ Add the following entries in `Environment Variables` of Travis CI
  `ENV = 'TESTING'`      
  `SECRET_KEY = <API-SECRET-KEY`      
  `TESTING_DATABASE_URL = 'sqlite:///:memory:'`
+ Add a YAML file in root folder of repo namely, `travis.yml` and add configurations in it.
