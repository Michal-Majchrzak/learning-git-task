shopping_list = {
    "piekarnia" : ['chleb', 'pączek', 'bułki'],
    "warzywniak" : ['marchew', 'seler', 'rukola']
}

for key, items in shopping_list.items():
    print(f"Idę do {key.capitalize()} i kupuję tam {[item.capitalize() for item in items]}")

print(f"Kupuję tam {sum([len(item[1]) for item in shopping_list.items()])} produktów.")