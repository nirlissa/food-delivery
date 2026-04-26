# ПРОГРАММА ДОСТАВКИ ЕДЫ
# Воронина Елизавета и Андриевская Кристина
# Группа: 1-ИАИТ-109

import json
import os

# ФАЙЛЫ ДЛЯ ХРАНЕНИЯ ДАННЫХ
MENU_FILE = "menu.txt"
ADDRESSES_FILE = "addresses.txt"
ORDERS_FILE = "orders.txt"

def load_menu():
    """Загружает меню из файла"""
    menu = []
    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 2:
                        menu.append([parts[0], int(parts[1])])
    else:
        # Меню по умолчанию
        menu = [
            ["Пицца Маргарита", 450],
            ["Пицца Пепперони", 550],
            ["Бургер", 350],
            ["Бургер Двойной", 450],
            ["Суши Филадельфия", 600],
            ["Суши Калифорния", 550],
            ["Картошка фри", 150],
            ["Наггетсы", 200],
            ["Кола", 100],
            ["Сок", 120]
        ]
        save_menu(menu)
    return menu

def save_menu(menu):
    """Сохраняет меню в файл"""
    with open(MENU_FILE, "w", encoding="utf-8") as f:
        for item in menu:
            f.write(f"{item[0]}|{item[1]}\n")
            
print("=" * 50)
print("ДОСТАВКА ЕДЫ")
print("=" * 50)

# МЕНЮ
menu = [
    ["Пицца Маргарита", 450],
    ["Пицца Пепперони", 550],
    ["Бургер", 350],
    ["Бургер Двойной", 450],
    ["Суши Филадельфия", 600],
    ["Суши Калифорния", 550],
    ["Картошка фри", 150],
    ["Наггетсы", 200],
    ["Кола", 100],
    ["Сок", 120]
]

# АДРЕСА
addresses = [
    "ул. Ленина, 1",
    "ул. Ленина, 5",
    "ул. Пушкина, 10",
    "ул. Гагарина, 3",
    "ул. Мира, 2"
]

# КОРЗИНА
cart = []

# ГЛАВНЫЙ ЦИКЛ
while True:
    print("\n" + "=" * 50)
    print("ГЛАВНОЕ МЕНЮ")
    print("=" * 50)
    print("1. Посмотреть меню")
    print("2. Корзина")
    print("3. О программе")
    print("4. Выход")
    print("=" * 50)
    
    choice = input("Выбери действие (1-4): ")
    
    # МЕНЮ
    if choice == "1":
        while True:
            print("\n" + "=" * 50)
            print("МЕНЮ")
            print("=" * 50)
            
            for i in range(len(menu)):
                print(f"{i+1}. {menu[i][0]} - {menu[i][1]} руб")
            
            print("0. Назад")
            print("=" * 50)
            
            food_choice = input("Введи номер блюда: ")
            
            if food_choice == "0":
                break
            
            if food_choice.isdigit():
                num = int(food_choice) - 1
                if 0 <= num < len(menu):
                    # Запрашиваем количество
                    quantity_input = input("Введи количество порций: ")
                    if quantity_input.isdigit() and int(quantity_input) > 0:
                        quantity = int(quantity_input)
                        item_name = menu[num][0]
                        item_price = menu[num][1]
                        # Добавляем как словарь с количеством
                        cart.append({
                            "name": item_name,
                            "price": item_price,
                            "quantity": quantity
                        })
                        print(f"{item_name} x{quantity} добавлено в корзину")
                    else:
                        print("Некорректное количество. Добавление отменено")
                else:
                    print("Нет такого блюда")
            else:
                print("Введи число")
    
    # КОРЗИНА
    elif choice == "2":
        while True:
            print("\n" + "=" * 50)
            print("КОРЗИНА")
            print("=" * 50)
            
            if len(cart) == 0:
                print("Корзина пуста")
            else:
                total = 0
                for i in range(len(cart)):
                    item = cart[i]
                    name = item["name"]
                    price = item["price"]
                    quantity = item["quantity"]
                    item_total = price * quantity
                    print(f"{i+1}. {name} - {price} руб x {quantity} = {item_total} руб")
                    total = total + item_total
                
                print("-" * 50)
                print(f"Сумма: {total} руб")
                
                if total >= 600:
                    print("Доставка бесплатно")
                    delivery = 0
                else:
                    delivery = 100
                    print(f"Доставка: {delivery} руб")
                    need = 600 - total
                    print(f"До бесплатной доставки {need} руб")
                
                print(f"ИТОГО: {total + delivery} руб")
            
            print("\nДЕЙСТВИЯ:")
            print("1. Оформить заказ")
            print("2. Очистить корзину")
            print("0. Назад")
            
            cart_action = input("Выбери действие: ")
            
            if cart_action == "1":
                if len(cart) == 0:
                    print("Корзина пуста")
                    input("Нажми Enter...")
                    continue
                
                print("\n" + "=" * 50)
                print("ОФОРМЛЕНИЕ ЗАКАЗА")
                print("=" * 50)
                
                name = input("Как тебя зовут? ")
                if name == "":
                    name = "Гость"
                
                print("\nАдреса:")
                for i in range(len(addresses)):
                    print(f"{i+1}. {addresses[i]}")
                
                while True:
                    addr_choice = input("Выбери номер адреса: ")
                    if addr_choice.isdigit():
                        addr_num = int(addr_choice) - 1
                        if addr_num >= 0 and addr_num < len(addresses):
                            address = addresses[addr_num]
                            break
                        else:
                            print("Нет такого адреса")
                    else:
                        print("Введи число")
                
                total = 0
                for item in cart:
                    total = total + (item["price"] * item["quantity"])
                
                if total >= 600:
                    delivery = 0
                else:
                    delivery = 100
                
                print("\n" + "=" * 50)
                print("ЗАКАЗ ПРИНЯТ")
                print("=" * 50)
                print(f"Имя: {name}")
                print(f"Адрес: {address}")
                print("-" * 50)
                print("Заказ:")
                for item in cart:
                    print(f"  • {item[0]}")
                print("-" * 50)
                print(f"Сумма: {total} руб")
                print(f"Доставка: {delivery} руб")
                print(f"ИТОГО: {total + delivery} руб")
                print("=" * 50)
                print("Спасибо за заказ")
                print("=" * 50)
                
                cart = []
                input("Нажми Enter для продолжения...")
            
            elif cart_action == "2":
                cart = []
                print("Корзина очищена")
                input("Нажми Enter...")
            
            elif cart_action == "0":
                break
    
    # О ПРОГРАММЕ
    elif choice == "3":
        print("\n" + "=" * 50)
        print("О ПРОГРАММЕ")
        print("=" * 50)
        print("Доставка еды")
        print("Версия: 1.0")
        print("\nРазработчики:")
        print("Воронина Елизавета - меню и корзина")
        print("Андриевская Кристина - заказы и интерфейс")
        print("\nГруппа: 1-ИАИТ-109")
        print("=" * 50)
        input("Нажми Enter для продолжения...")
    
    # ВЫХОД
    elif choice == "4":
        print("\nДо свидания")
        print("=" * 50)
        break
    
    else:
        print("Неверный выбор. Введи 1, 2, 3 или 4")
        input("Нажми Enter...")
