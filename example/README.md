#README

This is a draft template for the dynamic site generation as part of the chicago creates network project.
To use python3 and django must be installed.

I recommend installing python3 using the conda package installer, https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation.
Once conda is installed create a virtual enviroment using the following terminal command 'conda create <NAME>'.
Activate the enviroment using: 'conda activate <NAME>'.

To install django run: 'conda install django'.

Now that python and django have been installed we can locally deploy our site.
To do this run following command: 'python manage.py runserver'.
This command will deploy our site through a local python server.
After running the command you will recieve and error along with a url. 
The error will read something like the following:

'
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
'

You will need to run 'python manage.py migrate' to remove this error and to gain access to user registration and login features. 





