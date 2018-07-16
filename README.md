# The Three Astronauts


## OSX Local Development Instructions

### Install Homebrew

##### The OS X package manager can be installed via the command line:
```bash
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

##### After Installing, run doctor/update
```bash
$ brew doctor
...
$ brew update
```

### Install pip

We use [pip](http://pypi.python.org/pypi/pip) for managing Python packages and dependencies. pip is a replacement for easy_install, the default package manager.

Install with the following:

```bash
$ sudo easy_install pip
```

### Install / Configure VirtualEnv & VirtualEnvWrapper
You probably want to use [virtualenv](http://pypi.python.org/pypi/virtualenv) to manage your Python environments. Better still is virtualenvwrapper: [virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper).

#### Install both with the following:

```bash
$ pip install virtualenv virtualenvwrapper
```

##### After installing virtualenvwrapper, add the following to your .bash_profile:

```bash
$ export WORKON_HOME={{/path/to/your/virtualenv/directory/}}
$ export VIRTUALENVWRAPPER_HOOK_DIR=$WORKON_HOME
$ export VIRTUALENVWRAPPER_LOG_DIR=$WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh
```

##### To create a your virtualenv using virtualenvwrapper:

```bash
$ mkvirtualenv t3a
```

##### To work on the project (and activate the virtualenv) once you've created it, run:

```bash
$ workon t3a
```

NOTE: You should do this whenever you want to run the website locally. You can deactivate the environment with `$ deactivate` but it is not necessary.

### Installing backend dependencies

After you have activated your virtual environment, install project dependencies:

(make sure you're in the project directory and see the file `/t3a/t3a/requirements.txt`)

```bash
$ pip install -r requirements.txt
```

### Project settings

##### Create a `settings/development.py` file from the available `settings/development.example` file:

```bash
$ cp americana/settings/development.example americana/settings/development.py
```

### Database
We use [PostgreSQL](http://www.postgresql.org/). 

##### Install PostGres using Homebrew, which you installed earlier)

```bash
$ brew install postgres
...
$ ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents
```

##### Create the database:

```bash
$ createdb t3a
```

##### Then, create a superuser

```bash
$ python manage.py createsuperuser
```

##### List available migrations (if you're curious):

```bash
$ python manage.py migrate --list
```

##### migrate your database:

```bash
$ python manage.py migrate
```

NOTE: If you have already initialized and migrated a database, you must destroy and re-initialize it before loading seed data:

```bash
$ dropdb t3a
$ createdb t3a
```

### Running the development server

##### (optional) Add `pmpy` alias to your `.bash_profile` so you can run `pmpy ...` instead of `python manage.py ...`

Edit `~/.bash_profile` and add the following:

```
alias pmpy="python manage.py"
```

Finally, to run the development server on your local machine:

```bash
$ python manage.py runserver
```

To view the site, visit [http://localhost:8000](http://localhost:8000) in your browser.


##### Be a good neighbor – keep this file up to date!