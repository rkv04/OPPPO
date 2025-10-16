import pytest
from contextlib import nullcontext as does_not_raise
from core.command_parser import CommandParser
from exceptions.exceptions import CommandParseError


class TestCommandParser:

    @pytest.fixture
    def parser(self):
        return CommandParser()
    
    
    @pytest.mark.parametrize("command_line, expected_mnemonic, expected_data", [
        ('ADD {"field1": "value1"}', "ADD", {"field1": "value1"}),
        ('REM {"field1": "value1"}', "REM", {"field1": "value1"}),
        ("PRINT", "PRINT", {})
    ])
    def test_parse_valid_command(self, parser, command_line, expected_mnemonic, expected_data):
        mnemonic, data = parser.parse_command_line(command_line)
        assert mnemonic == expected_mnemonic
        assert data == expected_data

    
    @pytest.mark.parametrize("command_line", [
        ('ADD {field1": "value1"}'),
        ('ADD {"field1" "value1"}'),
        ('ADD {"field1": "value1"'),
        ('ADD ["field1": "value1"]')
    ])
    def test_parse_invalid_json(self, parser, command_line):
        with pytest.raises(CommandParseError):
            parser.parse_command_line(command_line)

    
