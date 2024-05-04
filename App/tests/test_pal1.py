# Тест №1.1: Проверка выбора цвета с помощью color chooser(позитивный)
import unittest
from unittest.mock import patch
from tkinter import Tk
from App.paint import Sketch
import os

class TestColorPalette(unittest.TestCase):
    def setUp(self):
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        self.root = Tk()
        self.sketch = Sketch(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('tkinter.colorchooser.askcolor')
    def test_color_pal_selection(self, mock_askcolor):
        # Задаем желаемый цвет, который будет возвращен мокированной функцией askcolor
        desired_color = "#FF0000"
        mock_askcolor.return_value = ((), desired_color)

        # Вызываем функцию color_pal
        self.sketch.color_pal()

        # Проверяем, что self.fill_color_line содержит выбранный цвет
        self.assertEqual(self.sketch.fill_color_line, desired_color)


