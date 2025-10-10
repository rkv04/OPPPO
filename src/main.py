from implementations.memory_storage import SportsEquipmentStorage
from implementations.console_output import ConsoleOutput
from core.command_executor import CommandExecutor
import sys


def main():
    equipment_storage = SportsEquipmentStorage()
    console_output = ConsoleOutput()
    command_executor = CommandExecutor(equipment_storage, console_output)
    try:
        command_executor.execute('../tests/data/sports_equipment.txt')
    except Exception as e:
        print(f"Критическая ошибка приложения: {e}")
        sys.exit(1);


if __name__ == '__main__':
    main()

