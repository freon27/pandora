import unittest
from mock import Mock
import os
from Pandora.pandora import Task


class TestTask(unittest.TestCase):
    
    def setUp(self):       
        def failing_test():
            return 0
            
        self.failing_test = failing_test
        
    def test_solve_simple_parameter(self):
        
        self.task = Task(
            "Test",
            "hint1",
            self.failing_test
        )
        
        self.task.test_function = Mock(return_value=False)
        result = self.task.test_solve("wrongvalue")
        self.task.test_function.assert_called_with("wrongvalue")
        self.assertEquals(result, False)
    
    
    def test_get_hint(self):
        self.task = Task(
            "Test",
            "hint1",
            self.failing_test
        )
        
        
        