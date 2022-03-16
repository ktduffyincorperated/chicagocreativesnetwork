# README

This is a draft template for the dynamic site generation aspect of the Chicago creates network project.
To use python3 and django must be installed.

I(Thoth Gunter) recommend installing python3 using the conda package installer, https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation.
> The following will contain instructions for the terminal. MacOs and Linux should be familiar with the terminal. 
> Windows users should use the Window's shell or Anaconda Shell, which comes with the conda package installer. 
Once conda is installed create a virtual environment using the following terminal command `conda create <NAME>`.
Activate the environment using: `conda activate <NAME>`.

To install django run: `conda install django`.

Now that python and django have been installed we can locally deploy our site.
To deploy run: `python manage.py runserver`.
This command will deploy our site through a local python server.
After running the command you will receive and error along with a url. 
The error will read something like the following:

```
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```

You will need to run 'python manage.py migrate' to remove this error and to gain access to user registration and login features. 


## Adding static content
If you would like to make alterations to the html, css, or js you can find the templates in the `home/static` and `home/templates` folder. 
`static` contains css and js. `templates` contains html.  These files contain the most basic examples of content.


# Additional Dependencies
 - Pillow  # an image processing library.





