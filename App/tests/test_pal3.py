# Тест №2.1: Проверка обработки исключения при выборе цвета в color_pal(негативный)
import unittest
from unittest.mock import patch
import tkinter as tk
from App.paint import Sketch
import os

class TestColorPal(unittest.TestCase):
    def setUp(self):
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        self.root = tk.Tk()
        self.sketch = Sketch(self.root)
        self.sketch.fill_color_line = 'initial_color'  # Устанавливаем начальное значение

    @patch('tkinter.colorchooser.askcolor')
    def test_color_pal_exception_handling(self, mock_askcolor):
        # Моделируем ситуацию, когда пользователь не выбрал цвет
        mock_askcolor.return_value = (None, None)

        # Вызываем функцию color_pal
        self.sketch.color_pal()

        # Проверяем, что значение self.fill_color_line не изменилось
        self.assertEqual(self.sketch.fill_color_line, 'initial_color')

    def tearDown(self):
        self.root.destroy()



