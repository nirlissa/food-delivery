# РАБОТА С КОРЗИНОЙ
# Воронина Елизавета
# Группа: 1-ИАИТ-109

from constants import FREE_DELIVERY_THRESHOLD, DELIVERY_COST
from file_handlers import get_valid_choice

def calculate_totals(cart):
    """Рассчитывает суммы заказа"""
    total = 0
    for item in cart:
        total = total + (item["price"] * item["quantity"])
    
    if total >= FREE_DELIVERY_THRESHOLD:
        delivery = 0
    else:
        delivery = DELIVERY_COST
    
    return total, delivery

def display_cart(cart):
    """Показывает содержимое корзины"""
    print("\n" + "=" * 50)
    print("КОРЗИНА")
    print("=" * 50)
    
    if len(cart) == 0:
        print("Корзина пуста")
        return None, None
    
    for i in range(len(cart)):
        item = cart[i]
        name = item["name"]
        price = item["price"]
        quantity = item["quantity"]
        item_total = price * quantity
        print(f"{i+1}. {name} - {price} руб x {quantity} = {item_total} руб")
    
    total, delivery = calculate_totals(cart)
    
    print("-" * 50)
    print(f"Сумма: {total} руб")
    
    if delivery == 0:
        print("Доставка бесплатно")
    else:
        print(f"Доставка: {delivery} руб")
        need = FREE_DELIVERY_THRESHOLD - total
        print(f"До бесплатной доставки не хватает {need} руб")
    
    print(f"ИТОГО: {total + delivery} руб")
    
    return total, delivery

def cart_menu(cart, addresses, order_callback):
    """Меню управления корзиной"""
    while True:
        total, delivery = display_cart(cart)
        
        print("\nДЕЙСТВИЯ:")
        print("1. Оформить заказ")
        print("2. Очистить корзину")
        print("0. Назад")
        
        cart_action = get_valid_choice("Выбери действие: ", 2, allow_zero=True)
        
        if cart_action == 1:
            if len(cart) == 0:
                print("Корзина пуста")
                input("Нажми Enter...")
                continue
            
            result = order_callback(cart, addresses, total, delivery)
            if result:  # Если заказ оформлен успешно
                return True  # Очищаем корзину
                
        elif cart_action == 2:
            cart.clear()
            print("Корзина очищена")
            input("Нажми Enter...")
        
        elif cart_action == 0:
            break
    
    return False
