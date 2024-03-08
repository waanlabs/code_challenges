from fabric2 import task


@task
def autoflake(ctx):
    ctx.run(
        "autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place code_challenges"
    )


@task
def isort(ctx):
    ctx.run("isort code_challenges")


@task
def black(ctx):
    ctx.run("black .")


@task
def flake(ctx):
    ctx.run("flake8 .")


@task
def pylint(ctx):
    ctx.run("pylint code_challenges")


@task
def mypy(ctx):
    ctx.run("mypy code_challenges")


@task
def bandit(ctx):
    ctx.run("bandit -r code_challenges")


@task
def pytest(ctx):
    ctx.run("pytest --cov=code_challenges --cov-report=xml")


@task
def coverage(ctx):
    ctx.run("coverage report --show-missing")


@task
def check(ctx):
    autoflake(ctx)
    isort(ctx)
    black(ctx)
    flake(ctx)
    pylint(ctx)
    mypy(ctx)
    bandit(ctx)
    pytest(ctx)
    coverage(ctx)
