from utils.validators import Validator
from exceptions.exceptions import ValidationError


class SportsEquipment():
    def __init__(self, equipment_type: str, manufacturer: str, price: int):
        self.__validate_data(price)
        self._equipment_type = equipment_type
        self._manufacturer = manufacturer
        self._price = price

    def __validate_data(self, price: int):
        self.__validate_price(price)

    def __validate_price(self, price):
        if Validator.validate_positive_integer(price):
            return
        raise ValidationError('Цена должна быть целым неотрицательным числом')

    def to_dict(self):
        pass


class SoccerBall(SportsEquipment):
    def __init__(self, equipment_type: str, manufacturer: str, price: int, size: int, material: str):
        super().__init__(equipment_type, manufacturer, price)
        self.__validate_data(size)
        self.__size = size
        self.__material = material

    def __str__(self):
        return (f"Футбольный мяч\n"
                f"Производитель: {self._manufacturer}\n"
                f"Цена: {self._price} руб.\n"
                f"Размер: {self.__size}\n"
                f"Материал: {self.__material}")

    @staticmethod
    def from_dict(data: dict):
        required = {"equipment_type", "manufacturer", "price", "size", "material"}
        Validator.validate_required_fields(data, required)
        return SoccerBall(
            equipment_type = data["equipment_type"],
            manufacturer = data['manufacturer'],
            price = data['price'],
            size = data['size'],
            material = data['material']
        )
    
    def to_dict(self):
        return {
            "equipment_type": self._equipment_type,
            "manufacturer": self._manufacturer,
            "price": self._price,
            "size": self.__size,
            "material": self.__material
        }

    def __validate_data(self, size: int):
        if Validator.validate_positive_integer(size):
            return
        raise ValidationError('Размер должен быть целым неотрицательным числом')
        

class TennisRacket(SportsEquipment):
    def __init__(self, equipment_type: str, manufacturer: str, price: int, weight: int, head_size: int):
        super().__init__(equipment_type, manufacturer, price)
        self.__validate_data(weight, head_size)
        self.__weight = weight
        self.__head_size = head_size

    @staticmethod
    def from_dict(data: dict):
        required = {"equipment_type", "manufacturer", "price", "weight", "head_size"}
        Validator.validate_required_fields(data, required)
        return TennisRacket(
                equipment_type = data["equipment_type"],
                manufacturer = data['manufacturer'],
                price = data['price'],
                weight = data['weight'],
                head_size = data['head_size']
            )
        
    def to_dict(self):
        return {
            "equipment_type": self._equipment_type,
            "manufacturer": self._manufacturer,
            "price": self._price,
            "weight": self.__weight,
            "head_size": self.__head_size
        }
    
    def __str__(self):
        return (f"Теннисная ракетка\n"
                f"Производитель: {self._manufacturer}\n"
                f"Цена: {self._price} руб.\n"
                f"Вес: {self.__weight} кг.\n"
                f"Размер: {self.__head_size}")
    
    def __validate_data(self, weight, head_size):
        self.__validate__head_size(head_size)
        self.__validate_weight(weight)

    def __validate_weight(self, weight):
        if Validator.validate_non_negative(weight):
            return
        raise ValidationError('Вес должен быть неотрицательным числом')

    def __validate__head_size(self, head_size):
        if Validator.validate_positive_integer(head_size):
            return
        raise ValidationError('Размер ракетки должен быть целым неотрицательным числом')



class Bicycle(SportsEquipment):
    def __init__(self, equipment_type: str, manufacturer: str, price: int, type: str, number_of_speeds: int):
        super().__init__(equipment_type, manufacturer, price)
        self.__validate_data(number_of_speeds)
        self.__type = type
        self.__number_of_speeds = number_of_speeds

    def __str__(self):
        return (f"Велосипед\n"
                f"Производитель: {self._manufacturer}\n"
                f"Цена: {self._price} руб.\n"
                f"Тип: {self.__type}\n"
                f"Число скоростей: {self.__number_of_speeds}")

    @staticmethod
    def from_dict(data: dict):
        required = {"equipment_type", "manufacturer", "price", "type", "number_of_speeds"}
        Validator.validate_required_fields(data, required)
        return Bicycle(
            equipment_type = data["equipment_type"],
            manufacturer = data['manufacturer'],
            price = data['price'],
            type = data['type'],
            number_of_speeds = data['number_of_speeds']
        )
        
    def to_dict(self):
        return {
            "equipment_type": self._equipment_type,
            "manufacturer": self._manufacturer,
            "price": self._price,
            "type": self.__type,
            "number_of_speeds": self.__number_of_speeds
        }
    
    def __validate_data(self, number_of_speeds):
        self.__validate_number_of_speeds(number_of_speeds)

    def __validate_number_of_speeds(self, number_of_speeds):
        if Validator.validate_positive_integer(number_of_speeds):
            return
        raise ValidationError('Число скоростей должно быть целым неотрицательным числом')


class SportsEquipmentFactory:

    __equipment_type_mapping = {
        "bicycle": Bicycle,
        "soccerBall": SoccerBall,
        "tennisRacket": TennisRacket
    }

    @staticmethod
    def create_from_dict(data: dict):
        allowed_equipment_types = ["bicycle", "soccerBall", "tennisRacket"]
        equipment_type = data.get('equipment_type')
        if not equipment_type:
            raise ValidationError("Поле 'equipment_type' является обязательным для каждого объекта")
        cls = SportsEquipmentFactory.__equipment_type_mapping.get(equipment_type)
        if not cls:
            raise ValidationError(f"Поле 'equipment_type' может принимать значения: {allowed_equipment_types}")
        return cls.from_dict(data)
    
    