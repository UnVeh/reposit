# Тест №2.2 отсутствие_первого_клика(негативный)
import unittest
from unittest.mock import Mock, patch
import os

class TestNoFirstClick(unittest.TestCase):
    os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    @patch('tkinter.Canvas.create_oval')
    def test_no_first_click(self, mock_create_oval):
        # Создаем мок-объект для класса Sketch
        sketch = Mock()
        sketch.old_x = None
        sketch.old_y = None
        sketch.fill_color_line = 'black'
        sketch.temp = []

        # Создаем мок-объект для события
        mock_event = Mock()
        mock_event.x = 100
        mock_event.y = 200

        # Вызываем функцию circle_ranging
        sketch.circle_ranging(mock_event)

        # Проверяем, что create_oval не был вызван
        mock_create_oval.assert_not_called()

        # Проверяем, что temp остался пустым
        self.assertEqual(sketch.temp, [])
