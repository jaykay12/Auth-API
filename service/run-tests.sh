source venv/bin/activate
source ./api.env
export ENV='TESTING'
python -m unittest discover -s tests -t ../
