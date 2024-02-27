class Flowers:

    def __init__(self, name, lifetime, color, stem_length, price):
        self.name = name
        self.lifetime = lifetime
        self.color = color
        self.stem_length = stem_length
        self.price = price


class Roses(Flowers):

    def __init__(self, name, lifetime, color, stem_length, price, have_thorns):
        super().__init__(name, lifetime, color, stem_length, price)
        self.have_thorns = have_thorns


class SunFlower(Flowers):

    def __init__(self, name, lifetime, color, stem_length, price, form):
        super().__init__(name, lifetime, color, stem_length, price)
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
        colors = [flower.color for flower in self.flower_bucket]
        colors.sort()
        return colors

    def sort_by_stem_length(self):
        stem_lengths = [flower.stem_length for flower in self.flower_bucket]
        stem_lengths.sort()
        return stem_lengths

    def sort_by_price(self):
        prices = [flower.price for flower in self.flower_bucket]
        prices.sort()
        return prices

    def search_by_name(self, name_value):
        names = [flower.name for flower in self.flower_bucket]
        if name_value in names:
            return True

    def search_by_lifetime(self, name_value):
        names = [flower.name for flower in self.flower_bucket]
        if name_value in names:
            return True


flower1 = Flowers('Lily', 5, 'Blue', 50, 20)
flower2 = Roses('Rose', 3, 'Black', 100, 50, True)
flower3 = SunFlower('Sunflower', 14, 'Yellow', 250, 10, 'Hybrids')
print(flower1)
print(flower2)
print(flower3)

bucket = BouquetOfFlowers()

bucket.add_flower(flower1)
bucket.add_flower(flower2)
bucket.add_flower(flower3)

print(bucket.calc_price_of_bucket())
print(bucket.average_lifetime())
print(bucket.sort_by_color())
print(bucket.sort_by_price())
print(bucket.sort_by_stem_length())
print(bucket.search_by_name('Sunflower'))
