from mock import Mock
from nose.tools import raises
from pandora.box import Box
from test.box_factory import BoxFactory

def test_creation():
        box = Box(**BoxFactory.attributes())
	assert box._levels == BoxFactory.attributes()['levels'] 

@raises(Exception)
def test_creation_fails_without_levels():
	params = BoxFactory.attributes()
	params['levels'] = []
        box = Box(**params)

# This is a level index for display purposes, starts from 1 
def test_current_level():
	params = BoxFactory.attributes()
        box = Box(**params)
	assert box.current_level() == 1

def test_message():
	params = BoxFactory.attributes()
        box = Box(**params)
	assert box.message() == params['levels'][0].message

def test_solve_success():
	params = BoxFactory.attributes()
        box = Box(**params)
	box._levels[0].solve = Mock(return_value = True)
	assert box.solve() == True
	assert box.current_level() == 2

def test_solve_failure():
	params = BoxFactory.attributes()
        box = Box(**params)
	box._levels[0].solve = Mock(return_value = False)
	assert box.solve() == False
	assert box.current_level() == 1

def test_hint():
	params = BoxFactory.attributes()
        box = Box(**params)
	assert box.hint() == params['levels'][0].get_hint()

	 
	


