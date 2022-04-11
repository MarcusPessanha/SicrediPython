import click
from ..questions.question2_solution2 import Orders
from .utils.ast_literal_option import PythonLiteralOption
from .utils.input_validator import InputValidator

@click.command()
@click.argument('n_max', default=100)
@click.option('--orders','-o', cls=PythonLiteralOption, metavar='<List[int] or Tuple[int]> with no empty characters')
def cli_combine_orders(n_max, orders):
    
    """
    Returns the minimum amount of trips to fulfill all <orders>.\n
    <n_max> an integer containing the maximum value that can be taken in a single trip.\n
    <orders> list of monetary values for each order.\n
        Example: --orders [70, 30, 10]\n
    Command Example:\n 
        python main.py combine-orders 100 --orders [70,30,10]
    """

    n_max, orders = InputValidator().validator_combine_orders(n_max, orders)

    print('Combining Orders')
    how_many = Orders(orders, n_max).combine_orders()
    # how_many = Orders.combine_orders(orders, n_max)
    print(f'Minimum amount of trips:{how_many}')

    return how_many
