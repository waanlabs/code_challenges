from fabric2 import task


@task
def format(ctx):
    ctx.run("black .")


@task
def lint(ctx):
    ctx.run("flake8 .")


@task
def pylint(ctx):
    ctx.run("pylint code_challenges")


@task
def test(ctx):
    ctx.run("pytest --cov=code_challenges --cov-report=xml")


@task
def coverage(ctx):
    ctx.run("coverage report --show-missing")
