# payment-microservice

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

## Project Utility Commands
* Run the development server
```
    $ inv run-dev
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
