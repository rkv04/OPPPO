from interfaces.output import OutputInterface
from interfaces.storage import StorageInterface
from entities.equipment import SportsEquipmentFactory
from core.command_parser import CommandParser
from utils.validators import Validator
from exceptions.exceptions import UnknownCommandError, ValidationError, CommandParseError


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
                raise UnknownCommandError(f'Неизвестная команда {mnemonic}')
            handler(data)

        except UnknownCommandError as e:
           self.__out.write(f"\nОшибка команды в строке {line_num}: {e}\n")
        except ValidationError as e:
            self.__out.write(f"\nОшибка валидации данных в строке {line_num}: {e}\n")
        except CommandParseError as e:
            self.__out.write(f"\nОшибка парсинга команды в строке {line_num}: {e}\n")
          
    def __exec_add_command(self, command_data: dict):
        equipment = SportsEquipmentFactory.create_from_dict(command_data)
        self.__storage.push_back(equipment)

    def __exec_rem_command(self, command_data: dict):
        required_fields = {'attribute', 'operator', 'target_value'}
        allowed_attributes = ['price', 'manufacturer']
        allowed_operators = ["==", ">", "<"]
        Validator.validate_condition(command_data, required_fields, allowed_operators, allowed_attributes)
        self.__storage.remove_where(command_data)

    def __exec_print_command(self, command_data: dict):
        sports_equipment = self.__storage.get_all()
        self.__out.write("\n")
        for i in sports_equipment:
            self.__out.write('\n')
            self.__out.write(i)
            self.__out.write('\n')
        self.__out.write("\n")

