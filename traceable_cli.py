import click
from app import application


@click.group()
def cli():
    pass

@cli.command()
@click.option('--agent', type=click.Choice(['nginx', 'platform'], case_sensitive=False))
def install(agent):
    if(agent == 'nginx'):
        print('Gathering required environment details to install Traceable NGINX plugin') # will replace with nginx_install() from application.py
        application.nginx_install()
    elif(agent == 'platform'):
        print('installing platform agent') # will replace with platform_install() from application.py
    else:
        print('there was an error with CLI tool please reach out to Traceable support')



