class Flowers:

    def __init__(self, name, lifetime, color, stem_length, price):
        self.name = name
        self.lifetime = lifetime
        self.color = color
        self.stem_length = stem_length
        self.price = price


class Roses(Flowers):

    def __init__(self, lifetime, color, stem_length, price, have_thorns):
        super().__init__('Rose', lifetime, color, stem_length, price)
        self.have_thorns = have_thorns


class SunFlower(Flowers):

    def __init__(self, lifetime, color, stem_length, price, form):
        super().__init__('Sunflower', lifetime, color, stem_length, price)
        self.form = form


class BouquetOfFlowers:
    def __init__(self):
        self.flower_bucket = []

    def add_flower(self, flower):
        self.flower_bucket.append(flower)

    def calc_price_of_bucket(self):
        flower_price = [flower.price for flower in self.flower_bucket]
        result = sum(flower_price) / len(flower_price)
        return round(result)

    def average_lifetime(self):
        average_lifetime = [flower.lifetime for flower in self.flower_bucket]
        result = sum(average_lifetime) / len(average_lifetime)
        return round(result, 2)

    def sort_by_color(self):
        sorted_by_color = sorted(self.flower_bucket, key=lambda flower: flower.color)
        return f'Sort flowers by color: {sorted_by_color}'

    def sort_by_stem_length(self):
        sorted_by_stem_length = sorted(self.flower_bucket, key=lambda flower: flower.stem_length)
        return f'Sort flowers stem length: {sorted_by_stem_length}'

    def sort_by_price(self):
        sorted_by_price = sorted(self.flower_bucket, key=lambda flower: flower.price)
        return f'Sort flowers by price: {sorted_by_price}'

    def search_by_name(self, name_value):
        for flower in self.flower_bucket:
            if name_value == flower.name:
                return f'Name: {flower.name}, flower: {flower}'

    def search_by_color(self, color_value):
        for flower in self.flower_bucket:
            if color_value == flower.color:
                return f'Color: {flower.color}, flower: {flower}'

    def search_by_lifetime(self, lifetime_value):
        for flower in self.flower_bucket:
            if lifetime_value == flower.lifetime:
                return f'Lifetime: {flower.lifetime}, flower: {flower}'


flower1 = Flowers('Lily', 5, 'Blue', 50, 20)
flower2 = Roses(3, 'Black', 100, 50, True)
flower3 = SunFlower(14, 'Yellow', 250, 10, 'Hybrids')

bucket_of_flowers = BouquetOfFlowers()

bucket_of_flowers.add_flower(flower1)
bucket_of_flowers.add_flower(flower2)
bucket_of_flowers.add_flower(flower3)
print('Search by name')
print(bucket_of_flowers.search_by_name('Lily'))
print(bucket_of_flowers.search_by_name('Rose'))
print(bucket_of_flowers.search_by_name('Sunflower'))
print('Search by lifetime')
print(bucket_of_flowers.search_by_lifetime(5))
print(bucket_of_flowers.search_by_lifetime(3))
print(bucket_of_flowers.search_by_lifetime(14))
print('Search by color')
print(bucket_of_flowers.search_by_color('Blue'))
print(bucket_of_flowers.search_by_color('Black'))
print(bucket_of_flowers.search_by_color('Yellow'))
print('Sort')
print(bucket_of_flowers.sort_by_color())
print(bucket_of_flowers.sort_by_stem_length())
print(bucket_of_flowers.sort_by_price())
