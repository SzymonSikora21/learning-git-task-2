# Zadanie 1
shop_list = {
    "piekarnia": ['chleb', 'pączek', 'bułki'],
    "warzywniak": ['marchew', 'seler', 'rukola']
}

for shop, products in shop_list.items():
    products = [product.capitalize() for product in products]
    print(f"Idę do {shop.capitalize()} i kupuję tam {products}")

X = len(shop_list.get("piekarnia")) + len(shop_list.get("warzywniak"))
print(f"W sumie kupuję {X} produktów.")

# Zadanie 2
my_list = list(range(101))
divisible_by_5 = [numbers for numbers in my_list if numbers % 5 == 0]
squares = [number ** 2 for number in my_list if number % 5 == 0]
print(divisible_by_5)
print(squares)

my_list2 = list(range(0, 101, 5))
print(my_list2)