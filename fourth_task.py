


import csv

def read_csv(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({
                'product_id': int(row['product_id']),
                'name': row['name'],
                'price': float(row['price']),
                'quantity': int(row['quantity']),
                'category': row['category'],
                'description': row['description'],
                'production_date': row['production_date'],
                #'expiration_date': row['expiration_date'],
                'rating': float(row['rating']),
                'status': row['status'],
            })
    return data

data = read_csv(r"E:\66\fourth_task.txt")

size = len(data)
avg_rating = 0
max_rating = data[0]['rating']
min_quantity = data[0]['quantity']

filtered_data = []

for item in data:
    avg_rating += item['rating']
    if max_rating < item['rating']:
        max_rating = item['rating']

    if min_quantity > item['quantity']:
        min_quantity = item['quantity']

    if item['status'] == 'New':
        filtered_data.append(item)

avg_rating /= size

with open("forth_task_1.txt", "w", encoding="utf-8") as f:
    f.write(f"Средний рейтинг: {avg_rating}\n")
    f.write(f"Максимальный рейтинг: {max_rating}\n")
    f.write(f"Минимальное количество: {min_quantity}\n")

with open("forth_task_2.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, filtered_data[0].keys())
    writer.writeheader()
    for row in filtered_data:
        writer.writerow(row)