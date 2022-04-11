import click
import ast

import settings
from sicredi.commands.combine_orders import cli_combine_orders
from sicredi.commands.n_open_contracts import cli_n_open_contracts


@click.group(context_settings=settings.CONTEXT_SETTINGS)
@click.version_option(version=settings.VERSION)
def cli():
    """
    Teste Sicredi Python.
    """
    pass

@click.command()
def initdb():
    """
    Connect db.
    """
    click.echo('not working yet')

@click.command()
def dropdb():
    """
    Drop db.
    """
    click.echo('not working yet')


cli.add_command(initdb, name='iniciar-db')
cli.add_command(dropdb, name='drop-db')
cli.add_command(cli_combine_orders, name='combine-orders')
cli.add_command(cli_n_open_contracts, name='n-open-contracts')


if __name__ == '__main__':
    cli(prog_name=settings.PROGRAM_NAME)
