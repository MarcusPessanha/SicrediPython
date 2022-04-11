import click
from ..questions.question1_solution import Contracts, Contract
from .utils.ast_literal_option import PythonLiteralOption
from .utils.input_validator import InputValidator


@click.command()
@click.argument('top_n', default=3)
@click.option('--open_contracts','-o', cls=PythonLiteralOption, metavar=('<List[tuples(alphanumeric,int)] '
                'or List[List[alphanumeric,int]]> with no empty characters'))
@click.option('--renegotiated_contracts','-r', cls=PythonLiteralOption, metavar=('<List[int] or Tuple[int]> '
                'with no empty characters'))
def cli_n_open_contracts(top_n, open_contracts, renegotiated_contracts):
    
    """
    Returns the IDs of the <n> largest debtors. \n
    <top_n> an integer containing the required number of debtors.\n
    <open_contracts> monthly list of clients and their debts.\n
    <renegotiated_contracts> list with the id(s) of customers who renegotiated their contract. 
    """

    top_n, open_contracts, renegotiated_contracts = InputValidator.validator_n_open_contracts(top_n, open_contracts, renegotiated_contracts)

    contracts_objects_list = [Contract(x[0], x[1]) for x in open_contracts]
    renegotiated_contracts = list(renegotiated_contracts)

    print(f'Getting top {top_n} debtors')
    actual_open_contracts = Contracts.get_top_N_open_contracts(contracts_objects_list, renegotiated_contracts, top_n)
    print(f'IDs of the {top_n} largest debtors:{actual_open_contracts}')

    return actual_open_contracts
