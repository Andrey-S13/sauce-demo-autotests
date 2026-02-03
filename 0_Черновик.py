def select_product_menu():
    """Выводит меню выбора товара и возвращает ключ товара и словарь"""
    products = {
        1: "Sauce Labs Backpack",
        2: "Sauce Labs Bike Light",
        3: "Sauce Labs Bolt T-Shirt",
        4: "Sauce Labs Fleece Jacket",
        5: "Sauce Labs Onesie",
        6: "Test.allTheThings() T-Shirt (Red)"
    }

    print("Приветствую тебя в нашем интернет-магазине")
    print("Выбери один из следующих товаров и укажи его номер:")

    for key, value in products.items():
        print(f"{key} - {value}")

    while True:  # Добавляем проверку ввода
        try:
            select_item = int(input("Введите номер товара: "))
            if select_item in products:
                # return select_item, products[select_item]  # Возвращаем ключ / значение
                print("-" * 20)
                print(f"Вы выбрали: {product_key} - {product_value}")
                print("-" * 20)
            else:
                print(f"Товара с номером {select_item} не существует. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите число!")

#
# product_key, product_value = select_product_menu()
# print("-" * 20)
# print(f"Вы выбрали: {product_key} - {product_value}")
# print("-" * 20)