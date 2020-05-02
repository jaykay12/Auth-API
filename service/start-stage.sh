source venv/bin/activate
export FLASK_ENV=stage
source ./api.env
export ENV='STAGE'
python app.py
