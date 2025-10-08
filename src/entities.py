

class SportsEquipment:
    def __init__(self, manufacturer: str, price: int):
        self.__validate_data(price)
        self._manufacturer = manufacturer
        self._price = price

    def __validate_data(self, price: int):
        self.__validate_price(price)

    def __validate_price(self, price):
        if isinstance(price, int) and price >= 0:
            return
        raise ValueError('цена должна быть целым неотрицательным числом')

    def to_dict(self):
        pass


class SoccerBall(SportsEquipment):

    NUMBER_OF_FIELDS = 5

    def __init__(self, manufacturer: str, price: int, size: int, material: str):
        super().__init__(manufacturer, price)
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
        try:
            return SoccerBall(
                manufacturer = data['manufacturer'],
                price = data['price'],
                size = data['size'],
                material = data['material']
            )
        except KeyError as e:
            raise ValueError(f"требуется поле {e}")
    
    def to_dict(self):
        return {
            "manufacturer": self._manufacturer,
            "price": self._price,
            "size": self.__size,
            "material": self.__material
        }

    def __validate_data(self, size: int):
        if isinstance(size, int) and size >= 0:
            return
        raise ValueError('размер должен быть целым неотрицательным числом')
        

class TennisRacket(SportsEquipment):

    NUMBER_OF_FIELDS = 5

    def __init__(self, manufacturer: str, price: int, weight: int, head_size: int):
        super().__init__(manufacturer, price)
        self.__validate_data(weight, head_size)
        self.__weight = weight
        self.__head_size = head_size

    @staticmethod
    def from_dict(data: dict):
        if len(data) > TennisRacket.NUMBER_OF_FIELDS:
            raise ValueError(f'слишком много полей у объекта (требуется {Bicycle.NUMBER_OF_FIELDS})')
        try:
            return TennisRacket(
                manufacturer = data['manufacturer'],
                price = data['price'],
                weight = data['weight'],
                head_size = data['head_size']
            )
        except KeyError as e:
            raise ValueError(f"требуется поле {e}")
        
    def to_dict(self):
        return {
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
        if isinstance(weight, float) and weight >= 0:
            return
        raise ValueError('вес должен быть неотрицательным числом')

    def __validate__head_size(self, head_size):
        if isinstance(head_size, int) and head_size >= 0:
            return
        raise ValueError('размер ракетки должен быть целым неотрицательным числом')



class Bicycle(SportsEquipment):

    NUMBER_OF_FIELDS = 5

    def __init__(self, manufacturer: str, price: int, type: str, number_of_speeds: int):
        super().__init__(manufacturer, price)
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
        if len(data) > Bicycle.NUMBER_OF_FIELDS:
            raise ValueError(f'слишком много полей у объекта (требуется {Bicycle.NUMBER_OF_FIELDS})')
        try:
            return Bicycle(
            manufacturer = data['manufacturer'],
            price = data['price'],
            type = data['type'],
            number_of_speeds = data['number_of_speeds']
        )
        except KeyError as e:
            raise ValueError(f"требуется поле '{e}'")
        
    def to_dict(self):
        return {
            "manufacturer": self._manufacturer,
            "price": self._price,
            "type": self.__type,
            "number_of_speeds": self.__number_of_speeds
        }
    
    def __validate_data(self, number_of_speeds):
        self.__validate_number_of_speeds(number_of_speeds)

    def __validate_number_of_speeds(self, number_of_speeds):
        if isinstance(number_of_speeds, int) and number_of_speeds >= 0:
            return
        raise ValueError('число скоростей должно быть целым неотрицательным числом')


class SportsEquipmentFactory:
    @staticmethod
    def create_from_dict(data: dict):
        equipment_type = data.get('equipment_type', None)
        if not equipment_type:
            raise ValueError("поле 'equipment_type' является обязательным для каждого объекта")
        if equipment_type == 'bicycle':
            return Bicycle.from_dict(data)
        elif equipment_type == 'soccerBall':
            return SoccerBall.from_dict(data)
        elif equipment_type == 'tennisRacket':
            return TennisRacket.from_dict(data)
        else:
            raise ValueError(f"поле 'equipment_type' может иметь значения: ['bicycle', 'soccerBall', 'tennisRacket']")
        
