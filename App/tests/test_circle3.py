# Тест 2.1 Некорректные координаты(негативный)
import unittest
import tkinter
from unittest.mock import MagicMock, patch
from App.paint import Sketch
import os

class TestSketch(unittest.TestCase):
    def setUp(self):
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        self.root = tkinter.Tk()
        self.sketch = Sketch(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('tkinter.Canvas')
    def test_circle_ranging_invalid_coords(self, mock_canvas):
        # Создаем mock объект для создания холста
        mock_canvas_instance = mock_canvas.return_value

        # Создаем mock объект для события мыши
        mock_event = MagicMock()
        mock_event.x = -100  # Некорректные координаты x
        mock_event.y = 1000  # Некорректные координаты y

        # Вызываем функцию circle_ranging с mock объектом события
        self.sketch.circle_ranging(mock_event)

        # Проверяем, что функция не вызвала исключений
        self.assertIsNone(mock_canvas_instance.create_oval.call_args)

