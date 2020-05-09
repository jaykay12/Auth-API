source venv/bin/activate
source ./api.env

if [ "$1" == "--stage" -o "$1" == "-s" ]; then
  export ENV='STAGE'; export FLASK_ENV=stage
else
  export ENV='DEVELOPMENT'; export export FLASK_ENV=development
fi

python app.py
