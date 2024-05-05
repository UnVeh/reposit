# Ошибка №1
 
* Описание:  ошибка, когда на холсте нет нарисованный объектов
* Тест: test_circle3
* Входные данные:

     self.sketch.old_x = None
     self.sketch.old_y = None
     event = type('Event', (), {'x': 100, 'y': 100})()
  
* Ожидаемый результат: не должно быть ошибок
* Фактический результат: IndexError: tuple index out of range
* Возможная причина: Это произошло потому что,  если список self.sketch.make_canvas.find_all() пуст, то есть на холсте нет никаких объектов, то происходит ошибка
* Статус: Ошибка исправлена и проверена. Строка self.assertEqual(self.sketch.make_canvas.itemcget(self.sketch.make_canvas.find_all()[0], 'fill'), '') исправлена на self.assertEqual(len(self.sketch.make_canvas.find_all()), 0). Теперь происходит проверка, что len(self.sketch.make_canvas.find_all()) равен 0, что означает, что на холсте нет нарисованных объектов

# Ошибка №2

* Описание: при тесте создается овал красного цвета, выходит ошибка
* Тест: test_fill1
* Входные данные: 
  initial_color = "blue"
  fill_color = "red"
  oval_id = self.canvas.create_oval(50, 50, 150, 150, fill=initial_color)
  x, y = 100, 100  
  new_color = self.canvas.itemcget(oval_id, "fill")
* Ожидаемый результат: на холсте должен быть черный овал
* Фактический результат: овал красного цвета
* Возможная причина: в приложении цвет по умолчанию – черный. При создании овала в тесте, цвет – красный
* Статус: Ошибка исправлена и проверена. 'red' заменен на 'black'

# Ошибка № 3

* Описание: Объект должен был залиться зеленым цветом, но этого не проиошло
* Тест: test_fill4
* Входные данные: 
  outer_color = "blue"
  inner_color = "green"
  fill_color = "black"
  outer_id = self.canvas.create_rectangle(50, 50, 200, 200, fill=outer_color)
  inner_id = self.canvas.create_oval(100, 100, 150, 150, fill=inner_color)
  x, y = 75, 75  
* Ожидаемый результат: объект должен стать зеленого цвета
* Фактический результат: объект не поменял цвет
* Возможная причина: ошибка во входных данных
* Статус: Ошибка исправлена и проверена. Убраны строки: outer_color = "blue" inner_color = "green" fill_color = "black". Строки: outer_id = self.canvas.create_rectangle(50, 50, 200, 200, fill=outer_color)
 inner_id = self.canvas.create_oval(100, 100, 150, 150, fill=inner_color) заменены на: outer_rect = self.canvas.create_rectangle(50, 50, 150, 150, fill="black")
 inner_rect = self.canvas.create_rectangle(75, 75, 125, 125, fill="green")

# Ошибка №4

* Описание: ошибка, когда цвет не был выбран
* Тест: test_pal3
* Входные данные:
 self.sketch.fill_color_line = 'initial_color'
* Ожидаемый результат: None
* Фактический результат: 'initial_color'
* Возможная причина: ошибка в функции color_pal
* Статус: Ошибка исправлена и проверена. Добавлена проверка (когда не выбран цвет) в функцию color_pal: if take_color
