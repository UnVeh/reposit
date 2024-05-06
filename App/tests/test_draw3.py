#Тест №2.1: Проверка отсутствия предыдущих координат(негативный)
import unittest
from unittest.mock import MagicMock
import tkinter
from App.paint import Sketch
import os

class TestKoord(unittest.TestCase):
    def setUp(self):
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        self.root = tkinter.Tk()
        self.sketch = Sketch(self.root)
        self.sketch.make_canvas = MagicMock()
        self.sketch.old_x = None
        self.sketch.old_y = None
        self.sketch.fill_color_line = "black"
        self.sketch.width_maintainer = 5
        self.sketch.temp = []

    def tearDown(self):
        self.root.destroy()

    def test_draw_with_brush_no_previous_coords(self):
        e = MagicMock()
        e.x = 20
        e.y = 20
        self.sketch.draw_with_brush(e)
        self.sketch.make_canvas.create_line.assert_not_called()
        self.assertEqual(self.sketch.old_x, 20)
        self.assertEqual(self.sketch.old_y, 20)
        self.assertEqual(len(self.sketch.temp), 0)



