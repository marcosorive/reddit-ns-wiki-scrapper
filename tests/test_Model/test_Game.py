import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../src')
from Model.Game import Game 


name_data = [
    "Paco----------123128371236",
    "____239479s8asd",
    "     ",
]

@pytest.mark.parametrize("name", name_data)
def test_Game(name):
    print(sys.path)
    game = Game(name)
    assert game.name == name