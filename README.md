# Get Started (Developement mode)

**1 - Clone the repository :**

`git clone git@github.com:TavaresDylan/Dylan_tavares_TP_Django.git`

**2 - Install virtual environment and dependencies :**

Create the virtual environment

`python3 -m venv venv`

Activate the env

`source ./venv/bin/activate`

Install required dependencies

`pip install -r requirements.txt`

**3 - Make the database migrations :**

`python manage.py makemigrations`

&

`python manage.py migrate`

**4 - Run the server :**

`python manage.py runserver`