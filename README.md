# Description

Adverity Python Challenge: Star Wars Explorer app

# Notes

The following is incomplete:

- Load More Button
  - There were some issues getting the "Load More" paginator button working, as it requires AJAX to function properly. Instead, I opted to use Django's default minimalistic paginator, which can still provide the desired functionality.
- Value Count
  - Implementing this feature would require the use of an external library, such as Datatables, which cannot be completed within the given timeframe.

---

# Development

Developed using Python / Django,

---

## Developer Notes

Please always use `pipenv install` instead of `pip3 install` when adding dependencies.

Also ensure to keep the `requirements.txt` up-to-date by running the following command whenever dependencies are added/removed.

```
pipenv requirements > requirements.txt
```

---

## Environment Settings

To ensure maintainability and ease of deployment, settings have been split as follows:

- `dev_settings.py`for Development
- `dev_settings.py` for production

Ensure you are running the application against the desired settings by switching the default environment settings in `manage.py`, `asgi.py`, `wsgi.py`.

Example:

```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '<project name>.settings.dev_settings')
```

- Verify you have `Debug` in `dev_settings.py` set to `True` for Development.
- Confirm you have `Debug` in `dev_settings.py` set to `False` for Production.

Never deploy to Production with `Debug` set to `True`.

---

## Environment & Application setup

Step 1: Download & install Python 3 -

The easiest way to setup a Python Environment on both Windows and macOS is through package managers.

If on Windows, you can use `winget`

Install Python by running the following command

```
winget install python
```

If on macOS, you can use `brew`

To setup homebrew, open the terminal and run the command

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Then install Python by running the following command

```
brew install python
```

Step 2: Install Pipenv

To setup & use isolated Virtual Environments, install pipenv

```
pip3 install pipenv
```

Step 3: Open the terminal & cd into project directory -

```
cd /path/to/project
```

Step 4: Activate/Create Virtual Environment

```
pipenv shell
```

Step 5: Run the following command to install all the dependencies -

```
pipenv install
```

Alternatively, you can run -

```
pip3 install -r requirements.txt
```

Step 6: Done!

Please note that on some devices, one of the dependencies, `psycopg2`, often fails to install. If this occures, download the binary version of the package as follows.

```
pip3 install psycopg2-binary
```

Psycopg2 is an essential package used to connect the application to a Cloud Database.

---

## Run Locally:

Step 1: Open the terminal & cd into project directory -

```
d /path/to/project`
```

Step 2: Run the following command to run the application -

```
python manage.py runserver`
```

Note: You can also run the app using `https` by replacing `runserver` with `runsslserver`

Step 3: Copy the URL that will display in the terminal into your browser

Default URL - http://127.0.0.1:8000/

Done!

Note: You may need to refresh your browser when front-end changes are made, back-end changes don't require re-running the application.

---

## Create Database:

Prerequisite: You must either have a local DB or Cloud DB setup and configured first. The relevent database settings can be found in `settings/dev_settings.py` or `settings/dev_settings.py`.

Database setup for Production must be configured in `settings/dev_settings.py`.
This app uses `boto3`. It can be configured to run any database. (E.g. MySQL, PostgreSQL, MongoDB). All thats needed is the necessary credentials.

Step 1: Open the terminal & cd into project directory -

```
cd /path/to/project
```

Step 2: Run the following command to run the application -

```
python manage.py migrate
```

Done!

Note: Database table, API, and forms are based off the Database model in `<project>/<app>/models.py`.

---

## Create Admin Account:

Step 1: Open the terminal & cd into project directory -

```
cd /path/to/project
```

Step 2: Run the following command to run the application -

```
python manage.py createsuperuser
```

Step 3: Include necessary info -

- Username
- Email
- Password - Note password is invisible when typing
- Password Again - Note password is invisible when typing

Step 4: Navigate to `/admin` & login -

Default URL - http://127.0.0.1:8000/admin

Done!

---

# Deployment

There are two Methods of Deployment, Cloud foundry or OpenShift. Dockerizing is not nessery for deployment on Cloud foundry.

---

## Deployment Notes

#### Set correct URL for Production in settings/dev_settings.py

#### Set correct settings for Production in manage.py

#### NOTE: `name` and `route` in manifest.yml define the app name & URL.

---

## Dockerizing the Application

Prerequisite: Ensure you have Docker installed & running in the background.

Note: Configurations for Docker are located in `Dockerfile` & `docker-compose.yml` file on the root directory

Step 1: Open the terminal & cd into project directory -

```
cd /path/to/project
```

Step 2: Run the following command to build the Docker image -

```
docker build -t <project name> .
```

Step 3: Run the following command to compose cloud Services -

```
docker-compose up
```

Done!

---

## Cloud foundry

Prerequisite: Ensure you have Cloud foundry installed & setup.

Note: Configurations for Cloud foundry Deployment, such as domain, are located in `manifest.yml` file on the root directory.

Step 1: Open the terminal & cd into project directory -

```
cd /path/to/project
```

Step 2: Login to Cloud foundry -

```
cf login --sso
```

Step 3: Follow the link, copy the code, paste it into the terminal & execute

Note: Password will not display when pasted or typed into the terminal, it will be hidden.

Step 4: Deploy to Cloud foundry -

```
cf push
```

Done!

---

## OpenShift

For Instructions to dockerize and deploy the application into OpenShift, please see relevant documentation on redhat.com.
