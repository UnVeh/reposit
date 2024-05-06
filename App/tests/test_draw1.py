# Тест № 1.1 Проверка рисования линии(позитивный)
import unittest
import tkinter
from unittest.mock import MagicMock
from App.paint import Sketch
import os

class TestLine(unittest.TestCase):
    def setUp(self):
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        self.root = tkinter.Tk()
        self.sketch = Sketch(self.root)
        self.sketch.make_canvas = MagicMock()
        self.sketch.old_x = 10
        self.sketch.old_y = 10
        self.sketch.fill_color_line = "black"
        self.sketch.width_maintainer = 5

    def tearDown(self):
        self.root.destroy()

    def test_draw_with_brush(self):
        e = MagicMock()
        e.x = 20
        e.y = 20
        self.sketch.draw_with_brush(e)
        self.sketch.make_canvas.create_line.assert_called_with(10, 10, 20, 20, fill="black", width=5, smooth=True, capstyle="round")
        self.assertEqual(self.sketch.old_x, 20)
        self.assertEqual(self.sketch.old_y, 20)

