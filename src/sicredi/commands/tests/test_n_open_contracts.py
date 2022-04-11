import pytest
from click.testing import CliRunner
from main import cli


class TestnOpenContracts():

    def test_command_should_return_exampled_asserted_value_sucess(self):
        runner = CliRunner() 
        top_n, open_contracts, renegotiated_contracts = 3, [[1,1],[2,2],[3,3],[4,4],[5,5]], [3]
        expected_return = [5, 4, 2]
        # ALL GIVEN

        # WHEN
        commands_parts = ['n-open-contracts', f'{top_n}', '--open_contracts',
                     f'{open_contracts}', '--renegotiated_contracts', f'{renegotiated_contracts}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 0
            assert f'IDs of the {top_n} largest debtors:{expected_return}' in result.output

    def test_command_should_return_asserted_value_sucess(self):
        runner = CliRunner() 
        top_n, open_contracts, renegotiated_contracts = 3, [[1,100],[2,200],[3,400],[4,300],['a',500],['z',1000]], [3,4]
        expected_return = ['z', 'a', 2]
        # ALL GIVEN

        # WHEN
        commands_parts = ['n-open-contracts', f'{top_n}', '--open_contracts',
                     f'{open_contracts}', '--renegotiated_contracts', f'{renegotiated_contracts}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 0
            assert f'IDs of the {top_n} largest debtors:{expected_return}' in result.output

    def test_command_should_return_error_with_negative_topn_value_fail(self):
        runner = CliRunner() 
        top_n, open_contracts, renegotiated_contracts = -3, [[1,1],[2,2],[3,3],[4,4],[5,5]], [3]
        expected_return = 'Error: No such option'
        # ALL GIVEN

        # WHEN
        commands_parts = ['n-open-contracts', f'{top_n}', '--open_contracts',
                     f'{open_contracts}', '--renegotiated_contracts', f'{renegotiated_contracts}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 2
            assert expected_return in result.output

    def test_command_should_return_error_with_float_topn_value_fail(self):
        runner = CliRunner() 
        top_n, open_contracts, renegotiated_contracts = 3.0, [[1,1],[2,2],[3,3],[4,4],[5,5]], [3]
        expected_return = 'Error: Invalid value'
        # ALL GIVEN

        # WHEN
        commands_parts = ['n-open-contracts', f'{top_n}', '--open_contracts',
                     f'{open_contracts}', '--renegotiated_contracts', f'{renegotiated_contracts}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 2
            assert expected_return in result.output
            assert 'is not a valid integer' in result.output

    def test_command_should_return_error_with_1element_tuple_contractID_value_fail(self):
        runner = CliRunner() 
        top_n, open_contracts, renegotiated_contracts = 3.0, [[1,1],[2,2],[3,3],[4,4],(5,)], [3]
        expected_return = 'Error: Invalid value'
        # ALL GIVEN

        # WHEN
        commands_parts = ['n-open-contracts', f'{top_n}', '--open_contracts',
                     f'{open_contracts}', '--renegotiated_contracts', f'{renegotiated_contracts}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 2
            assert expected_return in result.output
            assert 'is not a valid integer' in result.output

    def test_command_should_return_error_with_negative_open_contractID_value_fail(self):
        runner = CliRunner() 
        top_n, open_contracts, renegotiated_contracts = 3.0, [[-1,1],[2,2],[3,3],[4,4],[5,5]], [3]
        expected_return = 'Error: Invalid value'
        # ALL GIVEN

        # WHEN
        commands_parts = ['n-open-contracts', f'{top_n}', '--open_contracts',
                     f'{open_contracts}', '--renegotiated_contracts', f'{renegotiated_contracts}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 2
            assert expected_return in result.output
            assert 'is not a valid integer' in result.output

    def test_command_should_return_error_with_float_open_contractID_value_fail(self):
        runner = CliRunner() 
        top_n, open_contracts, renegotiated_contracts = 3.0, [[1.0,1],[2,2],[3,3],[4,4],[5,5]], [3]
        expected_return = 'Error: Invalid value'
        # ALL GIVEN

        # WHEN
        commands_parts = ['n-open-contracts', f'{top_n}', '--open_contracts',
                     f'{open_contracts}', '--renegotiated_contracts', f'{renegotiated_contracts}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 2
            assert expected_return in result.output
            assert 'is not a valid integer' in result.output

    def test_command_should_return_error_with_empty_open_contractID_value_fail(self):
        runner = CliRunner() 
        top_n, open_contracts, renegotiated_contracts = 3.0, [['',1],[2,2],[3,3],[4,4],[5,5]], [3]
        expected_return = 'Error: Invalid value'
        # ALL GIVEN

        # WHEN
        commands_parts = ['n-open-contracts', f'{top_n}', '--open_contracts',
                     f'{open_contracts}', '--renegotiated_contracts', f'{renegotiated_contracts}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 2
            assert expected_return in result.output
            assert 'is not a valid integer' in result.output

    def test_command_should_return_error_with_negative_open_contractDebt_value_fail(self):
        runner = CliRunner() 
        top_n, open_contracts, renegotiated_contracts = 3.0, [[1,-1],[2,2],[3,3],[4,4],[5,5]], [3]
        expected_return = 'Error: Invalid value'
        # ALL GIVEN

        # WHEN
        commands_parts = ['n-open-contracts', f'{top_n}', '--open_contracts',
                     f'{open_contracts}', '--renegotiated_contracts', f'{renegotiated_contracts}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 2
            assert expected_return in result.output
            assert 'is not a valid integer' in result.output

    def test_command_should_return_error_with_str_open_contractDebt_value_fail(self):
        runner = CliRunner() 
        top_n, open_contracts, renegotiated_contracts = 3.0, [[1,'a'],[2,2],[3,3],[4,4],[5,5]], [3]
        expected_return = 'Error: Invalid value'
        # ALL GIVEN

        # WHEN
        commands_parts = ['n-open-contracts', f'{top_n}', '--open_contracts',
                     f'{open_contracts}', '--renegotiated_contracts', f'{renegotiated_contracts}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 2
            assert expected_return in result.output
            assert 'is not a valid integer' in result.output

    def test_command_should_return_error_with_empty_open_contractDebt_value_fail(self):
        runner = CliRunner() 
        top_n, open_contracts, renegotiated_contracts = 3.0, [[1,],[2,2],[3,3],[4,4],[5,5]], [3]
        expected_return = 'Error: Invalid value'
        # ALL GIVEN

        # WHEN
        commands_parts = ['n-open-contracts', f'{top_n}', '--open_contracts',
                     f'{open_contracts}', '--renegotiated_contracts', f'{renegotiated_contracts}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 2
            assert expected_return in result.output
            assert 'is not a valid integer' in result.output

    def test_command_should_return_error_with_empty_renegotiated_contracts__value_fail(self):
        runner = CliRunner() 
        top_n, open_contracts, renegotiated_contracts = 3.0, [[1,],[2,2],[3,3],[4,4],[5,5]], []
        expected_return = 'Error: Invalid value'
        # ALL GIVEN

        # WHEN
        commands_parts = ['n-open-contracts', f'{top_n}', '--open_contracts',
                     f'{open_contracts}', '--renegotiated_contracts', f'{renegotiated_contracts}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 2
            assert expected_return in result.output
            assert 'is not a valid integer' in result.output

    def test_command_should_return_error_with_negative_renegotiated_contracts__value_fail(self):
        runner = CliRunner() 
        top_n, open_contracts, renegotiated_contracts = 3.0, [[1,],[2,2],[3,3],[4,4],[5,5]], []
        expected_return = 'Error: Invalid value'
        # ALL GIVEN

        # WHEN
        commands_parts = ['n-open-contracts', f'{top_n}', '--open_contracts',
                     f'{open_contracts}', '--renegotiated_contracts', f'{renegotiated_contracts}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 2
            assert expected_return in result.output
            assert 'is not a valid integer' in result.output

    def test_command_should_return_error_with_float_renegotiated_contracts__value_fail(self):
        runner = CliRunner() 
        top_n, open_contracts, renegotiated_contracts = 3.0, [[1,],[2,2],[3,3],[4,4],[5,5]], [3.0]
        expected_return = 'Error: Invalid value'
        # ALL GIVEN

        # WHEN
        commands_parts = ['n-open-contracts', f'{top_n}', '--open_contracts',
                     f'{open_contracts}', '--renegotiated_contracts', f'{renegotiated_contracts}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 2
            assert expected_return in result.output
            assert 'is not a valid integer' in result.output

    def test_command_should_return_error_with_1element_tuple_renegotiated_contracts__value_fail(self):
        runner = CliRunner() 
        top_n, open_contracts, renegotiated_contracts = 3.0, [[1,],[2,2],[3,3],[4,4],[5,5]], (3,)
        expected_return = 'Error: Invalid value'
        # ALL GIVEN

        # WHEN
        commands_parts = ['n-open-contracts', f'{top_n}', '--open_contracts',
                     f'{open_contracts}', '--renegotiated_contracts', f'{renegotiated_contracts}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 2
            assert expected_return in result.output
            assert 'is not a valid integer' in result.output
