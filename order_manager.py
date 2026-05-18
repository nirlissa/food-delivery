# РАБОТА С ЗАКАЗАМИ
# Андриевская Кристина
# Группа: 1-ИАИТ-109

from file_handlers import get_valid_choice, save_order

def display_addresses(addresses):
    """Показывает список адресов"""
    print("\nАдреса:")
    for i in range(len(addresses)):
        print(f"{i+1}. {addresses[i]}")

def select_address(addresses):
    """Выбор адреса доставки"""
    display_addresses(addresses)
    
    while True:
        addr_choice = get_valid_choice("Выбери номер адреса: ", len(addresses), allow_zero=False)
        return addresses[addr_choice - 1]

def create_order(cart, addresses, total, delivery):
    """Создает новый заказ"""
    print("\n" + "=" * 50)
    print("ОФОРМЛЕНИЕ ЗАКАЗА")
    print("=" * 50)
    
    customer_name = input("Как тебя зовут? ").strip()
    if customer_name == "":
        customer_name = "Гость"
    
    address = select_address(addresses)
    
    print("\n" + "=" * 50)
    print("ЗАКАЗ ПРИНЯТ")
    print("=" * 50)
    print(f"Имя: {customer_name}")
    print(f"Адрес: {address}")
    print("-" * 50)
    print("Заказ:")
    for item in cart:
        print(f"  • {item['name']} x{item['quantity']}")
    print("-" * 50)
    print(f"Сумма: {total} руб")
    print(f"Доставка: {delivery} руб")
    print(f"ИТОГО: {total + delivery} руб")
    print("=" * 50)
    print("Спасибо за заказ")
    print("=" * 50)
    
    order_data = {
        "name": customer_name,
        "address": address,
        "items": cart.copy(),
        "total": total,
        "delivery": delivery,
        "final_total": total + delivery
    }
    save_order(order_data)
    
    input("\nНажми Enter для продолжения...")
    return True
