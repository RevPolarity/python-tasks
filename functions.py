import random
import settings

# Выполнение Lib4: Безопасное подключение цветов на основе флага COLOR
if settings.COLOR:
    from colorama import Fore, Style

    COLOR_GREEN = Fore.GREEN + Style.BRIGHT
    COLOR_VICTORY = Fore.YELLOW + Style.BRIGHT  # Использование желтого цвета (Lib5)
    COLOR_RESET = Style.RESET_ALL
else:
    COLOR_GREEN = ""
    COLOR_VICTORY = ""
    COLOR_RESET = ""


def show_status(hero_name, stats):
    """Выводит статус персонажа. Строка состояния зеленая при COLOR (Lib4)."""
    print(settings.FRAME)
    formatted_name = hero_name.upper()

    status_text = f" Герой: {formatted_name} | Здоровье: {stats['hp']}% | Кристаллы: {stats['crystals']}"
    print(f"{COLOR_GREEN}{status_text}{COLOR_RESET}")

    inventory_list = ", ".join(stats["inventory"])
    print(f" Инвентарь: {inventory_list}")

    bonus = settings.calculate_crystal_bonus(stats["crystals"])
    print(f" Бонус к удаче от кристаллов: +{bonus}%")
    print(settings.FRAME)


def look_around(stats):
    """Ищет предметы, используя срезы и методы поиска в строках."""
    events = [
        "Тайник: Секретная 'Настойка' скрыта в щели.",
        "Тайник: Острый 'Обломок' лежит на каменном выступе.",
        "Впереди только соляные стены."
    ]
    chosen_event = random.choice(events)
    print(chosen_event)

    if chosen_event[:7] == "Тайник:":
        start_idx = chosen_event.find("'") + 1
        end_idx = chosen_event.rfind("'")
        item = chosen_event[start_idx:end_idx]

        if item not in stats["inventory"]:
            stats["inventory"].append(item)
            print(f"-> Вы нашли предмет: [{item}] и добавили его в инвентарь.")


def go_forward(stats):
    """Перемещение вперед со случайными событиями и боевой механикой (Lib5)."""
    chance = random.random()
    if chance < 0.3:
        damage = random.randint(15, 30)
        stats["hp"] -= damage
        print(f"Вы попали под обвал соляных плит! Получено {damage} урона.")
    elif chance < 0.6:
        print("Вы благополучно прошли вглубь следующего штрека шахты.")
    else:
        print("В темноте на вас нападает Слепой Крот-Шахтер! Начинается бой...")
        damage_received = random.randint(5, 15)
        stats["hp"] -= damage_received
        stats["crystals"] += 10

        # Вывод победы, покрашенный желтым цветом по требованию Lib5
        victory_text = f"Победа! Враг повержен. Вы получили {damage_received} урона, но добыли трофей: +10 кристаллов!"
        print(f"{COLOR_VICTORY}{victory_text}{COLOR_RESET}")


def rest(stats):
    """Восстановление здоровья."""
    if stats["hp"] >= 100:
        print("Вы полностью здоровы и не нуждаетесь в отдыхе.")
    else:
        heal = random.randint(20, 40)
        stats["hp"] = min(100, stats["hp"] + heal)
        print(f"Вы передохнули у соляного столба. Здоровье восстановлено на {heal}%.")


def gather_crystals(stats):
    """Сбор ресурсов."""
    if "Старая кирка" in stats["inventory"]:
        mined = random.randint(3, 7)
        stats["crystals"] += mined
        print(f"Размахивая киркой, вы добыли {mined} соляных кристаллов!")
    else:
        print("Без кирки вы не сможете отколоть крепкие кристаллы.")


def use_item(stats):
    """Использование предметов из инвентаря."""
    if "Настойка" in stats["inventory"]:
        stats["inventory"].remove("Настойка")
        stats["hp"] = min(100, stats["hp"] + 35)
        print("Вы выпили Настойку. Здоровье восстановилось на 35%!")
    else:
        print("В вашем инвентаре нет предметов для использования.")
