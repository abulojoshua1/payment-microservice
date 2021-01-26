# payment-microservice
[![Build Status](https://travis-ci.com/abulojoshua1/payment-microservice.svg?branch=main)](https://travis-ci.com/abulojoshua1/payment-microservice)

[![Coverage Status](https://coveralls.io/repos/github/abulojoshua1/payment-microservice/badge.svg?branch=main)](https://coveralls.io/github/abulojoshua1/payment-microservice?branch=main)

## Project Requirements
The applications below are required for proper setup of the project. Make sure thay are installed before proceeding with project setup
- [GIT](https://git-scm.com/)
- [PYTHON 3.9.X](https://www.python.org/)
- [VIRTUALENV](https://virtualenv.pypa.io/en/latest/installation.html)

## Project Setup
* Clone the repo using [GIT](https://git-scm.com/) by running
```
   $ git clone https://github.com/abulojoshua1/payment-microservice
```

* Navigate to the payment-microservice directory using the command below
```
   $ cd payment-microservice
```

* Create a virtual environment by running
```
   $ virtualenv venv
```

* Activate you virtual environment by running
```
    $ venv\Scripts\activate
```

* Install all project dependencies by running 
```
    $ pip install -r requirements.txt
```

* Create a file named settings.json and copy the content of `/example.settings.json` into it at the project root directory
* You can also use the `APPLICATION_SETTINGS` environment variable to specify the path to the a settings JSON file

## Project Utility Commands
* Run the development server
```
    $ inv run-dev
```

* Run the production server
```
    $ inv run-prod
```

* [Isort](https://pypi.org/project/isort/) python imports
```
    $ inv isort
```

* Check for [linting](https://flake8.pycqa.org/en/latest/)/[Isort](https://pypi.org/project/isort/) errors
```
    $ inv lint
```

* Run unit tests
```
    $ inv test
```
