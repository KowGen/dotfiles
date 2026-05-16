#!/usr/bin/env python3

import datetime
import os
from pathlib import Path
import subprocess
from rich.console import Console

console = Console()

BASE_DIR = Path("/home/chyntemir/Документы/Obsidian\ Vault")
file_path = BASE_DIR / "diary.md"


def main_menu(): 
    os.system("clear")
    console.print(f"""
    [bold]=== ДНЕВНИК [purple](Obsidian)[/purple] ===[/bold]
    Файл: {file_path}
    --------------------------
    1 - insert mod
    2 - Список файлов в Vault
    3 - Редактировать в Neovim
    4 - Показать заголовки (Grep)
    0 - [red]Выйти[/red]
    --------------------------
    """, justify="center")
    
    try:
        return int(console.input("[yellow]Выберите режим:[/yellow] "))
    except ValueError:
        return -1

		
	
#это первый 1
def insert_mod():

	date_and_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

	# принимает дату и хештеги
	tags_input = list(input(f"{[date_and_time]} | Теги (через пробел): ").split())

	# для того чтобы на каждом отдельном хештеге был символ хештег
	for_save_tags = (f"### {date_and_time + " | Tags: " + " ".join([f"#{tag}" for tag in tags_input])}")

	note_mass = []
	
	while True:
		print("--- incert mod ( s! сохранить ) ---")
		note = input("> ")
		if note == "s!":
			break
		note_mass.append(note)
		
	note = "\n".join(note_mass)
	with open(file_path, "a", encoding="utf-8") as f:
        # запись в файл
		f.write(f"{for_save_tags}\n")
		f.write(f"{note} \n\n\n")

	input("\nНажми Enter, чтобы вернуться в меню...")




# это второй 2
def directory_files():

	os.system(f"ls {BASE_DIR}")
	#os.listdir("/home/chyntemir/Документы/Obsidian Vault/")
	input("\nНажми Enter, чтобы вернуться в меню...")

# это третий 3
def edit_file():
	#os.system(f"nvim + '{file_path}'")
	subprocess.run(["nvim", file_path])

# это четвёртный 4
# console = Console()

def name_data():
    # Мы используем тройные кавычки для меню. 
    # В Rich лучше выводить это через console.print
    console.print("""
    [bold blue]=== Показать заголовки ===[/bold blue]
    --------------------------
    1 - показать теги
    2 - показать все заголовки
    3 - найти конкретный тег
    0 - [red]Меню[/red]
    --------------------------
    """)
        
    try:
        # Используем твой объект console
        mod = int(console.input("[yellow]Выберите режим:[/yellow] "))
    except ValueError:
        console.print("[red]Ошибка: введите число![/red]")
        return -1

    if mod == 1:
        pass

    elif mod == 2:
        # Здесь была ошибка отступов - теперь они ровные
        subprocess.run(["grep", "^###", file_path])
        console.input("\n[dim]Нажми Enter, чтобы вернуться в меню...[/dim]")

    elif mod == 3:
        search_teg = console.input("Поиск тега (без [bold]# color[/bold]): ")
        # Ищем заголовок, содержащий нужный тег
        subprocess.run(["grep", "-i", f"#{search_teg}", file_path])
        console.input("\n[dim]Нажми Enter, чтобы вернуться в меню...[/dim]")

    elif mod == 0:
        return
        
    else:
        console.input("\nНажми Enter, чтобы вернуться в меню...")

# тут появляеться сам главный экарн

while True:

	mod = main_menu()
	if mod == 1:
		insert_mod()
			
	elif mod == 2:
		directory_files()
			
	elif mod == 3:
		edit_file()

	elif mod == 4:
		name_data()

	elif mod == 0:
		break
			
	else:
		print("\nERROR")
		input("Нажми Enter, чтобы вернуться в меню...")

