from typing import List
from log import log_debug


class Orders:
    @staticmethod
    def check_input_combine_orders(requests: List[int], n_max: int) -> None:
        if not isinstance(n_max, int):
            raise ValueError('The variable \'n_max\' have to be integer positive.')

        if not requests or not isinstance(requests, list):
            raise ValueError('The variable \'requests\' have to be a list of positive integer(s).')

        x = [x for x in requests if type(x) != int or x > n_max or x <= 0]
        if x:
            raise ValueError('Only positive integers less than or equal '
            f'to \'n_max\' are allowed in the request list. Not accepted: {x}')

    @staticmethod
    def combine_orders(requests: List[int], n_max: int) -> int:        
        Orders.check_input_combine_orders(requests, n_max)

        log_debug(f'requests: {requests}'), log_debug(f'n_max: {n_max}')

        sorted_list = sorted(requests, reverse=True)
        log_debug(f'sorted_list: {sorted_list}')

        trips_list = []
        k = len(sorted_list)
        log_debug(f'k: {k}')

        while k != 0:
            highest_value, lower_value = sorted_list[0], sorted_list[-1]
            if sum((highest_value, lower_value)) <= n_max:
                log_debug(f'highest_value: {highest_value}, lower_value: {lower_value} SOMA É MENOR que n_max')

                if len(sorted_list) == 1:
                    sorted_list.pop(0)
                    trips_list.append((highest_value,))
                else:
                    sorted_list.pop(0), sorted_list.pop()
                    trips_list.append((highest_value, lower_value))

                log_debug(sorted_list)
                k = len(sorted_list)
                log_debug(f'k: {k}')

            else:
                log_debug(f'highest_value: {highest_value}, lower_value: {lower_value} SOMA É MAIOR QUE n_max')
                sorted_list.pop(0)
                log_debug(sorted_list)
                trips_list.append((highest_value,))

                k = len(sorted_list)
                log_debug(f'k: {k}')
            
            log_debug(f'trips_list: {trips_list}')

        number_trips = len(trips_list)
        log_debug(f'number_trips: {number_trips}')
        return number_trips



'''Testes'''

n_max = 100
orders = [70, 30, 10]
# orders = ['met', 30, 10]
# orders = [70, 30, 10]
# orders = [10, 50, 5, 40, 100, 80, 34, 10, 2, 50, 73, 87, 2, 1, 2]
# orders = [10, 50, 5, 40, 100, 80, 34, 10, 2, 50, 73, 87, 2, 1, -2]
# orders = [10, 50, 5, 40]
# orders = []
# orders = '1'
# orders = [70, 30, 10.0]
# orders = [70, 30, 10, 110]
# orders = [70, 30, 10, 0]

# import random 
# orders = [random.randint(1, 100) for i in range(500)]
n_max = 100
expected_orders = 2

how_many = Orders().combine_orders(orders, n_max)
print(f'how_many: {how_many}')
# assert how_many == expected_orders


# TODO - testes 
# TODO - comentar o código
# TODO - fazer documentação explicando as soluções
# TODO - decorator para registrar performance em diferentes cenários 
# TODO - organizar
