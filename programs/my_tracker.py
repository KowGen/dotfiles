#!/usr/bin/env python3
import datetime
import os

DIARY_FILE = "diary.md"

def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def parse_entries():
    """Разбирает файл на список записей (словари)."""
    if not os.path.exists(DIARY_FILE):
        return []
    
    with open(DIARY_FILE, "r", encoding="utf-8") as f:
        content = f.read().strip()
    
    if not content:
        return []

    # Разделяем файл по заголовкам ##
    raw_sections = content.split("\n## ")
    entries = []
    
    for section in raw_sections:
        if not section: continue
        # Очищаем от возможных остатков ## в начале
        section = section.lstrip("## ").strip()
        lines = section.split("\n")
        header = lines[0] # Это строка "Дата | Tags: #теги"
        body = "\n".join(lines[1:]) # Все остальное — текст заметки
        
        entries.append({"header": header, "body": body})
    return entries

def save_all(entries):
    """Перезаписывает файл всеми записями."""
    with open(DIARY_FILE, "w", encoding="utf-8") as f:
        for e in entries:
            f.write(f"## {e['header']}\n{e['body']}\n\n")

def insert_mode():
    print("\n--- НОВАЯ ЗАПИСЬ ---")
    tags_input = input("Tags (через пробел): ").strip()
    content = input("> ").strip()
    
    if not content:
        print("Ошибка: Пустая заметка!")
        return

    tags = " ".join([f"#{t.strip()}" for t in tags_input.split() if t.strip()])
    header = f"{get_timestamp()} | Tags: {tags}"
    
    entries = parse_entries()
    entries.append({"header": header, "body": content})
    save_all(entries)
    print("✓ Сохранено!")

def search_mode():
    query = input("Поиск (текст или тег): ").lower()
    entries = parse_entries()
    found = False
    for e in entries:
        if query in e['header'].lower() or query in e['body'].lower():
            print(f"\n## {e['header']}\n{e['body']}")
            found = True
    if not found: print("Ничего не найдено.")

def edit_mode():
    entries = parse_entries()
    if not entries:
        print("Файл пуст.")
        return

    for i, e in enumerate(entries):
        print(f"[{i}] {e['header']}")
    
    try:
        idx = int(input("\nНомер записи для редактирования: "))
        print(f"Старый текст: {entries[idx]['body']}")
        new_content = input("Новый текст (Enter чтобы оставить): ").strip()
        if new_content:
            entries[idx]['body'] = new_content
            save_all(entries)
            print("✓ Обновлено!")
    except (ValueError, IndexError):
        print("Ошибка: неверный номер.")

def filter_by_date():
    date_query = input("Введите дату (ГГГГ-ММ-ДД): ")
    entries = parse_entries()
    for e in entries:
        if date_query in e['header']:
            print(f"\n## {e['header']}\n{e['body']}")

def main_menu():
    while True:
        print(f"\n{'='*20}")
        print("   DIARY MVP 2.0")
        print(f"{'='*20}")
        print("1. Insert (Добавить)")
        print("2. Search (Поиск)")
        print("3. Edit (Редактировать)")
        print("4. Filter by Date (По дате)")
        print("5. List All (Показать всё)")
        print("0. Exit")
        
        choice = input("\nВыбор: ")
        
        if choice == '1': insert_mode()
        elif choice == '2': search_mode()
        elif choice == '3': edit_mode()
        elif choice == '4': filter_by_date()
        elif choice == '5':
            for e in parse_entries(): print(f"\n## {e['header']}\n{e['body']}")
        elif choice == '0': break
        else: print("Неверный ввод.")

if __name__ == "__main__":
    main_menu()
