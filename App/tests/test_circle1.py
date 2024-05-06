# Тест №1.1: Проверка рисования окружности(позитивный)
import unittest
from tkinter import Tk
from App.paint import Sketch
import os

class TestSketch(unittest.TestCase):
    def setUp(self):
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

        self.root = Tk()
        self.sketch = Sketch(self.root)

    def test_circle_ranging(self):
        # Моделируем событие движения мыши
        self.sketch.old_x = 100
        self.sketch.old_y = 100
        event = type('Event', (), {'x': 200, 'y': 200})()
        self.sketch.circle_ranging(event)

        # Проверяем, что создан правильный объект на холсте
        self.assertEqual(len(self.sketch.temp), 1)
        oval = self.sketch.temp[0]
        self.assertEqual(self.sketch.make_canvas.coords(oval), [100, 100, 200, 200])
        self.assertEqual(self.sketch.make_canvas.itemcget(oval, 'fill'), self.sketch.fill_color_line)

    def tearDown(self):
        self.root.destroy()

