sudo apt-get update
sudo apt-get install -y python3
pip install virtualenv
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python petpal/petpal/manage.py makemigrations
python petpal/petpal/manage.py migrate --run-syncdb