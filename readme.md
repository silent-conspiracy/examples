Recommended OS:
Ubuntu 12.04 LTS

Required softwares: 
1. Python2.7 (Recommended) - Provided default on Ubuntu 12.04 LTS
2. pip Python Package - run these commands on terminal
   'wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py'
   'python get-pip.py'
3. virtualenv and virtualenvwrapper
   'pip install virtualenv'
   'pip install virtualenvwrapper'

Virtual Environment Setup:
1. After installing virtualenv and virtualenvwrapper, edit ~/.bashrc by adding these lines at the bottom:

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Development
source /usr/local/bin/virtualenvwrapper.sh

2. Exit and open a new terminal.
3. Run this command: 'mkvirtualenv 1northsoft-examples'
4. Make sure that whenever we need to run the server we need to be in the virtualenv. The same when we want to install new python packages.
5. More about virtualenv: 'http://www.silverwareconsulting.com/index.cfm/2012/7/24/Getting-Started-with-virtualenv-and-virtualenvwrapper-in-Python'


Installing required packages used in project
1. Find 'requirements.txt' in the project folder.
2. Run 'workon 1northsoft-examples' and make sure the terminal is under 1northsoft-examples environment.
3. Run 'pip install -r requirements.txt' -- installs all required packages for this project.


Storing Entities
1. Django uses MVC Framework and entities are stored into the database according to the attributes of the entity / model.
2. When a project is created the project structure is as follows:

   MyProject (created using 'django.admin.py startproject MyProject')
     |-- manage.py
     |-- MyProject (Contains all settings regarding the project)
           |-- __init__.py
           |-- settings.py  # Project settings
           |-- urls.py      # Url specification and settings
           |-- wsgi.py      # For use with Apache
     |-- NewApplication (created using 'python manage.py startapp NewApplication'
           |-- __init__.py
           |-- admin.py     # Admin page configuration
           |-- models.py    # Add models / entities to be stored in database here
           |-- tests.py     # Unit Tests codes.
           |-- views.py     # View function to handle requests.

3. How to add models: 'https://docs.djangoproject.com/en/1.6/topics/db/models/'
4. Model field types: 'https://docs.djangoproject.com/en/1.6/ref/models/fields/#model-field-types'
5. After added the models, to create the database tables, run:
   "python manage.py syncdb"
6. Check the database tables and they are created.


Setting up Django with databases other than sqlite3:
1. Default django database used is sqlite3, a file-based database system, under the extension '.db'
2. Settings of other databases: https://docs.djangoproject.com/en/dev/ref/databases/#connecting-to-the-database


