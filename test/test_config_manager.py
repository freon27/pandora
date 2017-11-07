import unittest
import os
from Pandora.pandora import ConfigManager
from testfixtures import TempDirectory, compare

class TestConfigManager(unittest.TestCase):
    
    def test_read_config(self):
        d = TempDirectory()
        d.write("t1.txt", b'0')
        task_index = ConfigManager.read_config(os.path.join(d.path,"t1.txt"))
        self.assertEqual(task_index, 0)
        d.cleanup()

    def test_write_config(self):
        d = TempDirectory()
        ConfigManager.write_config(os.path.join(d.path,"t1.txt"), 1)
        compare(d.read("t1.txt"), b'1')
        d.cleanup()
        
    def test_initialise_file(self):
        d = TempDirectory()
        task_index = ConfigManager.read_config(os.path.join(d.path,"t1.txt"))
        compare(d.read("t1.txt"), b'0')
        d.cleanup()