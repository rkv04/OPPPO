

class Validator:
    @staticmethod
    def validate_positive_integer(value):
        return isinstance(value, int) and value >= 0
    
    @staticmethod
    def validate_required_fields(data: dict, required_fields: list):
        missing = [field for field in required_fields if field not in data]
        if missing:
            raise ValueError(f'Отсутствуют обязательные поля: {missing}')