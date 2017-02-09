# the-last-thousand

*Version: 1.0*

## How to get started on your local development environment.
#### Prerequisites:

* git
* python 2.7.x
* virtualenv

### Create project directory and environment

* `mkdir the-last-thousand && cd the-last-thousand`
* `virtualenv env`
* `source env/scripts/activate` *Activate the environment (each time you start a session working with the code)*

*Obtain source code and clone into crawler directory*
* `git clone https://github.com/lestrato/the-last-thousand.git twitter`
* `cd twitter`

*Your Directory structure will look like this:*
```
the-last-thousand
├── twitter
│   ├── mainsite
│   ├── static
│   ├── twitter
├── env
```

### Install requirements
*from within the-front-page/crawler directory*
* `pip install -r requirements.txt`

### Configure OAuth (Twitter's Authentication)
* `cp mainsite/credentials.py.example mainsite/credentials.py`
* add the correct missing values to mainsite/credentials.py

*for help on OAuth see https://dev.twitter.com/oauth/application-only*

### Run a server locally for development
* `./manage.py runserver`
* Navigate to http://localhost:8000/
