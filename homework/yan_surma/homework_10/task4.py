PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_list = PRICE_LIST.split()
items = price_list[::2]  # Получим список товаров
str_prices = price_list[1::2]  # Получим цены

prices = [int(price.replace('р', '')) for price in str_prices]  # Сгенерируем список с int ценами

price_dict = dict(zip(items, prices))
print(price_dict)

