from invoke import run, task


@task(name="run-dev")
def run_dev(context):
    run("python app.py", echo=True, pty=True)


@task(name="run-prod")
def run_prod(context):
    run("gunicorn -c gunicorn_config.py app:app", echo=True, pty=True)


@task(name="test")
def test_py(context):
    run("pytest --cov=src", echo=True, pty=True)


@task(name="isort")
def isort(context):
    run("isort ./src", echo=True, pty=True)
    run("isort ./tests", echo=True, pty=True)
    run("isort ./tasks", echo=True, pty=True)


@task(name="lint")
def lint_py(context):
    """
    Isort imports and check for linting errors
    """
    run("isort --check-only ./src", echo=True, pty=True)
    run("isort --check-only ./tests", echo=True, pty=True)
    run("isort --check-only ./tasks", echo=True, pty=True)

    run("flake8 ./src", echo=True, pty=True)
    run("flake8 ./tests", echo=True, pty=True)
    run("flake8 ./tasks", echo=True, pty=True)
