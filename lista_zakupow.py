shopping_list = {
    "piekarnia" : ['chleb', 'pączek', 'bułki'],
    "warzywniak" : ['marchew', 'seler', 'rukola']
}

for key, items in shopping_list.items():
    print(f"Idę do {key.capitalize()} i kupuję tam {[item.capitalize() for item in items]}")