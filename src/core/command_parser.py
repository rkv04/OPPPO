from json import loads as json_loads, JSONDecodeError


class CommandParser:
    def __init__(self):
        pass

    def parse_command_line(self, line: str):
        line = line.strip()
        command_parts = line.split(' ', maxsplit=1)
        command_mnemonic = command_parts[0]
        if len(command_parts) == 1:
            return command_mnemonic, {}
        try:
            data = json_loads(command_parts[1])
            return command_mnemonic, data
        except JSONDecodeError as e:
            raise ValueError ("Ошибка в структуре JSON объекта") from e