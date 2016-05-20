## Installation guide

### Crop Compass API Developer Setup (MacOS)

This procedure has been adapted from the [API setup in the Hack Oregon or-agriculture repository](https://github.com/hackoregon/or-agriculture/blob/master/api/cropcompass-api-setup.mkdn).

#### Clone the Django API for the Hack Oregon Agriculture git repo
`git clone https://github.com/atifar/or-agriculture.git`

#### Go to http://brew.sh/ and install homebrew on your mac
`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

#### Install Postgres using brew:
`brew install postgresql`

#### Start Postgres
`postgres -D /usr/local/var/postgres &`

#### Create a logical database for your data to go in
`createdb agtech`

#### Create role in database, if it doesn't already exist

`psql`

`CREATE USER alex with CREATEUSER;`

`ALTER USER alex PASSWORD 'mysecretpassword';`

`CREATE database alex;`

`\q`

#### Load in the local database file
`psql -d agtech -f /path/to/local-database-file.sql`

#### Check if python3 is installed
`which python3`

If there's no output from this command, perform the next step, otherwise skip it.

#### Install Python3 (includes pip for managing Python packages)
`brew install python3`

#### Install virtualenv so that you can sandbox your Python modules
`sudo pip install virtualenv`

#### Create a virtualenv somewhere convenient
`virtualenv --python=python3 ~/virtualenv`

#### Activate your virtualenv
`source ~/virtualenv/bin/activate`

#### Install the Django project dependencies
`pip install -r /path/to/my/git/directory/or-agriculture/requirements.txt`

#### Create the local_settings.py file to use your local postgres database instance

*Note that the database settings shown here are used only in development.* Use your favorite text editor to create the following project file and save the code snippet below into it:

`or-agriculture/cropcompass/cropcompass/local_settings.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'agtech',
        'USER': 'alex',
        'PASSWORD': 'mysecretpassword',
        'HOST': '',
        'PORT': ''
    }
}
```

#### Create and apply initial database migrations
`cd or-agriculture/cropcompass`
`./manage.py makemigrations`
`./manage.py migrate`

#### Run the Django development server
`./manage.py runserver`

#### Navigate to http://127.0.0.1:8000/ on your browser to get the API root!
