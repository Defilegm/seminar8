from modul import checkintinput
def start():
    message =[(1,'Добавление нового студента'),
    (2,'Добавление предмета'),
    (3,'Добавление оценки ученику по предмету'),
    (4,'Показ списка учеников (имена фамилия)'), 
    (5,'Показ листа оценок конкретного ученика'),
    (6,'Показ списка предметов'),
    (7,'Рандом журнал'),
    (8,'Вывести среднюю оценку ученика по предмету'),
    (9,'Вывести среднюю оценку по школе по предмету'),
    (10,'Вывод количества учеников претендующих на золотую медаль'),
    (11,'Импорт в файл'),
    (12,'Выход из программы')
    ]
    for elem in message:
        print(f'{elem[0]} {elem[1]}')
    choice = checkintinput('Выберите действите по номеру: ','Неверный ввод!')
    return choice

    


