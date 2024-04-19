# Поведенческие модели ПО

## Диаграммы состояний

### Выбор цвета

![Pal diagram](https://github.com/UnVeh/reposit/blob/master/diagrams/pal.png)

Эта диаграмма описывает процесс выбора цвета в приложении для рисования:
1. Ожидание действия: Начальное состояние, ожидание действия пользователя.
2. Выбор цвета: Пользователь нажимает на цвет во встроенной в палитре, выбирая его. Затем меняется цвет инструмента.
3. Нажатие на иконку палитры: Пользователь нажимает на иконку палитры для открытия окна выбора цвета.
4. Выбор цвета в палитре: Пользователь выбрает цвет, нажав на него в палитре.
5. Отмена выбора цвета: Если пользователь решает отменить выбор цвета, процесс завершается.
6. Подтверждение выбора цвета: Если пользователь подтверждает выбранный цвет, процесс переходит к следующему шагу.
7. Инструмент поменял цвет: Цвет инструмента изменяется на выбранный пользователем цвет.
8. Завершение: Завершающее состояние, когда процесс завершен.

[Код](https://github.com/UnVeh/reposit/blob/master/diagrams/state_pal.puml)

### Использование фигуры

![F diagram](https://github.com/UnVeh/reposit/blob/master/diagrams/figure.png)

Эта диаграмма описывает процесс создания и манипулирования фигурами в приложении для рисования:

1. Ожидание выбора фигуры: Начальное состояние, ожидание действия пользователя.
2. Выбор фигуры: Пользователь выбирает фигуру для создания.
3. Наведение курсора на холст: Пользователь перемещает курсор по холсту.
4. Нажатие на кнопку: Пользователь нажимает на кнопку мыши для начала создания фигуры.
5. Далее выбор:
	a) Потянуть курсор в одну из сторон: Пользователь удерживает кнопку мыши и перемещает курсор для определения размеров или формы фигуры.
	Фигура меняет форму: Если пользователь желает изменить форму фигуры, процесс продолжается.
	б) Отпустить кнопку: Пользователь отпускает кнопку мыши после завершения формирования фигуры.
	Фигура на холсте приняла статическое положение: Фигура на холсте принимает конечную статическую форму после отпускания кнопки мыши.
6. Завершение : Завершающее состояние, когда процесс создания фигуры завершен.

[Код](https://github.com/UnVeh/reposit/blob/master/diagrams/state_figure.puml)

### Заливка

![Fill diagram](https://github.com/UnVeh/reposit/blob/master/diagrams/fill.png)

Эта диаграмма описывает процесс заливки объектов или холста определенным цветом в приложении для рисования:

1. Ожидание выбора инструмента: Начальное состояние, ожидание действия пользователя.
2. Выбор инструмента заливки: Пользователь выбирает инструмент "заливка".
3. Наведение курсора на холст: Пользователь перемещает курсор по холсту.
4. Нажатие на кнопку: Пользователь нажимает на кнопку мыши для начала процесса заливки.
5. Объект залился цветом: Если курсор находится над объектом, то объект заливается выбранным цветом.
6. Холст залился цветом: Если курсор находится на холсте вне объектов, то весь холст заливается выбранным цветом.
7. Произошла заливка: Процесс заливки завершается.
8. Завершение: Завершающее состояние, когда процесс заливки завершен.Эта диаграмма описывает процесс заливки объектов или холста определенным цветом в приложении для рисования:

[Код](https://github.com/UnVeh/reposit/blob/master/diagrams/state_fill.puml)

## Диаграммы последовательности

### Использование ластика

![Er diagram](https://github.com/UnVeh/reposit/blob/master/diagrams/S_Er.png)

Эта диаграмма описывает процесс использования ластика для стирания части рисунка на холсте:
1. (Start drawing): Запуск приложения.
2. Создание нового холста (CreateNewCanvas()): Приложение создает новый холст для рисования.
3. Холст создан (Canvas created): Приложение сообщает пользователю о создании холста.
4. Выбор ластика (ChooseEraser()): Пользователь выбирает инструмент ластика для стирания рисунка.
5. Ластик выбран (EraserIsChosen()): Приложение получает информацию о выборе пользователем ластика.
6. Изменение формы курсора (CursorChangeShape()): Приложение изменяет форму курсора, чтобы сообщить пользователю о выборе ластика.
7. Стирание (Erasing(shape)): Пользователь использует ластик для стирания части рисунка на холсте.
8. Добавление области стирания (AddEraseArea(shape)): Приложение добавляет информацию об области, которую пользователь стер на холсте.
9. Завершение процесса: После завершения стирания процесс завершается.

[Код](https://github.com/UnVeh/reposit/blob/master/diagrams/S_Er.puml)

### Использование фигур

![F diagram](https://github.com/UnVeh/reposit/blob/master/diagrams/S_figure.png)

Эта диаграмма описывает процесс создания нового холста и рисования выбранной фигуры:
1. (Start drawing): Запуск приложения.
2. Создание нового холста (CreateNewCanvas()): Приложение создает новый холст для рисования.
3. Холст создан (Canvas created): Приложение сообщает пользователю о создании холста.
4. Выбор фигуры (ChooseFigure()): Пользователь выбирает фигуру для рисования.
5. Фигура выбрана (FigureIsChosen()): Приложение получает информацию о выбранной пользователем фигуре.
6. Изменение формы курсора (CursorChangeShape()): Приложение меняет форму курсора, чтобы сообщить пользователю о выборе фигуры.
7. Рисование фигуры (DrawFigure(shape)): Пользователь рисует выбранную фигуру на холсте.
8. Отображение фигуры (ShowFigure(shape)): Приложение отображает на холсте нарисованную пользователем фигуру.
9. Завершение процесса: После завершения рисования фигуры и ее отображения на холсте процесс завершается.

[Код](https://github.com/UnVeh/reposit/blob/master/diagrams/S_figure.puml)

### Заливка

![Fill diagram](https://github.com/UnVeh/reposit/blob/master/diagrams/S_fill.png)

Эта диаграмма описывает процесс использования инструмента заливки для заполнения определенной области на холсте:
1. (Start drawing): Запуск приложения.
2. Создание нового холста (CreateNewCanvas()): Приложение создает новый холст для рисования.
3. Холст создан (Canvas created): Приложение сообщает пользователю о создании холста.
4. Выбор инструмента заливки (ChooseFill()): Пользователь выбирает инструмент заливки для заполнения области на холсте.
5. Инструмент заливки выбран (FillisChosen()): Приложение получает информацию о выборе пользователем инструмента заливки.
6. Изменение формы курсора (CursorChangeShape()): Приложение изменяет форму курсора, чтобы сообщить пользователю о выборе заливки
7. Клик по области на холсте (ClickOnArea): Пользователь кликает по области на холсте, которую хочет заполнить.
8. Отображение области заполнения (ShowFillArea()): Приложение показывает пользователю область, которая заполнилась выбранным цветом.
9. Завершение процесса: После отображения области для заполнения процесс завершается.

[Код](https://github.com/UnVeh/reposit/blob/master/diagrams/S_fill.puml)
