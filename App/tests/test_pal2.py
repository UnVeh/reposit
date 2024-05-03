# Тест №1.2: Проверка выбора цвета из встроенной палитры(позитивный)
import unittest
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

    def test_colors_selection(self):
        # Список ожидаемых цветов из палитры
        expected_colors = [
            "red", "#0C68FF", "#F7FC11", "#A90DCB", "#FF970C", "#29C112", "#FF6AC0",
            "black", "#852B09", "#29D4B5", "#89E71F", "#36134C", "#FFD379", "#B4B3B2",
            "#FEA3A3", "#FFFC9C"
        ]

        # Проверяем каждый цвет из палитры
        for idx, color in enumerate(expected_colors, start=1):
            self.sketch.colors(idx)
            self.assertEqual(self.sketch.fill_color_line, color)

if __name__ == '__main__':
    unittest.main()
