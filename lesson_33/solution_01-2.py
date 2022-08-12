"""
Дана база данных (в виде текстового файла) о продажах некоторого интернет-магазина.

Каждая строка входного файла представляет собой запись вида Покупатель, Товар, Количество, Стоимость, где:
Покупатель - имя покупателя (строка без пробелов),
товар - название товара (строка без пробелов),
количество - количество приобретенных единиц товара,
cтоимость - стоимость покупки.

1. Создайте список и выведите на экран всех покупателей, а для каждого покупателя подсчитайте общее количество
приобретенных им товаров и их стоимость.

2. Создайте список и выведите на экран все товары, а для каждого товара подсчитайте общее количество приобретенных
и их стоимость.
"""
import csv


def read_data():
    result = []
    f = open("data.txt", "r")
    for row in csv.reader(f):
        result.append({
            "user": row[0],
            "product": row[1],
            "count": int(row[2]),
            "cost": int(row[3]),
        })
    f.close()
    return result


def write_data(result, file_name):
    f = open(file_name, "w")
    writer = csv.writer(f)
    for user, value in result.items():
        writer.writerow([user, value["products_count"], value["products_cost"]])
    f.close()


if __name__ == "__main__":
    data = read_data()

    users = {}
    for current in data:
        user = current["user"]
        if user in users:
            users[user]["products_count"] += current["count"]
            users[user]["products_cost"] += current["cost"]
        else:
            users[user] = {
                "products_count": current["count"],
                "products_cost": current["cost"]
            }
    write_data(users, "users.csv")

    products = {}
    for current in data:
        product = current["product"]
        if product in products:
            products[product]["products_count"] += current["count"]
            products[product]["products_cost"] += current["cost"]
        else:
            products[product] = {
                "products_count": current["count"],
                "products_cost": current["cost"]
            }
    write_data(products, "products.csv")

    print(data)

