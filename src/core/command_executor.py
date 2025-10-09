from interfaces.output import OutputInterface
from interfaces.storage import StorageInterface
from models.equipment import SportsEquipmentFactory
from core.command_parser import CommandParser


class CommandExecutor:
    def __init__(self, storage: StorageInterface, out: OutputInterface):
        self.__storage = storage
        self.__out = out
        self.__command_parser = CommandParser()
        self.__command_handlers = {
            "ADD": self.__exec_add_command,
            "REM": self.__exec_rem_command,
            "PRINT": self.__exec_print_command
        }

    def execute(self, path_to_command_file: str):
        try:
            with open(path_to_command_file, "r", encoding="utf-8") as file:
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    if not line:
                        continue
                    self.__process_line(line, line_num)

        except FileNotFoundError:
            self.__out.write(f"Файл {path_to_command_file} не найден\n")
        except IOError as e:
            self.__out.write(f"Ошибка чтения файла: {e}")
                
    def __process_line(self, command_line: str, line_num: int):
        try:
            mnemonic, data = self.__command_parser.parse_command_line(command_line)
            handler = self.__command_handlers.get(mnemonic)
            if not handler:
                raise ValueError(f'Неизвестная команда {mnemonic}')
            handler(data or {})
        except Exception as e:
            self.__out.write(f"\nОшибка при выполнении команды в строке {line_num}: {e}\n")
        
    def __exec_add_command(self, command_data: str):
        equipment = SportsEquipmentFactory.create_from_dict(command_data)
        self.__storage.push_back(equipment)

    def __exec_print_command(self, command_data):
        sports_equipment = self.__storage.get_all()
        self.__out.write('\n----------\n')
        for i in sports_equipment:
            self.__out.write('\n')
            self.__out.write(i)
            self.__out.write('\n')
        self.__out.write('\n----------\n')

    def __exec_rem_command(self, command_data: str):
        for i in command_data:
            if i not in ['attribute', 'operator', 'target_value']:
                raise ValueError(f'неизвестное поле {i}')
        self.__storage.remove_where(command_data)