from storage import SportsEquipmentStorage
from output import ConsoleOutput
from command_executor import CommandExecutor


def main():
    equipment_storage = SportsEquipmentStorage()
    console_output = ConsoleOutput()
    command_executor = CommandExecutor(equipment_storage, console_output)
    command_executor.execute('../tests/data/sports_equipment.txt')


if __name__ == '__main__':
    main()

