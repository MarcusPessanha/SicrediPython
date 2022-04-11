import click
import re


class InputValidator():

    @staticmethod
    def validator_combine_orders(n_max, orders):
        """
        Checks if the input arguments of the \'combine-orders\' command are valid.
        """
        # Validando n_max
        if not isinstance(n_max, int) or n_max <= 0:
                raise click.BadParameter(n_max)
        
        #Validando orders
        if not isinstance(orders, list) and not isinstance(orders, tuple):
                raise click.BadParameter(f'{orders} is not a valid list of positive integer(s).')

        x = [x for x in orders if x <=0]
        if x:
            raise click.BadParameter(f'{orders} is not a valid list of positive integer(s).')

        if isinstance(orders, tuple):
            orders = [int(x) for x in orders]   

        return n_max, orders

    @staticmethod
    def validator_n_open_contracts(top_n, open_contracts, renegotiated_contracts):
        """
        Checks if the input arguments of the \'n-open-contracts\' command are valid.
        """

        # Validando top_n
        if not isinstance(top_n, int):
                raise click.BadParameter(top_n)
        
        # Validando open_contracts
        if not isinstance(open_contracts, list) and not isinstance(open_contracts, tuple):
            raise click.BadParameter(f'{renegotiated_contracts} is not a valid list.')
        
        x = [x for x in open_contracts if type(x) != list and type(x) != tuple]
        if x:
            raise click.BadParameter(f'{x} is not a valid parameter.')

        x = [x for x in open_contracts if len(x) != 2]
        if x:
            raise click.BadParameter(f'{x} is not a valid parameter. {x} must contain 2 non-null elements.')

        regex = "^\S+[a-z0-9]*$"
        x = [x for x in open_contracts if not re.match(regex, str(x[0])) or not isinstance(x[1], (int, float))]
        if x:
            raise click.BadParameter(f'{x} is not a valid parameter. {x} must be like (alphanumeric, int or float)')

        # Validando renegotiated_contracts
        if not isinstance(renegotiated_contracts, list) and not isinstance(renegotiated_contracts, tuple):
            raise click.BadParameter(f'{renegotiated_contracts} is not a valid list of integer(s)')
        
        x = [x for x in renegotiated_contracts if type(x) != int]
        if x:
            raise click.BadParameter(f'{x} is not a valid integer.')
        

        return top_n, open_contracts, renegotiated_contracts
