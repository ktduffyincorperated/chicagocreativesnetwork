#README

This is a test template for the final site.
To use python and django must be install on your computer. 

To use django install python3 using conda, https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation.
Once conda is installed install create a virtual enviroment using 'conda create <NAME>', in your terminal.
Activate the enviroment using: conda activate <NAME>.

To install django run 'conda install django'.

To run the site locally run 'python manage.py runserver'.
You will recieve the following error:

'
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
'

You will need to run 'python manage.py migrate' to remove this error and allow one the ability to use the user space. 



