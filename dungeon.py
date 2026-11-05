"""Текстовая ролевая игра Подземелье: Соляные шахты с поддержкой сохранений и цветного интерфейса."""

import sys
import settings
import functions

# Вывод приветственного экрана (Практическая 3)
print(settings.FRAME)
print(f"   {settings.TITLE}   ")
print(settings.FRAME)
print()

# Загрузка JSON данных (Практическая 15)
saved_game = settings.load_game()
stats = {}
hero_name = ""

if saved_game:
    print(f"Обнаружено сохранение героя {saved_game['hero_name']} от {saved_game.get('save_time', 'неизвестно')}.")
    print("Загрузить этот прогресс? (да / нет)")
    user_input = input().lower().strip()
    if user_input in ["да", "д", "yes", "y"]:
        hero_name = saved_game["hero_name"]
        stats["hp"] = saved_game["hp"]
        stats["crystals"] = saved_game["crystals"]
        stats["inventory"] = saved_game["inventory"]
        print(f"\nС возвращением в игру, {hero_name}!")

if not stats:
    print("Как зовут героя?")
    hero_name = input().strip()
    if not hero_name:
        hero_name = "Безымянный Искатель"

    stats["hp"] = settings.INITIAL_STATS["hp"]
    stats["crystals"] = settings.INITIAL_STATS["crystals"]
    stats["inventory"] = list(settings.INITIAL_STATS["inventory"])

    print(f"\nДобро пожаловать, {hero_name}!")
    print("Ты входишь в древние соляные копи. Вокруг темно, а в воздухе стоит едкий запах соли.\n")

# Игровой цикл (Практическая 5)
while True:
    if stats["hp"] <= 0:
        print(settings.FRAME)
        print(f"Увы, {hero_name} исчерпал запас жизненных сил и остался в шахтах навечно...")
        print("ИГРА ОКОНЧЕНА.")
        print(settings.FRAME)
        break

    functions.show_status(hero_name, stats)

    print("Выберите действие:")
    print("1 - Осмотреться")
    print("2 - Идти вперёд (Возможен бой!)")
    print("3 - Отдохнуть")
    print("4 - Собрать кристаллы")
    print("5 - Выпить настойку")
    print("6 - Сохранить прогресс")
    print("7 - Покинуть шахты (Выход)")
    print()

    action = input().strip()
    print()

    if action == "1":
        functions.look_around(stats)
    elif action == "2":
        functions.go_forward(stats)
    elif action == "3":
        functions.rest(stats)
    elif action == "4":
        functions.gather_crystals(stats)
    elif action == "5":
        functions.use_item(stats)
    elif action == "6":
        settings.save_game(hero_name, stats)
    elif action == "7":
        print(settings.FRAME)
        print(f"Удачи в копях, {hero_name}! До новых встреч!")
        print(settings.FRAME)
        sys.exit()
    else:
        print("Неверный ввод. Внимательно смотрите на доступные номера действий.")

    print()
