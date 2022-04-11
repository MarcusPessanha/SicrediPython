import pytest
from click.testing import CliRunner
from main import cli


class TestCombineOrders():

    def test_command_should_return_exampled_asserted_value_sucess(self):
        runner = CliRunner() 
        n_max, orders = 100, [70,30,10]
        expected_return = 2
        # ALL GIVEN

        # WHEN
        commands_parts = ['combine-orders', f'{n_max}', '--orders', f'{orders}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 0
            assert f'Minimum amount of trips:{expected_return}' in result.output

    def test_command_should_return_asserted_value_sucess(self):
        runner = CliRunner() 
        n_max, orders = 90, [10, 50, 5, 40, 89, 80, 34, 10, 2, 50, 73, 87, 2, 1, 2]
        expected_return = 8
        # ALL GIVEN

        # WHEN
        commands_parts = ['combine-orders', f'{n_max}', '--orders', f'{orders}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 0
            assert f'Minimum amount of trips:{expected_return}' in result.output
    
    def test_command_should_return_error_with_negative_nmax_fail(self):
        runner = CliRunner() 
        n_max, orders = -100, [70,30,10]
        expected_return = 'Error: No such option'
        # ALL GIVEN

        # WHEN
        commands_parts = ['combine-orders', f'{n_max}', '--orders', f'{orders}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 2
            assert expected_return in result.output

    def test_command_should_return_error_with_float_nmax_fail(self):
        runner = CliRunner() 
        n_max, orders = 100.0, [70,30,10]
        expected_return = 'Error: Invalid value'
        # ALL GIVEN

        # WHEN
        commands_parts = ['combine-orders', f'{n_max}', '--orders', f'{orders}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 2
            assert expected_return in result.output
            assert 'is not a valid integer' in result.output

    def test_command_should_return_error_with_negative_order_fail(self):
        runner = CliRunner() 
        n_max, orders = 100, [70,30,-10]
        expected_return = 'Error: Invalid value'
        # ALL GIVEN

        # WHEN
        commands_parts = ['combine-orders', f'{n_max}', '--orders', f'{orders}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 2
            assert expected_return in result.output
            assert f'is not a valid list of positive integer(s)' in result.output

    def test_command_should_return_error_with_value_order_bigger_than_nmax_fail(self):
        runner = CliRunner() 
        n_max, orders = 100, [70,30,110]
        expected_return = 'Combining Orders'
        # ALL GIVEN

        # WHEN
        commands_parts = ['combine-orders', f'{n_max}', '--orders', f'{orders}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 1
            assert expected_return in result.stdout
            # assert f'Only positive integers less than or equal' in result.exception
            # assert f'Not accepted' in result.output

    def test_command_should_return_error_with_string_in_value_order_fail(self):
        runner = CliRunner() 
        n_max, orders = 100, [70,30,'a']
        expected_return = 'Error: Invalid value:'
        # ALL GIVEN

        # WHEN
        commands_parts = ['combine-orders', f'{n_max}', '--orders', f'{orders}']

        with runner.isolated_filesystem():
            result = runner.invoke(cli, commands_parts)
        # THEN    
            assert result.exit_code == 2
            assert expected_return in result.output
            assert f's not a valid list of positive integer(s)' in result.output
            