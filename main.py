import json
import os
from datetime import datetime

notes_file = "notes.json"


def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, "r") as f:
            return json.load(f)
    return {}


def save_notes(notes):
    with open(notes_file, "w") as f:
        json.dump(notes, f, indent=4)


def add_note():
    notes = load_notes()
    note_id = input("Введите ID заметки: ")
    note_title = input("Введите название заметки: ")
    note_body = input("Введите текст заметки: ")
    note_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes[note_id] = {
        "title": note_title,
        "body": note_body,
        "date": note_date
    }
    save_notes(notes)
    print("Заметка успешно добавлена.")


def edit_note():
    notes = load_notes()
    note_id = input("Введите ID заметки, которую нужно изменить: ")
    if note_id in notes:
        note_title = input("Введите новое название заметки: ")
        note_body = input("Введите новый текст заметки: ")
        note_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notes[note_id]["title"] = note_title
        notes[note_id]["body"] = note_body
        notes[note_id]["date"] = note_date
        save_notes(notes)
        print("Заметка успешно изменена.")
    else:
        print("ID заметки не найден.")


def delete_note():
    notes = load_notes()
    note_id = input("Введите ID заметки, которую нужно удалить: ")
    if note_id in notes:
        del notes[note_id]
        save_notes(notes)
        print("Заметка успешно удалена.")
    else:
        print("ID заметки не найден.")


def list_notes():
    notes = load_notes()
    for note_id, note_info in notes.items():
        print(f"ID заметки: {note_id}")
        print(f"Заголовок: {note_info['title']}")
        print(f"Текст: {note_info['body']}")
        print(f"Дата: {note_info['date']}")
        print("----------------------")


def main():
    while True:
        print("1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Список заметок")
        print("5. Выход")

        choice = input("\nВведите номер команды: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            edit_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            list_notes()
        elif choice == "5":
            break
        else:
            print("Неверный номер. Пожалуйста, попробуйте еще раз.")


if __name__ == "__main__":
    main()