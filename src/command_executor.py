import json
from interfaces import StorageInterface, OutputInterface
from entities import SportsEquipmentFactory


class CommandExecutor:
    def __init__(self, storage: StorageInterface, out: OutputInterface):
        self.__storage = storage
        self.__out = out

    def execute(self, path_to_command_file: str):
        try:
            with open(path_to_command_file, 'r') as command_file:
                for command_num, command_line in enumerate(command_file, 1):
                    try:
                        command_line = command_line.strip()
                        if not command_line:
                            continue
                        self.__parse_and_execute_command(command_line)

                    except ValueError as e:
                        self.__out.write(f'\nОшибка при выполнении команды в строке {command_num}: {e}\n')

        except FileNotFoundError:
            self.__out.write(f'Файл {path_to_command_file} не найден\n')
        except IOError as e:
            self.__out.write(f'Ошибка чтения файла: {e}')
                
    def __parse_and_execute_command(self, command_line: str):
        command_parts = command_line.split(' ', maxsplit=1)
        command_mnemonic = command_parts[0]
        if len(command_parts) > 1:
            command_data = command_parts[1]
        if command_mnemonic == 'ADD':
            self.__exec_add_command(command_data)
        elif command_mnemonic == "REM":
            self.__exec_rem_command(command_data)
        elif command_mnemonic == 'PRINT':
            self.__exec_print_command()
        else:
            raise ValueError(f'неизвестная команда {command_mnemonic}')
        
    def __str_to_json(self, command_data: str):
        try:
            return json.loads(command_data)
        except json.JSONDecodeError:
            raise ValueError('ошибка в структуре JSON объекта') 
        
    def __exec_add_command(self, command_data: str):
        data = self.__str_to_json(command_data)
        equipment = SportsEquipmentFactory.create_from_dict(data)
        self.__storage.push_back(equipment)

    def __exec_print_command(self):
        sports_equipment = self.__storage.get_all()
        self.__out.write('\n----------\n')
        for i in sports_equipment:
            self.__out.write('\n')
            self.__out.write(i)
            self.__out.write('\n')
        self.__out.write('\n----------\n')

    def __exec_rem_command(self, command_data: str):
        condition = self.__str_to_json(command_data)
        for i in condition:
            if i not in ['attribute', 'operator', 'target_value']:
                raise ValueError(f'неизвестное поле {i}')
        self.__storage.remove_where(condition)


