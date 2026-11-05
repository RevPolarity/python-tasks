import json
import os
import datetime
import math

# Константы оформления
FRAME = "=" * 45
TITLE = "ПОДЗЕМЕЛЬЕ: СОЛЯНЫЕ ШАХТЫ"

# =====================================================================
# ВЫПОЛНЕНИЕ Lib5: Документирование неиспользованных констант по ТЗ
# Три цвета Fore: Fore.YELLOW (использован для победы), Fore.MAGENTA, Fore.WHITE
# Две константы Style: Style.DIM, Style.NORMAL
# =====================================================================

# Выполнение Lib4: Безопасный try-import импорт colorama
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLOR = True
except ImportError:
    COLOR = False

# Стартовый словарь состояния игрока
INITIAL_STATS = {
    "hp": 100,
    "crystals": 0,
    "inventory": ["Факел", "Старая кирка"]
}

def get_current_time():
    """Возвращает текущую дату и время."""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def calculate_crystal_bonus(crystals):
    """Рассчитывает логарифмический бонус к удаче."""
    if crystals > 0:
        return round(math.log(crystals, 2) * 5, 2)
    return 0

def save_game(hero_name, stats):
    """Сохранение структуры данных в файл JSON."""
    data = {
        "hero_name": hero_name,
        "hp": stats["hp"],
        "crystals": stats["crystals"],
        "inventory": stats["inventory"],
        "save_time": get_current_time()
    }
    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("\n~ Прогресс успешно зафиксирован в save.json! ~")

def load_game():
    """Чтение структуры данных из JSON."""
    if os.path.exists("save.json"):
        try:
            with open("save.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, PermissionError):
            print("Ошибка чтения файла сохранения. Начинаем новую игру.")
            return None
    return None
