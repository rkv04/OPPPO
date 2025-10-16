import pytest
from core.command_executor import CommandExecutor
from implementations.memory_storage import SportsEquipmentStorage


class MockOutput:
    def __init__(self):
        self.messages = []

    def write(self, message: str):
        self.messages.append(message)


class TestCommandExecutor:

    def test_execute_line_with_unknown_command(self):
        storage = SportsEquipmentStorage()
        output = MockOutput()
        executor = CommandExecutor(storage, output)
        executor.execute_line('UNKNOWN {"field1": "value1"}', 1)
        msg = output.messages[-1]
        assert "Неизвестная команда" in msg

