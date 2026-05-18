# РАБОТА С МЕНЮ
# Воронина Елизавета
# Группа: 1-ИАИТ-109

from file_handlers import get_valid_choice, get_valid_number_input

def display_menu(menu):
    """Показывает меню"""
    print("\n" + "=" * 50)
    print("МЕНЮ")
    print("=" * 50)
    
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i][0]} - {menu[i][1]} руб")
    
    print("0. Назад")
    print("=" * 50)

def add_to_cart(menu, cart):
    """Добавляет блюдо в корзину"""
    while True:
        display_menu(menu)
        
        food_choice = get_valid_choice("Введи номер блюда: ", len(menu), allow_zero=True)
        
        if food_choice == 0:
            break
        
        num = food_choice - 1
        item_name = menu[num][0]
        item_price = menu[num][1]
        
        # Запрашиваем количество
        quantity = get_valid_number_input("Введи количество порций: ")
        
        # Добавляем как словарь с количеством
        cart.append({
            "name": item_name,
            "price": item_price,
            "quantity": quantity
        })
        print(f"{item_name} x{quantity} добавлено в корзину")
        print()
      
