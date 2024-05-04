import sys
import os
import unittest

# Добавляем корневую директорию App в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    unittest.TextTestRunner().run(test_suite)

