shopping_list = {
    "piekarnia" : ['chleb', 'pączek', 'bułki'],
    "warzywniak" : ['marchew', 'seler', 'rukola']
}

for key, items in shopping_list.items():
    print(f"Idę do {key} i kupuję tam {items}")