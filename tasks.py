from invoke import task


@task
def format(ctx):
    ctx.run("black . --exclude \(__pycache__\|venv\)")
