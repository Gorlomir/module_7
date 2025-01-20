import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.products = []
        self.file_name = 'products.txt'

    def load_products_from_file(self):
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    parts = line.strip().split(', ')
                    if len(parts) == 3:
                        self.products.append(Product(parts[0], float(parts[1]), parts[2]))
        except FileNotFoundError:
            pass

    def save_products_to_file(self):
        with open(self.file_name, 'w') as file:
            for product in self.products:
                file.write(f"{product}\n")

    def add(self, *products):
        for product in products:
            name = product.name
            category = product.category
            weight = product.weight

            existing_product = next((p for p in self.products if p.name == name and p.category == category), None)

            if existing_product:
                existing_weight = existing_product.weight
                new_weight = existing_weight + weight
                print(f"Продукт {name} уже был в магазине, его общий вес теперь равен {new_weight:.1f}")
            else:
                self.products.append(product)

        self.save_products_to_file()

    def get_products(self):
        return pprint.pformat([str(product) for product in self.products])

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())
