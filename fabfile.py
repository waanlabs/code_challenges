from fabric import *


@task
def test(ctx, folder_name):
    ctx.run(f'pytest --cov={folder_name} --cov-report=xml')


@task
def coverage(ctx):
    ctx.run('coverage report --show-missing')
