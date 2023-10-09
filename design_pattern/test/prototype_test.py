from ..prototype_with_registory_design.CarGameObject import CarGameObject as c
# import design_pattern.prototype_with_registory_design.TreeGameObject
import pytest

@pytest.fixture
def car_object():
    car_game_object = c(12, 23, [1, 2, 3], "car_shape")
    car_game_object.create_car()
    car_game_object.position_object()
    return car_game_object

def test_prototype_object_creation(car_object):
    assert car_object.pixels == [1, 2, 3]
    
def test_clonable_car(car_object):
    car_object1 = car_object.clone()
    car_object2 = car_object.clone()
    assert car_object1 != car_object2
    assert car_object != car_object1
    assert car_object != car_object2
    