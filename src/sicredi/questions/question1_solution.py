import re


class Contract:
    def __init__(self, id, debt):
        self.id = self.validate_id(id)
        self.debt = self.validate_debt(debt)

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)

    def validate_id(self, id):
        id = str(id)
        # Somente caracteres alfanuméricos e sem espaço são aceitos
        regex = "^\S+[a-z0-9]*$"
        if not re.match(regex, id):
            raise ValueError("Not valid id.")

        try:
            id = int(id)
            return id
        except:
            return id

    def validate_debt(self, debt):
        if not isinstance(debt, int) and not isinstance(debt, float) or debt <= 0:
            raise ValueError(f'The variable \'debt\' have to be a positive integer or float.{debt}')
        return debt


class Contracts:
    def get_top_N_open_contracts(open_contracts, renegotiated_contracts, top_n):

        # Retirando contratos já renegociados
        debtor_list = [x for x in open_contracts if x.id not in renegotiated_contracts]
        # debtor_list = list(filter(lambda  x: x.id not in renegotiated_contracts, open_contracts))

        # Ordenando do maior devedor para o menor
        debtor_list.sort(key=lambda x: x.debt, reverse=True)

        # Montando a lista com os ids dos n maiores devedores
        top_N_open_contracts = [x.id for x in debtor_list][:top_n]

        return top_N_open_contracts
