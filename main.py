# ПРОГРАММА ДОСТАВКИ ЕДЫ
# Воронина Елизавета и Андриевская Кристина
# Группа: 1-ИАИТ-109

from file_handlers import load_menu, load_addresses, get_valid_choice
from menu_manager import add_to_cart
from cart_manager import cart_menu
from order_manager import create_order

def show_about():
    """Показывает информацию о программе"""
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

def main():
    """Главная функция программы"""
    print("=" * 50)
    print("ДОСТАВКА ЕДЫ")
    print("=" * 50)
    
    # ЗАГРУЗКА ДАННЫХ
    menu = load_menu()
    addresses = load_addresses()
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
        
        choice = get_valid_choice("Выбери действие (1-4): ", 4, allow_zero=False)
        
        # МЕНЮ
        if choice == 1:
            add_to_cart(menu, cart)
        
        # КОРЗИНА
        elif choice == 2:
            order_created = cart_menu(cart, addresses, create_order)
            if order_created:
                cart.clear()
        
        # О ПРОГРАММЕ
        elif choice == 3:
            show_about()
        
        # ВЫХОД
        elif choice == 4:
            print("\nДо свидания")
            print("=" * 50)
            break

if __name__ == "__main__":
    main()
