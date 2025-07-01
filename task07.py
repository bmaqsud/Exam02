cart = {
  'non': {'price': 3000, 'quantity': 2},
  'sut': {'price': 8000, 'quantity': 1},
  'olma': {'price': 5000, 'quantity': 5}
}
total=0
for i in cart.values():
    total+=i['price'] * i['quantity']
print(f"umumiy summa: {total}")