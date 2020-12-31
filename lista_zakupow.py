shopping_list = {
    "piekarnia" : ['chleb', 'pączek', 'bułki'],
    "warzywniak" : ['marchew', 'seler', 'rukola']
}

items_counter = 0
for key, items in shopping_list.items():
    print(f"Idę do {key.capitalize()} i kupuję tam {[item.capitalize() for item in items]}")
    items_counter += len(items)

print(f"Kupuję tam {items_counter} produktów.")
print("Pozdrowienia!!!")