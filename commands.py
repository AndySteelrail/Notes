import json
import time


def save(notes, file_name):
    with open(file_name, "w", encoding = "utf-8") as doc:
        doc.write(json.dumps(notes, ensure_ascii = False))

def load(file_name):
    try:
        with open(file_name, "r", encoding = "utf-8") as doc:
            notes = json.load(doc)
        print("Заметки загружены\n")
        save(notes, file_name)
        return notes
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Ошибка при загрузке файла JSON. Файл поврежден или имеет неверный формат.")
        return {}
    
def showAll(notes):
    if(notes):
        print("Ваши заметки:")
        for id, data in notes.items():
            print(f"№ {data.get('id', 'N/A')}; {data.get('title_note', 'N/A')}; Дата: {data.get('current_date', 'N/A')}")
        note_id = input("Хотите открыть свою заметку? Введите ID. Хотите назад? Введите \"no\": ")
        if note_id.lower() != "no":
            show_note_body(notes, note_id)
    else:
        print("У вас нет заметок.")

def showDate(notes):
    if(notes):
        print("Введите диапазон дат, чтобы отфильтровать заметки:")
        start_date = input("Введите начальную дату (формат: ДД-ММ-ГГГГ): ")
        end_date = input("Введите конечную дату (формат: ДД-ММ-ГГГГ): ")

        try:
            start_time = time.strptime(start_date, "%d-%m-%Y")
            end_date = time.strptime(end_date, "%d-%m-%Y")
            if end_date < start_time:
                print("Ошибка: Начальная дата позже конечной даты.")
                return
        except ValueError:
            print("Ошибка: Неверный формат даты.")
            return

        print("Ваши заметки:")
        for id, data in notes.items():
            note_data = time.strptime(data.get('current_date'), "%a %b %d %H:%M:%S %Y")
            if start_time <= note_data <= end_date:
                print(f"№ {data.get('id', 'N/A')};"
                      f" {data.get('title_note', 'N/A')};"
                      f" Дата: {data.get('current_date', 'N/A')}")

        note_id = input("Хотите открыть заметку? Введите ID. Для возвращения назад введите \"no\": ")
        if note_id.lower() != "no":
            show_note_body(notes, note_id)
    else:
        print("У вас нет заметок.")

def show_note_body(notes, note_id):
    try:
        if note_id in notes:
            print(f"Заметка № {note_id}: {notes[note_id]['title_note']}")
            print(notes[note_id]['body_note'])
            print()
        else:
            print("Заметка с таким ID не найдена.\n")
    except ValueError:
        print("Неверный ввод.\n")

def add(notes, id_counter, file_name):
    title_note = input("Введите заголовок заметки: ")
    body_note = input("Введите свою заметку:\n")
    current_date = time.ctime(time.time())

    entry_id = str(id_counter)
    for key, value in notes.items():
        if 'id' in value and value['id'] == id_counter:
            entry_id = str(id_counter + 1)

    notes[entry_id] = {
        'id': entry_id, 
        'title_note': title_note, 
        'body_note': body_note, 
        'current_date': current_date}
    save(notes, file_name)

def delete(notes, file_name):
    if (notes):
        note_id = input("Введите ID удаляемой заметки: ")
        try:
            if note_id in notes:
                del notes[note_id]
                print("Ваша заметка была удалена.\n")
                save(notes, file_name)
            else:
                print("Заметка с таким ID не была найдена.\n")
        except ValueError:
            print("Неверный ввод. Введите ID заметки.")
    else:
        print("Прежде чем удалить, нужно создать заметку. Заметок нет.")

def change(notes, file_name):
    if (notes):
        note_id = input("Введите ID изменяемой заметки: ")
        try:
            if note_id in notes:
                notes[note_id]['title_note'] = input("Введите новый заголовок своей заметки: ")
                notes[note_id]['body_note'] = input("Введите свою новую заметку:\n")
                notes[note_id]['current_date'] = time.ctime(time.time())
                print("Заметка успешно изменена.\n")
                save(notes, file_name)
            else:
                print("Заметки с таким ID не существует.\n")
        except ValueError:
            print("Неверный ввод. Введите ID заметки.")
    else:
        print("Нет ни одной заметки. Изменять нечего")