## Building and Running on Dev Environment


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
+ Confiugre Heroku deploy on local machine.
  - Login to heroku account using `heroku login`
  - Create heroku app using `heroku create auth-api-flask`
  - Set buildpack for the app using `heroku buildpacks:set heroku/python`
  - Create Procfile with the content as  
  `web: cd service && gunicorn app:app`
+ Login to Heroku platform and add `Heroku Postgres` as an add-on.
+ Modify config vars as follows:
  - PRODUCTION_DATABASE_URL = ''
  - ENV = PRODUCTION
  - SECRET_KEY = ''
+ Push the project to Heroku platform using `git push heroku master`
+ Configure aut-deploy from GitHub hooks.
