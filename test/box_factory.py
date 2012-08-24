import factory
from pandora.box import Level
from pandora.box import Box

class LevelFactory(factory.Factory):
	FACTORY_FOR = Level
	message = factory.Sequence(lambda n: 'This is level {0}'.format(n))
	hints = ['Why not try reading a book', 'This is the book you should read', 'Follow this link then']
	
class BoxFactory(factory.Factory):
	FACTORY_FOR = Box
	levels = [LevelFactory.build(), LevelFactory.build(), LevelFactory.build()]
	
