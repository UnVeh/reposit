# Тест №1.1 заполнение_одиночного_объекта(позитивный)
import unittest
from tkinter import Tk
from App.paint import Sketch
import os

class TestFillShape(unittest.TestCase):
    def setUp(self):
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        self.root = Tk()
        self.sketch = Sketch(self.root)
        self.canvas = self.sketch.make_canvas

    def tearDown(self):
        self.root.destroy()

    def test_single_object_fill(self):
        # Создаем овал на холсте
        initial_color = "blue"
        fill_color = "black"
        oval_id = self.canvas.create_oval(50, 50, 150, 150, fill=initial_color)

        # Вызываем fill_shape на созданном овале
        x, y = 100, 100  # Координаты внутри овала
        self.sketch.fill_shape(Event(x=x, y=y))

        # Проверяем, что овал заполнен новым цветом
        new_color = self.canvas.itemcget(oval_id, "fill")
        self.assertEqual(new_color, fill_color)

class Event:
    def __init__(self, x, y):
        self.x = x
        self.y = y


