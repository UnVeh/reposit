# Тест №2.1 заполнение_несвязанных_объектов (негативный)
import unittest
from tkinter import Tk
from App.paint import Sketch
import os

class TestFillNotNeighbors(unittest.TestCase):
    def setUp(self):
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        self.root = Tk()
        self.sketch = Sketch(self.root)
        self.canvas = self.sketch.make_canvas

    def tearDown(self):
        self.root.destroy()

    def test_unconnected_objects_fill(self):
        # Создаем несвязанные объекты на холсте с разными цветами
        rect1_color = "blue"
        rect2_color = "green"
        oval_color = "red"
        fill_color = "black"

        rect1_id = self.canvas.create_rectangle(50, 50, 150, 150, fill=rect1_color)
        rect2_id = self.canvas.create_rectangle(200, 200, 300, 300, fill=rect2_color)
        oval_id = self.canvas.create_oval(350, 350, 450, 450, fill=oval_color)

        # Вызываем fill_shape на первом прямоугольнике
        x, y = 75, 75  # Координаты внутри первого прямоугольника
        self.sketch.fill_shape(Event(x=x, y=y))

        # Проверяем, что только первый прямоугольник заполнен новым цветом
        new_color1 = self.canvas.itemcget(rect1_id, "fill")
        new_color2 = self.canvas.itemcget(rect2_id, "fill")
        new_color3 = self.canvas.itemcget(oval_id, "fill")
        self.assertEqual(new_color1, fill_color)
        self.assertEqual(new_color2, rect2_color)
        self.assertEqual(new_color3, oval_color)

class Event:
    def __init__(self, x, y):
        self.x = x
        self.y = y

