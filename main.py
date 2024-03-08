from commands import load, add, showAll, showDate, delete, change

file_name = "notes.json"

notes = load(file_name)
id_counter = len(notes) + 1

info = ("""
        Для управления заметками используйте команды:
        'info' -   показывает доступные команды программы
        'all'  -   показывает все заметки
        'date' -   показывает все заметки, созданные в указанных датах
        'add' -    добавляет новую заметку
        'delete' - удаляет заметку с выбранным ID
        'change' - изменяет заметку
        'exit' -   выход из программы""")

while True:
    command = input("Введите одну из команд: info, all, date, add, delete, change, exit\n")

    match command:
        case "info": print(info)
        case "all":  showAll(notes)
        case "add":  
            add(notes, id_counter, file_name)
            id_counter += 1
        case "date": showDate(notes)
        case "delete": delete(notes, file_name)
        case "change": change(notes, file_name)
        case "exit":
            print("Работа с заметками прекращена.")
            break
        case _: print('Вы ввели неверную команду! Для списка команд обратитесь к "info"!')