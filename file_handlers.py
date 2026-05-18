# РАБОТА С ФАЙЛАМИ
# Воронина Елизавета и Андриевская Кристина
# Группа: 1-ИАИТ-109

import os
import json
from constants import MENU_FILE, ADDRESSES_FILE, ORDERS_FILE, DEFAULT_MENU, DEFAULT_ADDRESSES

def load_menu():
    """Загружает меню из файла"""
    menu = []
    if os.path.exists(MENU_FILE):
        try:
            with open(MENU_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        parts = line.split("|")
                        if len(parts) == 2:
                            menu.append([parts[0], int(parts[1])])
        except (IOError, ValueError) as e:
            print(f"Ошибка при загрузке меню: {e}")
            return DEFAULT_MENU.copy()
    else:
        menu = DEFAULT_MENU.copy()
        save_menu(menu)
    return menu

def save_menu(menu):
    """Сохраняет меню в файл"""
    try:
        with open(MENU_FILE, "w", encoding="utf-8") as f:
            for item in menu:
                f.write(f"{item[0]}|{item[1]}\n")
    except IOError as e:
        print(f"Ошибка при сохранении меню: {e}")

def load_addresses():
    """Загружает адреса из файла"""
    addresses = []
    if os.path.exists(ADDRESSES_FILE):
        try:
            with open(ADDRESSES_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        addresses.append(line)
        except IOError as e:
            print(f"Ошибка при загрузке адресов: {e}")
            return DEFAULT_ADDRESSES.copy()
    else:
        addresses = DEFAULT_ADDRESSES.copy()
        save_addresses(addresses)
    return addresses

def save_addresses(addresses):
    """Сохраняет адреса в файл"""
    try:
        with open(ADDRESSES_FILE, "w", encoding="utf-8") as f:
            for addr in addresses:
                f.write(addr + "\n")
    except IOError as e:
        print(f"Ошибка при сохранении адресов: {e}")

def save_order(order_data):
    """Сохраняет заказ в файл"""
    try:
        with open(ORDERS_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(order_data, ensure_ascii=False) + "\n")
    except IOError as e:
        print(f"Ошибка при сохранении заказа: {e}")

def get_valid_number_input(prompt, allow_zero=True):
    """Безопасный ввод числа"""
    while True:
        user_input = input(prompt)
        if user_input == "":
            print("Пожалуйста, введите число")
            continue
        if user_input.isdigit():
            num = int(user_input)
            if allow_zero and num == 0:
                return num
            if num > 0:
                return num
            else:
                print("Число должно быть больше 0")
        else:
            print("Пожалуйста, введите только цифры")

def get_valid_choice(prompt, max_choice, allow_zero=True):
    """Безопасный выбор пункта меню"""
    while True:
        user_input = input(prompt)
        if user_input == "":
            print("Пожалуйста, введите число")
            continue
        if user_input.isdigit():
            num = int(user_input)
            if allow_zero and num == 0:
                return num
            if 1 <= num <= max_choice:
                return num
            else:
                print(f"Пожалуйста, выберите число от 1 до {max_choice}")
        else:
            print("Пожалуйста, введите только цифры")
