import pytest
from exceptions.exceptions import ValidationError
from entities.equipment import (
    SoccerBall,
    TennisRacket,
    Bicycle,
    SportsEquipmentFactory
)


class TestEntities:

    # Bicycle

    def test_bicycle_creation_success(self):
        data = {
            "equipment_type": "bicycle",
            "manufacturer": "Россия",
            "price": 18000,
            "type": "горный",
            "number_of_speeds": 21
        }
        bicycle = Bicycle.from_dict(data)
        assert isinstance(bicycle, Bicycle)
        assert bicycle.to_dict() == data


    @pytest.mark.parametrize("data", [
        ({
            "equipment_type": "bicycle",
            "manufacturer": "Россия",
            "price": -50000,
            "type": "горный",
            "number_of_speeds": 21
        }),
        ({
            "equipment_type": "bicycle",
            "manufacturer": "Россия",
            "price": -50000,
            "type": "горный",
            "number_of_speeds": -7
        }),
        ({
            "equipment_type": "bicycle",
            "manufacturer": "Россия",
            "price": -50000
        }),
    ])
    def test_bicycle_creation_invalid(self, data):
        with pytest.raises(ValidationError):
            Bicycle.from_dict(data)
        

    # Soccer ball

    def test_soccer_ball_creation_success(self):
        data = {
            "equipment_type": "soccerBall",
            "manufacturer": "Россия",
            "price": 10000,
            "size": 5,
            "material": "полиуретан, резина"
        }
        soccer_ball = SoccerBall.from_dict(data)
        assert isinstance(soccer_ball, SoccerBall)
        assert soccer_ball.to_dict() == data


    @pytest.mark.parametrize("data", [
        ({
            "equipment_type": "soccerBall",
            "manufacturer": "Россия",
            "price": "123",
            "size": 100,
            "material": "полиуретан, резина"
        }),
        ({
            "equipment_type": "soccerBall",
            "manufacturer": "Россия",
            "price": 10000,
            "size": -100,
            "material": "полиуретан, резина"
        }),
        ({
            "equipment_type": "soccerBall",
            "manufacturer": "Россия",
            "price": 10000,
            "material": "полиуретан, резина"
        }),
    ])    
    def test_soccer_ball_creation_invalid(self, data):
        with pytest.raises(ValidationError):
            SoccerBall.from_dict(data)


    # Tennis racket

    def test_tennis_racket_creation_success(self):
        data = {
            "equipment_type": "tennisRacket",
            "manufacturer": "США",
            "price": 25000,
            "weight": 0.5,
            "head_size": 95
        }
        racket = TennisRacket.from_dict(data)
        assert isinstance(racket, TennisRacket)
        assert racket.to_dict() == data


    @pytest.mark.parametrize("data", [
        ({
            "equipment_type": "tennisRacket",
            "manufacturer": "США",
            "price": 25000,
            "weight": -10,
            "head_size": 95
        }),
        ({
            "equipment_type": "tennisRacket",
            "manufacturer": "США",
            "price": -25000,
            "weight": 0.5,
            "head_size": 95
        }),
        ({
            "equipment_type": "tennisRacket",
            "manufacturer": "США",
            "price": 25000,
            "weight": 0.5,
            "head_size": "qwe"
        }),
    ])    
    def test_tennis_racket_creation_invalid(self, data):
        with pytest.raises(ValidationError):
            TennisRacket.from_dict(data)

    # Factory

    @pytest.mark.parametrize("data, expected_instance", [
        ({
            "equipment_type": "bicycle",
            "manufacturer": "Россия",
            "price": 18000,
            "type": "горный",
            "number_of_speeds": 21
        }, Bicycle),
        ({
            "equipment_type": "soccerBall",
            "manufacturer": "Россия",
            "price": 10000,
            "size": 5,
            "material": "полиуретан, резина"
        }, SoccerBall),
        ({
            "equipment_type": "tennisRacket",
            "manufacturer": "США",
            "price": 25000,
            "weight": 0.5,
            "head_size": 95
        }, TennisRacket),
    ])  
    def test_factory_bicycle_creation(self, data, expected_instance):
        obj = SportsEquipmentFactory.create_from_dict(data)
        assert isinstance(obj, expected_instance)
        assert obj.to_dict() == data


    def test_factory_invalid_type(self):
        data = {
            "equipment_type": "invalid_type",
            "manufacturer": "Россия",
            "price": 25000,
            "weight": 0.5,
            "head_size": 95
        }
        with pytest.raises(ValidationError, match=r"Поле 'equipment_type' может принимать значения"):
            SportsEquipmentFactory.create_from_dict(data)

