from exceptions.exceptions import ValidationError


class Validator:
    @staticmethod
    def validate_positive_integer(value):
        return isinstance(value, int) and value >= 0
    
    @staticmethod
    def validate_non_negative(value):
        return isinstance(value, (int, float)) and value >= 0
    
    @staticmethod
    def validate_required_fields(data: dict, required_fields: set):
        missing = required_fields - set(data.keys())
        extra = set(data.keys()) - required_fields
        if missing:
            raise ValidationError(f"Отсутствуют обязательные поля: {', '.join(missing)}")
        if extra:
            raise ValidationError(f"Лишние поля: {', '.join(extra)}")

    @staticmethod
    def validate_condition(condition: dict, required_fields: list, allowed_operators: list, allowed_attributes: list):
        Validator.validate_required_fields(condition, required_fields)
        if condition["operator"] not in allowed_operators:
            raise ValidationError(f"Поддерживаемые операторы: {allowed_operators}")
        if condition["attribute"] not in allowed_attributes:
            raise ValidationError(f"Поле 'attribute' может принимать значения: {allowed_attributes}")
        
