from tkinter import *
from tkinter import messagebox, colorchooser, filedialog
from PIL import Image, ImageTk, ImageGrab


class Sketch:
    def __init__(self,
                 root):  # происходит инициализация различных переменных и создание графического интерфейса программы.

        self.window = root  # переменная, хранящая ссылку на главное окно программы.
        self.window.title("Paint")
        self.make_canvas = Canvas(self.window, width=1060, height=650,
                                  bg="white")  # переменная, хранящая ссылку на холст, на котором будет отображаться рисунок.
        self.make_canvas.place(x=250, y=20)

        # переменные, хранящие ссылки на различные меню программы
        self.my_menu = None
        self.file_menu = None
        self.edit_menu = None
        self.color_menu = None

        # различные переменные, используемые в программе для управления отображением и состоянием элементов интерфейста.
        self.coord = None
        self.status = None
        self.controller_set = None
        self.das_img = None
        self.brush_img = None
        self.circle_img = None
        self.rectangle_img = None
        self.eraser_img = None
        self.delete_seg = None
        self.triangle_img = None
        self.pipette_img = None
        self.color_frame = None
        self.choosing_color = None
        self.color = None
        self.permanent_color = None
        self.segment_1 = None
        self.palette_color = None
        self.palette_img = None
        self.eraser = None
        self.segment_2 = None
        self.top = None
        self.make_width_frame = None
        self.shape_outline_width_label = None
        self.eraser_width_label = None
        self.eraser_controller = None
        self.notation_box = None
        self.red_color = None
        self.blue_color = None
        self.yellow_color = None
        self.violet_color = None
        self.orange_color = None
        self.green_color = None
        self.pink_color = None
        self.blue_color = None
        self.brown_color = None
        self.black_color = None
        self.color_frame2 = None
        self.lightblue_color = None
        self.green_yellow_color = None
        self.plum_color = None
        self.lightpink_color = None
        self.grey_color = None
        self.skin_color = None
        self.lightyellow_color = None
        self.fill_img = None
        self.line_img = None
        self.color_frame1 = None
        self.scroll_down_img = None
        self.scroll_up_img = None
        self.scroll_down_button = None
        self.scroll_up_button = None

        self.old_x = None
        self.old_y = None
        self.new_x = None
        self.new_y = None

        # Создаются кнопки для инструментов рисования
        self.brush = Button(self.window)
        self.circle = Button(self.window)
        self.rec = Button(self.window)
        self.triangle_btn = Button(self.window)
        self.eraser = Button(self.window)
        self.line = Button(self.window)
        self.pipette_button = Button(self.window)
        self.fill_button = Button(self.window)


        # Создаются контейнеры для хранения изображений, отмены действий, временного хранения, цветов и меню изображений
        self.img_container = []
        self.undo_container = []
        self.temp = []
        self.color_container = []
        self.menu_img_container = []

        # Устанавливаются значения для цветов
        self.fill_color = "#FFFFFF"
        self.flood = None
        self.fill_color_line = "black"
        self.color_container_box = "black"

        # Задается начальное значение ширины кисти, счетчиков и активного инструмента
        self.color_circle_width_maintainer = 15
        self.img_counter = -1
        self.width_controller_scale = 0
        self.counter = -1
        self.width_maintainer = 2
        self.erase_width_maintainer = 5
        self.active_coloring = 2

        # вызываются различные методы и функции для настройки и управления интерфейсом программы.
        self.control(1)  # Вызывается метод control() с аргументом 1 для установки определенного состояния интерфейса.
        self.controller()  # Вызывается метод controller() для управления интерфейсом и отображения элементов.
        self.make_menu()  # для создания меню программы
        self.make_status_bar()  # оздания строки состояния программы
        self.width_controller()  # для настройки контроллера ширины кисти.
        self.color_set()  # для установки цветовых параметров
        self.make_canvas.bind('<Motion>',
                              self.movement_cursor)  # Создается привязка события движения мыши к методу movement_cursor()
        # Movement
        self.window.bind('<space>', self.movement)
        self.window.bind('<Left>', self.movement)
        self.window.bind('<Right>', self.movement)
        self.window.bind('<Up>', self.movement)
        self.window.bind('<Down>', self.movement)

    # В этой части программы определяется метод control(), который управляет различными функциями и действиями в зависимости от значения аргумента notation
    def control(self, notation):
        if self.temp:  # Если у переменной temp есть элементы, то вызывается метод delete у объекта make_canvas для удаления элемента изображения, хранящегося в переменной temp
            self.make_canvas.delete(self.temp.pop())
        # Если переменная notation_box существует и ее состояние равно DISABLED, то включается ее состояние, устанавливая значение NORMAL.
        if self.notation_box:
            if self.notation_box['state'] == DISABLED:
                self.notation_box['state'] = NORMAL
        self.make_canvas.config(cursor="plus")
        self.make_canvas.unbind("<B1-Motion>")
        self.make_canvas.unbind("<ButtonRelease-1>")
        self.make_canvas.unbind("<Button-1>")

        # В зависимости от значения аргумента notation, создаются различные привязки событий и вызываются соответствующие методы
        if notation == 1:
            self.make_canvas.config(cursor="dot")
            self.make_canvas.bind("<B1-Motion>", self.draw_with_brush)
        elif notation == 2:
            self.make_canvas.bind("<B1-Motion>", self.circle_ranging)
        elif notation == 3:
            self.make_canvas.bind("<B1-Motion>", self.rectangle_ranging)

        elif notation == 4:
            self.make_canvas.config(cursor="dotbox")
            self.make_canvas.bind("<B1-Motion>", self.erasing_setup)
        elif notation == 5:
            self.make_canvas.bind('<B1-Motion>', self.triangle_ranging)
        elif notation == 6:
            self.make_canvas.bind("<B1-Motion>", self.line_ranging)

        elif notation == 7:
            take = messagebox.askyesno("Clear Conformation", "Хотите отчистить холст?")
            if take is True:
                self.make_canvas.delete("all")
                self.clear()
        elif notation == 8:
            take = messagebox.askyesno("Exit Conformation", "Хотите выйти?")
            if take is True:
                self.window.destroy()
        elif notation == 9:
            self.make_canvas.config(cursor="cross")  # Изменить курсор на пипетку
            self.make_canvas.bind("<Button-1>", self.get_color)  # Привязать обработчик события нажатия на холст

        elif notation == 10:
            self.make_canvas.config(cursor="target")
            self.make_canvas.bind("<Button-1>", self.fill_shape)

    def controller(self):
        self.controller_set = Frame(self.window, width=190, height=680, bd=0, bg="#4F4F4F",
                                    highlightbackground="grey50", highlightthickness=2, relief="solid")
        self.controller_set.place(x=0, y=0)

        self.notation_box = Listbox(self.controller_set, width=4, height=10, font=("Arial", 10, "bold"), fg="grey37",
                                    bg="grey12", relief=SUNKEN, bd=5)
        self.notation_box.place(x=15, y=435)


        self.segment_1 = Label(self.controller_set, text="Фигуры", bg="#4F4F4F", fg="grey70",
                               font=("Arial", 12, "bold"), highlightbackground="grey50", relief="solid", bd=2, padx=15,
                               pady=1)
        self.segment_1.place(x=44, y=172)

        self.rectangle_img = ImageTk.PhotoImage(Image.open("Pictures/rectan.png").resize((27, 27), Image.LANCZOS))
        self.rec = Button(self.controller_set, image=self.rectangle_img, bg="#4F4F4F", relief="solid", fg="#4F4F4F",
                          bd=0, activebackground="#4F4F4F", command=lambda: self.control(3))
        self.rec.place(x=20, y=220)

        self.triangle_img = ImageTk.PhotoImage(Image.open("Pictures/triangle.png").resize((27, 27), Image.LANCZOS))
        self.triangle_btn = Button(self.controller_set, image=self.triangle_img, bg="#4F4F4F", relief="solid",
                                   fg="#4F4F4F", activebackground="#4F4F4F",
                                   bd=0, command=lambda: self.control(5))
        self.triangle_btn.place(x=60, y=220)

        self.circle_img = ImageTk.PhotoImage(Image.open("Pictures/circle.png").resize((27, 27), Image.LANCZOS))
        self.circle = Button(self.controller_set, image=self.circle_img, bg="#4F4F4F", relief="solid", fg="#4F4F4F",
                             activebackground="#4F4F4F",
                             bd=0, command=lambda: self.control(2))
        self.circle.place(x=100, y=220)

        self.line_img = ImageTk.PhotoImage(Image.open("Pictures/line.png").resize((22, 22), Image.LANCZOS))
        self.line = Button(self.controller_set, image=self.line_img, fg="#4F4F4F", bg="#4F4F4F",
                           activebackground="#4F4F4F", relief="solid", bd=0,
                           command=lambda: self.control(6))
        self.line.place(x=140, y=220)

        self.segment_2 = Label(self.controller_set, text="Инструменты", bg="#4F4F4F", fg="grey70",
                               highlightbackground="grey50",
                               font=("Arial", 12, "bold"), relief="solid", bd=2, padx=10, pady=1)
        self.segment_2.place(x=25, y=280)

        self.brush_img = ImageTk.PhotoImage(Image.open("Pictures/paintbrush.png").resize((27, 27), Image.LANCZOS))
        self.brush = Button(self.controller_set, image=self.brush_img, bg="#4F4F4F", relief="solid", width=30,
                             height=30, fg="#4F4F4F", bd=0, activebackground="#4F4F4F", command=lambda: self.control(1))
        self.brush.place(x=17, y=330)

        self.eraser_img = ImageTk.PhotoImage(Image.open("Pictures/eraser.png").resize((27, 27), Image.LANCZOS))
        self.eraser = Button(self.controller_set, image=self.eraser_img, bg="#4F4F4F", relief="solid", width=30,
                             height=30, fg="#4F4F4F", activebackground="#4F4F4F", bd=0, command=lambda: self.control(4))
        self.eraser.place(x=57, y=330)

        self.pipette_img = ImageTk.PhotoImage(Image.open("Pictures/pipette.png").resize((27, 27), Image.LANCZOS))
        self.pipette_button = Button(self.controller_set, image=self.pipette_img, width=30, height=30, bg="#4F4F4F", relief="solid",
                                     fg="#4F4F4F", bd=0, activebackground="#4F4F4F", command=lambda: self.control(9))
        self.pipette_button.place(x=97, y=330)

        self.fill_img = ImageTk.PhotoImage(Image.open("Pictures/fill-color.png").resize((27, 27), Image.LANCZOS))
        self.fill_button = Button(self.controller_set, image=self.fill_img, bg="#4F4F4F",
                                  relief="solid", fg="#4F4F4F", bd=0, activebackground="#4F4F4F",
                                  command=lambda: self.control(10))
        self.fill_button.place(x=137, y=330)

        self.scroll_up_img = ImageTk.PhotoImage(Image.open("Pictures/up.png").resize((28, 15), Image.LANCZOS))
        self.scroll_up_button = Button(self.controller_set, image=self.scroll_up_img, command=self.scroll_up, relief="solid", width=26, height=13, bd=0, bg="#4F4F4F", activebackground="#4F4F4F")
        self.scroll_up_button.place(x=20, y=414)

        self.scroll_down_img = ImageTk.PhotoImage(Image.open("Pictures/down.png").resize((28, 15), Image.LANCZOS))
        self.scroll_down_button = Button(self.controller_set, image=self.scroll_down_img, command=self.scroll_down, relief="solid", width=26, height=13, bd=0, bg="#4F4F4F", activebackground="#4F4F4F")
        self.scroll_down_button.place(x=20, y=623)



    def scroll_up(self):
        self.notation_box.yview_scroll(-1, "units")

    def scroll_down(self):
        self.notation_box.yview_scroll(1, "units")


    # Menu setup
    def make_menu(self):
        self.my_menu = Menu(self.window)
        self.window.config(menu=self.my_menu)
        menu_img = ["open_img.png", "save_img.png", "exit_img.png", "undo_img.png", "clear_img.png"]
        for i in range(5):
            self.menu_img_container.append(i)
            self.menu_img_container[i] = ImageTk.PhotoImage(
                Image.open("Pictures/" + menu_img[i]).resize((30, 30), Image.LANCZOS))

        self.file_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Открыть", accelerator="(Ctrl+O)", command=lambda: self.open_file(False),
                                   image=self.menu_img_container[0], compound=LEFT, background="#4F4F4F",
                                   foreground="grey80", font=("Arial", 10, "bold"), activebackground="grey60",
                                   activeforeground="grey40")
        self.file_menu.add_command(label="Сохранить", accelerator="(Ctrl+S)", command=lambda: self.save_file(False),
                                   state=DISABLED, image=self.menu_img_container[1], compound=LEFT,
                                   background="#4F4F4F", foreground="grey80", font=("Arial", 10, "bold"),
                                   activebackground="grey60", activeforeground="grey40")
        self.file_menu.add_command(label="Выйти", command=lambda: self.control(8), image=self.menu_img_container[2],
                                   compound=LEFT, background="#4F4F4F", foreground="grey80", font=("Arial", 10, "bold"),
                                   activebackground="grey60", activeforeground="grey40")
        self.window.bind('<Control-Key-o>', self.open_file)
        self.window.bind('<Control-Key-s>', self.save_file)

        self.edit_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Опции", menu=self.edit_menu)
        self.edit_menu.add_command(label="Отменить", command=lambda: self.undo(False), accelerator="(Ctrl+Z)",
                                   state=DISABLED, image=self.menu_img_container[3], compound=LEFT,
                                   background="#4F4F4F", foreground="grey80", font=("Arial", 10, "bold"),
                                   activebackground="grey60", activeforeground="grey40")
        self.edit_menu.add_command(label="Очистить", command=lambda: self.control(7), state=DISABLED,
                                   image=self.menu_img_container[4], compound=LEFT, background="#4F4F4F",
                                   foreground="grey80", font=("Arial", 10, "bold"), activebackground="grey60",
                                   activeforeground="grey40")
        self.window.bind("<Control-Key-z>", self.undo)



    def movement_cursor(self, e):  # Позиция курсора время движения
        self.coord.config(text=str(e.x) + "," + str(e.y) + "px")

    def make_status_bar(self):
        self.status = Label(self.window, text="Paint", fg="grey60", bg="grey11", font=("Arial", 12, "bold"))
        self.status.place(x=1250, y=685)

        self.coord = Label(self.window, text="", fg="grey60", bg="grey11", font=("Arial", 9, "bold"))
        self.coord.place(x=20, y=687)

    def open_file(self, e):
        if self.notation_box['state'] == DISABLED:
            self.notation_box['state'] = NORMAL
        self.make_canvas.unbind("<B1-Motion>")
        self.make_canvas.unbind("<ButtonRelease-1>")
        self.make_canvas.unbind("<Button-1>")

        image_mine = filedialog.askopenfilename(initialdir="\Desktop", title="Select an image",
                                                filetypes=(("JPEG Images", "*.jpg"), ("All images", "*.*")))

        if image_mine:
            self.img_container.append(ImageTk.PhotoImage(Image.open(image_mine)))
            self.img_counter += 1
            take = self.make_canvas.create_image(100, 200, image=self.img_container[self.img_counter])
            self.undo_container.append(take)
            self.notation_box.insert(END, len(self.undo_container) - 1)
            self.reset()
        self.control(1)

    def save_file(self, e):
        file = filedialog.asksaveasfilename(initialdir="Saved_file", filetypes=[("PNG File", "*.png")])
        if file:
            x = self.window.winfo_rootx() + self.make_canvas.winfo_x() + 10
            y = self.window.winfo_rooty() + self.make_canvas.winfo_y() + 10
            x1 = x + self.make_canvas.winfo_width() - 20
            y1 = y + self.make_canvas.winfo_height() - 20
            ImageGrab.grab().crop((x, y, x1, y1)).save(file + '.png')
            self.window.title("Paint" + "-----" + file + ".png")

    def undo(self, e):
        if self.notation_box:
            if self.notation_box['state'] == DISABLED:
                self.notation_box['state'] = NORMAL
            self.notation_box.delete(END)
        if self.undo_container:
            take = self.undo_container.pop()
            if type(take) == list:
                for x in take:
                    self.make_canvas.delete(x)
            else:
                self.make_canvas.delete(take)
        if len(self.undo_container) == 0:
            self.clear()

    def clear(self):
        self.undo_container.clear()  # отчистка контейнера
        self.notation_box.delete(0, END)  # Удаляет все значения из виджета notation_box, начиная с 0 и до конца (END)
        self.file_menu.entryconfig("Сохранить", state=DISABLED)  # Деактивирует пункт меню "Save" в меню file_menu
        self.edit_menu.entryconfig("Отменить", state=DISABLED)
        self.edit_menu.entryconfig("Очистить", state=DISABLED)

        self.temp.clear()
        self.img_container.clear()

        self.img_counter = -1
        self.counter = -1

    def reset(self):
        if self.notation_box:
            self.file_menu.entryconfig("Сохранить", state=NORMAL)
            self.edit_menu.entryconfig("Отменить", state=NORMAL)
            self.edit_menu.entryconfig("Очистить", state=NORMAL)

            # self.option_menu.entryconfig("Movement", state=NORMAL)
            if self.notation_box['state'] == DISABLED:
                self.notation_box['state'] = NORMAL
        self.new_x = None
        self.new_y = None
        self.old_x = None
        self.old_y = None
        self.temp = []

    def fill_shape(self, event=None):
        if event is None:
            return

        x, y = event.x, event.y
        fill_color = self.fill_color_line

        if not self.make_canvas.find_all():
            return  # Если на холсте нет объектов, выходим из функции

        shape_id = self.make_canvas.find_closest(x, y)[0]
        original_color = self.make_canvas.itemcget(shape_id, "fill")

        def fill_neighbors(obj_id):
            # Получаем все объекты-соседи заданного объекта
            neighbor_ids = self.make_canvas.find_overlapping(*self.make_canvas.bbox(obj_id))

            # Заливаем объекты-соседи цветом, если они имеют тот же цвет и продолжаем заполнение для каждого из них
            for neighbor_id in neighbor_ids:
                if self.make_canvas.itemcget(neighbor_id, "fill") == original_color:
                    self.make_canvas.itemconfig(neighbor_id, fill=fill_color)
                    fill_neighbors(neighbor_id)

        # Заливаем начальный объект цветом и запускаем процесс заполнения его соседей
        self.make_canvas.itemconfig(shape_id, fill=fill_color)
        fill_neighbors(shape_id)
        self.make_canvas.unbind("<Button-1>")  # Отвязать обработчик события
        self.make_canvas.config(cursor="arrow")

    def draw_with_brush(self, e):
        if self.old_x and self.old_y:
            brush_line = self.make_canvas.create_line(self.old_x, self.old_y, e.x, e.y, fill=self.fill_color_line,
                                                       width=self.width_maintainer, smooth=True, capstyle=ROUND)
            self.temp.append(brush_line)

        self.old_x = e.x
        self.old_y = e.y

        def push_value(e):
            self.undo_container.append(self.temp)
            self.notation_box.insert(END, len(self.undo_container) - 1)
            self.reset()

        self.make_canvas.bind("<ButtonRelease-1>", push_value)

    def erasing_setup(self, e):
        if self.old_x and self.old_y:
            take = self.make_canvas.create_line(self.old_x, self.old_y, e.x, e.y, fill="white",
                                                width=self.erase_width_maintainer, smooth=True, capstyle=ROUND)
            self.temp.append(take)

        self.old_x = e.x
        self.old_y = e.y

        def real_erasing(e):
            self.undo_container.append(self.temp)
            self.notation_box.insert(END, len(self.undo_container) - 1)
            self.reset()

        self.make_canvas.bind("<ButtonRelease-1>", real_erasing)

    def circle_ranging(self, e):
        if self.old_x and self.old_y:
            take = self.make_canvas.create_oval(self.old_x, self.old_y, e.x, e.y, width=0, fill=self.fill_color_line)
            self.temp.append(take)
        else:
            self.old_x = e.x
            self.old_y = e.y

        def circle_make(e):
            for x in self.temp:
                self.make_canvas.delete(x)

            try:
                take = self.make_canvas.create_oval(self.old_x, self.old_y, e.x, e.y, width=0,
                                                    fill=self.fill_color_line)
                self.undo_container.append(take)
                self.notation_box.insert(END, len(self.undo_container) - 1)
                self.reset()
            except:
                print("Error")

        self.make_canvas.bind('<ButtonRelease-1>', circle_make)

    def rectangle_ranging(self, e):
        if self.old_x and self.old_y:
            take = self.make_canvas.create_rectangle(self.old_x, self.old_y, e.x, e.y, width=0,
                                                     fill=self.fill_color_line)
            self.temp.append(take)
        else:
            self.old_x = e.x
            self.old_y = e.y

        def rectangle_make(e):
            for x in self.temp:
                self.make_canvas.delete(x)
            try:
                take = self.make_canvas.create_rectangle(self.old_x, self.old_y, e.x, e.y, width=0,
                                                         fill=self.fill_color_line)
                self.undo_container.append(take)
                self.notation_box.insert(END, len(self.undo_container) - 1)
                self.reset()
            except:
                print("Error")

        self.make_canvas.bind('<ButtonRelease-1>', rectangle_make)

    def triangle_ranging(self, e):
        if self.old_x and self.old_y:
            take = self.make_canvas.create_polygon(self.old_x, self.old_y, self.old_x - (e.x - self.old_x), e.y, e.x,
                                                   e.y, width=0, fill=self.fill_color_line)
            self.temp.append(take)
        else:
            self.old_x = e.x
            self.old_y = e.y

        def triangle_make(e):
            for x in self.temp:
                self.make_canvas.delete(x)
            try:
                take = self.make_canvas.create_polygon(self.old_x, self.old_y, self.old_x - (e.x - self.old_x), e.y,
                                                       e.x,
                                                       e.y, width=0, fill=self.fill_color_line)
                self.undo_container.append(take)
                self.notation_box.insert(END, len(self.undo_container) - 1)
                self.reset()
            except:
                print("Error")

        self.make_canvas.bind('<ButtonRelease-1>', triangle_make)

    def get_color(self, event):
        x, y = event.x, event.y
        item = self.make_canvas.find_closest(x, y)  # Найти ближайший объект на холсте
        if item:
            object_color = self.make_canvas.itemcget(item[0], "fill")  # Получить цвет объекта
            self.fill_color_line = object_color  # Установить цвет карандаша
        self.make_canvas.unbind("<Button-1>")  # Отвязать обработчик события
        self.make_canvas.config(cursor="arrow")
        self.update_color_frame1()

    def line_ranging(self, e):
        if self.old_x and self.old_y:
            take = self.make_canvas.create_line(self.old_x, self.old_y, e.x, e.y, width=self.width_maintainer,
                                                fill=self.fill_color_line)
            self.temp.append(take)
        else:
            self.old_y = e.y
            self.old_x = e.x

        def line_make(e):
            for x in self.temp:
                self.make_canvas.delete(x)
            try:
                take = self.make_canvas.create_line(self.old_x, self.old_y, e.x, e.y, width=self.width_maintainer,
                                                    fill=self.fill_color_line, capstyle=ROUND)
                self.undo_container.append(take)
                self.notation_box.insert(END, len(self.undo_container) - 1)
                self.reset()
            except:
                print("Error")

        self.make_canvas.bind('<ButtonRelease-1>', line_make)


    def movement(self, e):
        try:
            take = self.notation_box.get(ACTIVE)
            self.notation_box.config(state=DISABLED)
            take = self.undo_container[take]
            if e.keycode == 32:
                self.notation_box.config(state=NORMAL)
            if e.keycode == 37:
                if type(take) == list:
                    for x in take:
                        self.make_canvas.move(x, -2, 0)
                else:
                    self.make_canvas.move(take, -2, 0)
            if e.keycode == 38:
                if type(take) == list:
                    for x in take:
                        self.make_canvas.move(x, 0, -2)
                else:
                    self.make_canvas.move(take, 0, -2)
            if e.keycode == 39:
                if type(take) == list:
                    for x in take:
                        self.make_canvas.move(x, 2, 0)
                else:
                    self.make_canvas.move(take, 2, 0)
            if e.keycode == 40:
                if type(take) == list:
                    for x in take:
                        self.make_canvas.move(x, 0, 2)
                else:
                    self.make_canvas.move(take, 0, 2)
        except:
            print("Error")

    def width_controller(self):
        self.make_width_frame = Frame(self.controller_set, bd=0, width=10, height=5, bg="#4F4F4F",
                                      highlightbackground="black", relief="solid")
        self.make_width_frame.place(x=68, y=400)

        def shape_outline_width_controller(e):
            self.width_maintainer = e

        def eraser_width_controller(e):
            self.erase_width_maintainer = e

        self.shape_outline_width_label = Label(self.make_width_frame, text="Линия", width=5, font=("Arial", 8, "bold"),
                                               bg="#4F4F4F", relief=FLAT, fg="grey70")
        self.shape_outline_width_label.pack(anchor="nw", padx=4, pady=5)

        self.width_controller_scale = Scale(self.make_width_frame, orient=VERTICAL, from_=0, to=120, width=12,
                                            length=200, bg="#4F4F4F", highlightbackground="grey20", relief="solid",
                                            fg="grey70", bd=1, command=shape_outline_width_controller,
                                            activebackground="grey50")
        self.width_controller_scale.set(self.width_maintainer)
        self.width_controller_scale.pack(side=LEFT, padx=4, pady=5)

        self.eraser_width_label = Label(self.make_width_frame, text="Ластик", font=("Arial", 8, "bold"), relief=FLAT,
                                        width=5,
                                        bg="#4F4F4F", fg="grey70")
        self.eraser_width_label.place(x=53, y=6)

        self.eraser_controller = Scale(self.make_width_frame, orient=VERTICAL, from_=0, to=120, width=12, length=200,
                                       bg="#4F4F4F", activebackground="grey50", highlightbackground="grey20",
                                       relief="solid",
                                       fg="grey70", bd=1, command=eraser_width_controller)
        self.eraser_controller.set(self.erase_width_maintainer)
        self.eraser_controller.pack(side=RIGHT, padx=4, pady=5)

    def color_pal(self):
        take_color = colorchooser.askcolor()[1]
        if take_color:  # Проверяем, что пользователь выбрал цвет
            self.fill_color_line = take_color
            self.update_color_frame1()

    def colors(self, c):
        color_list = [
            "red", "#0C68FF", "#F7FC11", "#A90DCB", "#FF970C", "#29C112", "#FF6AC0",
            "black", "#852B09", "#29D4B5", "#89E71F", "#36134C", "#FFD379", "#B4B3B2",
            "#FEA3A3", "#FFFC9C"
        ]
        self.fill_color_line = color_list[c - 1]
        self.update_color_frame1()

    def update_color_frame1(self):
        if self.color_frame1:
            self.color_frame1.destroy()
        self.color_frame1 = Frame(self.controller_set, bd=0, relief="solid", width=120,
                                  height=2, bg=self.fill_color_line)
        self.color_frame1.place(x=30, y=140)

    def color_set(self):
        self.color_frame = Frame(self.controller_set, bd=1, highlightbackground="black", relief="solid", width=10,
                                 height=10, bg="grey50")
        self.color_frame.place(x=23, y=20)

        self.color_frame2 = Frame(self.controller_set, bd=0, highlightbackground="black", relief="solid", width=10,
                                  height=10, bg="#4F4F4F")
        self.color_frame2.place(x=27, y=25)

        color_storage = ["red_img.png", "blue_img.png", "yellow.png", "violet_img.png", "orange_img.png",
                         "green_img.png", "pink_img.png", "black_img.png", "brown_image.png", "lightblue.png",
                         "greenyellow.png", "plum.png", "skin.png", "grey.png", "lightpink.png", "lightyellow.png"]

        for i in range(16):
            self.color_container.append(i)
            self.color_container[i] = ImageTk.PhotoImage(
                Image.open("Pictures/" + color_storage[i]).resize((20, 20), Image.LANCZOS))

        self.palette_img = ImageTk.PhotoImage(Image.open("Pictures/choose_color.png").resize((47, 47), Image.LANCZOS))
        self.palette_color = Button(self.color_frame2, image=self.palette_img, relief=RAISED, bd=0, width=47, height=47,
                                      bg="grey50", activebackground="grey50",
                                      command=self.color_pal)
        self.palette_color.grid(row=1, column=1)

        self.red_color = Button(self.color_frame, image=self.color_container[0], relief="solid", bd=0, bg="grey50",
                                width=20, height=20, fg="grey50", activebackground="grey50",
                                command=lambda: self.colors(1))
        self.red_color.grid(row=3, column=4, padx=2, pady=3)
        self.blue_color = Button(self.color_frame, image=self.color_container[1], relief="solid", bd=0, bg="grey50",
                                 width=20, height=20, fg="grey50", activebackground="grey50",
                                 command=lambda: self.colors(2))
        self.blue_color.grid(row=1, column=5, padx=2, pady=3)

        self.yellow_color = Button(self.color_frame, image=self.color_container[2], relief="solid", bd=0, bg="grey50",
                                   width=20, height=20, fg="grey50", activebackground="grey50",
                                   command=lambda: self.colors(3))
        self.yellow_color.grid(row=2, column=3, padx=2, pady=3)

        self.violet_color = Button(self.color_frame, image=self.color_container[3], relief="solid", bd=0, bg="grey50",
                                   width=20, height=20, fg="grey50", activebackground="grey50",
                                   command=lambda: self.colors(4))
        self.violet_color.grid(row=4, column=3, padx=2, pady=3)

        self.orange_color = Button(self.color_frame, image=self.color_container[4], relief="solid", bd=0, bg="grey50",
                                   width=20, height=20, fg="grey50", activebackground="grey50",
                                   command=lambda: self.colors(5))
        self.orange_color.grid(row=3, column=3, padx=2, pady=3)

        self.green_color = Button(self.color_frame, image=self.color_container[5], relief="solid", bd=0, bg="grey50",
                                  width=20, height=20, fg="grey55", activebackground="grey50",
                                  command=lambda: self.colors(6))
        self.green_color.grid(row=2, column=5, padx=2, pady=3)

        self.pink_color = Button(self.color_frame, image=self.color_container[6], relief="solid", bd=0, bg="grey50",
                                 width=20, height=20, fg="grey50", activebackground="grey50",
                                 command=lambda: self.colors(7))
        self.pink_color.grid(row=4, column=2, padx=2, pady=3)

        self.black_color = Button(self.color_frame, image=self.color_container[7], relief="solid", bd=0, bg="grey50",
                                  width=20, height=20, fg="grey50", activebackground="grey50",
                                  command=lambda: self.colors(8))
        self.black_color.grid(row=4, column=5, padx=2, pady=3)

        self.brown_color = Button(self.color_frame, image=self.color_container[8], relief="solid", bd=0, bg="grey50",
                                  width=20, height=20, fg="grey50", activebackground="grey50",
                                  command=lambda: self.colors(9))
        self.brown_color.grid(row=3, column=5, padx=2, pady=3)

        self.lightblue_color = Button(self.color_frame, image=self.color_container[9], relief="solid", bd=0,
                                      bg="grey50",
                                      width=20, height=20, fg="grey50", activebackground="grey50",
                                      command=lambda: self.colors(10))
        self.lightblue_color.grid(row=1, column=4, padx=2, pady=3)

        self.green_yellow_color = Button(self.color_frame, image=self.color_container[10], relief="solid", bd=0,
                                         bg="grey50",
                                         width=20, height=20, fg="grey50", activebackground="grey50",
                                         command=lambda: self.colors(11))
        self.green_yellow_color.grid(row=2, column=4, padx=2, pady=3)

        self.plum_color = Button(self.color_frame, image=self.color_container[11], relief="solid", bd=0, bg="grey50",
                                 width=20, height=20, fg="grey50", activebackground="grey50",
                                 command=lambda: self.colors(12))
        self.plum_color.grid(row=4, column=4, padx=2, pady=3)

        self.skin_color = Button(self.color_frame, image=self.color_container[12], relief="solid", bd=0, bg="grey50",
                                 width=20, height=20, fg="grey50", activebackground="grey50",
                                 command=lambda: self.colors(13))
        self.skin_color.grid(row=3, column=2, padx=2, pady=3)

        self.grey_color = Button(self.color_frame, image=self.color_container[13], relief="solid", bd=0, bg="grey50",
                                 width=20, height=20, fg="grey50", activebackground="grey50",
                                 command=lambda: self.colors(14))
        self.grey_color.grid(row=1, column=3, padx=2, pady=3)

        self.lightpink_color = Button(self.color_frame, image=self.color_container[14], relief="solid", bd=0,
                                      bg="grey50",
                                      width=20, height=20, fg="grey50", activebackground="grey50",
                                      command=lambda: self.colors(15))
        self.lightpink_color.grid(row=4, column=1, padx=2, pady=3)

        self.lightyellow_color = Button(self.color_frame, image=self.color_container[15], relief="solid", bd=0,
                                        bg="grey50", width=20, height=20,
                                        fg="grey50", activebackground="grey50", command=lambda: self.colors(16))
        self.lightyellow_color.grid(row=3, column=1, padx=2, pady=3)


if __name__ == '__main__':
    window = Tk()
    window.geometry("1346x700")
    window.maxsize(1366, 768)
    window.minsize(1346, 700)
    window.config(bg="grey11")

    Sketch(window)
    window.mainloop()
