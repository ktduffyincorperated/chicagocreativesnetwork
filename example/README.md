# Chicago Creatives Network

This is a draft template for the dynamic site generation aspect of the Chicago creates network project.

## Installation

### Prequisites
- Python3

### Install Dependencies
1. Create a virtual environment inside the `/example` directory, activate the environment, and install dependencies.
```
cd example
virtualenv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

### Run migrations
*This step creates the database and tables and should only be done during the first install.*
```
python manage.py migrate
```

## Local Development
To run the app on a local server:
```
python manage.py runserver
```
Note that you will need to have an active virtual environment so run `source ./venv/bin/activate` if you haven't already.




## Adding static content
If you would like to make alterations to the html, css, or js you can find the templates in the `home/static` and `home/templates` folder. 
`static` contains css and js. `templates` contains html.  These files contain the most basic examples of content.