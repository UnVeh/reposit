# Тест №1.2: Проверка добавления окружности в список temp (позитивный)
import unittest
from tkinter import Tk
from App.paint import Sketch
import os

class TestCircleRangingAddToTemp(unittest.TestCase):
    def setUp(self):
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        self.root = Tk()
        self.sketch = Sketch(self.root)

    def test_circle_ranging_add_to_temp(self):

        # Подготовка данных
        self.sketch.old_x = 50
        self.sketch.old_y = 50
        event = type('Event', (), {'x': 150, 'y': 150})()

        # Вызов функции, которую тестируем
        self.sketch.circle_ranging(event)

        # Проверка ожидаемого результата
        self.assertEqual(len(self.sketch.temp), 1)
        oval = self.sketch.temp[0]
        self.assertEqual(self.sketch.make_canvas.coords(oval), [50, 50, 150, 150])
        self.assertEqual(self.sketch.make_canvas.itemcget(oval, 'fill'), self.sketch.fill_color_line)

    def tearDown(self):
        self.root.destroy()

