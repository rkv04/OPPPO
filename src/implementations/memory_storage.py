from interfaces.storage import StorageInterface
from entities.equipment import SportsEquipment


class SportsEquipmentStorage(StorageInterface):
    def __init__(self):
        self.__equipments = []
        self.__comparison_functions = {
            "==": lambda a, b: a == b,
            ">": lambda a, b: a > b,
            "<": lambda a, b: a < b
        }

    def push_back(self, equipment: SportsEquipment):
        self.__equipments.append(equipment)

    def get_all(self):
        return self.__equipments
    
    def remove_where(self, condition: dict):
        for idx, equipment in enumerate(self.__equipments):
            if (self.__is_condition_true(equipment, condition)):
                self.__equipments.pop(idx)

    def __is_condition_true(self, equipment, condition: dict):
        operator = condition["operator"]
        target_value = condition["target_value"]
        attribute = condition["attribute"]
        equipment_value = equipment.to_dict()[attribute]
        return self.__comparison_functions[operator](equipment_value, target_value)
        
