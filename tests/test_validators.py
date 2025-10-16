import pytest
from contextlib import nullcontext as does_not_raise
from utils.validators import Validator
from exceptions.exceptions import ValidationError


class TestValidator:
    @pytest.mark.parametrize("value, expected", [
        (5, True),
        (-5, False),
        (5.55, False),
        ("10", False)
    ])
    def test_validate_positive_integer(self, value, expected):
        assert Validator.validate_positive_integer(value) == expected


    @pytest.mark.parametrize("value, expected", [
        (5.66, True),
        (5, True),
        (-5, False),
        (None, False)
    ])
    def test_validate_non_negative(self, value, expected):
        assert Validator.validate_non_negative(value) == expected


    @pytest.mark.parametrize("data, required_fields, expected_exception", [
        (
            {"field1": "value1", "field2": "value2", "field3": "value3"},
            {"field1", "field2", "field3"},
            does_not_raise()
        ),
        (
            {"field1": "value1", "field2": "value2", "field3": "value3"},
            {"field1", "field2", "field3", "field4"},
            pytest.raises(ValidationError)
        ),
        (
            {"field1": "value1", "field2": "value2", "field3": "value3"},
            {"field1", "field2"},
            pytest.raises(ValidationError)
        )
    ])
    def test_validate_required_fields(self, data, required_fields, expected_exception):
        with expected_exception:
            Validator.validate_required_fields(data, required_fields)


