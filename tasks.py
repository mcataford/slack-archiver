from invoke import task


@task
def format(ctx):
    ctx.run("black . --exclude \(__pycache__\|venv\)")


@task
def lint(ctx):
    ctx.run("black . --exclude \(__pycache__\|venv\) --check")


@task
def test(ctx):
    ctx.run("pytest")
