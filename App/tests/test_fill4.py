# Тест №2.2 заполнение_вложенных_объектов (негативный)
import unittest
from tkinter import Tk
from App.paint import Sketch
import os

class TestFillShapes(unittest.TestCase):
    def setUp(self):
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        self.root = Tk()
        self.sketch = Sketch(self.root)
        self.canvas = self.sketch.make_canvas

    def tearDown(self):
        self.root.destroy()

    def test_fill_nested_objects(self):
        # Создать два объекта на холсте, один внутри другого
        outer_rect = self.canvas.create_rectangle(50, 50, 150, 150, fill="black")
        inner_rect = self.canvas.create_rectangle(75, 75, 125, 125, fill="green")

        # Вызвать функцию fill_shape внутри внешнего объекта
        x, y = 100, 100
        self.sketch.fill_shape(Event(self.canvas, x=x, y=y))

        # Проверить, что оба объекта заполнены новым цветом
        fill_color = self.sketch.fill_color_line
        outer_rect_color = self.canvas.itemcget(outer_rect, "fill")
        inner_rect_color = self.canvas.itemcget(inner_rect, "fill")
        self.assertEqual(outer_rect_color, fill_color)
        self.assertEqual(inner_rect_color, fill_color)

class Event:
    def __init__(self, canvas, x, y):
        self.x = x
        self.y = y
        self.canvas = canvas



