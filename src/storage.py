from interfaces import StorageInterface
from entities import SportsEquipment


class SportsEquipmentStorage(StorageInterface):
    def __init__(self):
        self.__equipments = []

    def push_back(self, equipment: SportsEquipment):
        self.__equipments.append(equipment)

    def get_all(self):
        return self.__equipments
    
    def remove_where(self, condition: dict):
        if condition['attribute'] not in ['price', 'manufacturer']:
            raise ValueError(f'поле "attribute" может принимать значения ["price", "manufacturer"]')
        for idx, equipment in enumerate(self.__equipments):
            if (self.__is_condition_true(equipment, condition)):
                self.__equipments.pop(idx)

    def __is_condition_true(self, equipment, condition: dict):
        operator = condition['operator']
        target_value = condition['target_value']
        attribute = condition['attribute']
        equipment_dict = equipment.to_dict()
        if operator == '==':
            return equipment_dict[attribute] == target_value
        elif operator == '>':
            return equipment_dict[attribute] > target_value
        elif operator == '<':
            return equipment_dict[attribute] < target_value
        else:
            raise ValueError(f'неподдерживаемый оператор {operator}')
        
