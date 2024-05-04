# Тест №1.2 заполнение_связанных_объектов(позитивный)
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

    def test_connected_objects_fill(self):
        # Создаем группу связанных объектов на холсте
        initial_color = "blue"
        fill_color = "black"
        rect1_id = self.canvas.create_rectangle(50, 50, 150, 150, fill=initial_color)
        rect2_id = self.canvas.create_rectangle(100, 100, 200, 200, fill=initial_color)
        oval_id = self.canvas.create_oval(150, 150, 250, 250, fill=initial_color)

        # Вызываем fill_shape на одном из объектов
        x, y = 75, 75  # Координаты внутри первого прямоугольника
        self.sketch.fill_shape(Event(x=x, y=y))

        # Проверяем, что все связанные объекты заполнены новым цветом
        new_color1 = self.canvas.itemcget(rect1_id, "fill")
        new_color2 = self.canvas.itemcget(rect2_id, "fill")
        new_color3 = self.canvas.itemcget(oval_id, "fill")
        self.assertEqual(new_color1, fill_color)
        self.assertEqual(new_color2, fill_color)
        self.assertEqual(new_color3, fill_color)

# Вспомогательный класс для создания события мыши
class Event:
    def __init__(self, x, y):
        self.x = x
        self.y = y

