from invoke import run, task


@task(name="run-dev")
def run_dev(context):
    run("python app.py", echo=True, pty=True)


@task(name="test-py")
def test_py(context):
    run("pytest", echo=True, pty=True)


@task(name="lint-py")
def lint_py(context):
    """
    Isort imports and check for linting errors
    """
    run("isort ./src", echo=True, pty=True)
    run("isort ./tests", echo=True, pty=True)
    run("isort ./tasks", echo=True, pty=True)

    run("flake8 ./src", echo=True, pty=True)
    run("flake8 ./tests", echo=True, pty=True)
    run("flake8 ./tasks", echo=True, pty=True)
