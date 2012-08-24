from mock import Mock
from nose.tools import raises
from pandora.box import Level
from test.box_factory import LevelFactory

def test_message():
	params = LevelFactory.attributes() 
        level = Level(**params)
	assert level.message == params['message']

def test_hints():
        level = Level(**LevelFactory.attributes())
	assert level.hints == LevelFactory.attributes()['hints']
	assert level._current_hint == 0 

def test_get_hint():
        level = Level(**LevelFactory.attributes())
	hint_list = LevelFactory.attributes()['hints']
	assert level.get_hint() == hint_list[0]

def test_next_hint():
        level = Level(**LevelFactory.attributes())
	hint_list = LevelFactory.attributes()['hints']
	assert level.next_hint() == hint_list[1]
	assert level.next_hint() == hint_list[2]
	# This should still be the third hint as it is the last one
	assert level.next_hint() == hint_list[2]

@raises(NotImplementedError)
def test_solve_fails_if_called():
        level = Level(**LevelFactory.attributes())
	level.solve()

