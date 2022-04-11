import click
import ast

from src.question2_solution2 import Orders



class PythonLiteralOption(click.Option):

    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except:
            raise click.BadParameter(value)


@click.group()
def cli():
    pass

@click.command()
def initdb():
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')

@click.command()
@click.argument('n_max', default=100)
@click.option('--orders','-o', cls=PythonLiteralOption, metavar='<List[int]>')
def cli_combine_orders(n_max, orders):
    """Returns the minimum amount of trips to fulfill all <orders>. \n
    <n_max> an integer containing the maximum value that can be taken in a single trip.
    """
    print('Combining Orders')

    if not isinstance(n_max, int):
            raise click.BadParameter(n_max)
    if not isinstance(orders, list) and not isinstance(orders, tuple):
            raise click.BadParameter(f'{orders} is not a valid list of integers')

    if isinstance(orders, tuple):
        orders = [int(x) for x in orders]    

    how_many = Orders(orders, n_max).combine_orders()
    print(f'Minimum amount of trips:{how_many}')
    return how_many


cli.add_command(initdb, name='iniciar-db')
cli.add_command(dropdb, name='drop-db')
cli.add_command(cli_combine_orders, name='combine-orders')



if __name__ == '__main__':
    cli()
