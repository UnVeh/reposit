#Тест №2.2: Проверка недопустимых параметров(негативный)
import unittest
from unittest.mock import MagicMock
import tkinter
from App.paint import Sketch
import os

class TestSketch(unittest.TestCase):
    def setUp(self):
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        self.root = tkinter.Tk()
        self.sketch = Sketch(self.root)
        self.sketch.make_canvas = MagicMock()
        self.sketch.old_x = 10
        self.sketch.old_y = 10
        self.sketch.fill_color_line = "not_a_valid_color"
        self.sketch.width_maintainer = -5
        self.sketch.temp = []

    def tearDown(self):
        self.root.destroy()

    def test_draw_with_brush_invalid_params(self):
        e = MagicMock()
        e.x = 20
        e.y = 20
        try:
            self.sketch.draw_with_brush(e)
        except Exception:
            self.fail("draw_with_brush raised an exception with invalid parameters")

        self.sketch.make_canvas.create_line.assert_called_with(10, 10, 20, 20, fill="not_a_valid_color", width=-5, smooth=True, capstyle="round")
        self.assertEqual(self.sketch.old_x, 20)
        self.assertEqual(self.sketch.old_y, 20)
        self.assertEqual(len(self.sketch.temp), 1)
        self.assertIn(self.sketch.make_canvas.create_line.return_value, self.sketch.temp)


