from typing import List
from log import log_debug


class Orders:
    def __init__(self, requests: List[int], n_max: int) -> None:
        self.requests = requests
        self.n_max = n_max

    def check_input_combine_orders(func):
        '''validation decorator'''
        def check(self):
            if not isinstance(self.n_max, int):
                raise ValueError('The variable \'n_max\' have to be integer positive.')

            if not self.requests or not isinstance(self.requests, list):
                raise ValueError('The variable \'requests\' have to be a list of positive integer(s).')

            x = [x for x in self.requests if type(x) != int or x > self.n_max or x <= 0]
            if x:
                raise ValueError('Only positive integers less than or equal '
                f'to \'n_max\' are allowed in the request list. Not accepted: {x}')

            return func(self)
        return check

    @check_input_combine_orders
    def combine_orders(self) -> int:
        sorted_list = sorted(self.requests, reverse=True)
        trips_list = []
        k = len(sorted_list)

        while k != 0:
            highest_value, lower_value = sorted_list[0], sorted_list[-1]
            if sum((highest_value, lower_value)) <= self.n_max:

                if len(sorted_list) == 1:
                    sorted_list.pop(0)
                    trips_list.append((highest_value,))
                else:
                    sorted_list.pop(0), sorted_list.pop()
                    trips_list.append((highest_value, lower_value))

                k = len(sorted_list)

            else:
                sorted_list.pop(0)
                trips_list.append((highest_value,))
                k = len(sorted_list)
        
            log_debug(f'trips_list: {trips_list}')

        number_trips = len(trips_list)
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

how_many = Orders(orders, n_max).combine_orders()
print(f'how_many: {how_many}')

# expected_orders = 2
# assert how_many == expected_orders
