def field(items, *args):
    assert len(args) > 0, "Необходимо передать хотя бы одно поле"

    if len(args) == 1:
        # Если одно поле, выдаем только значения
        for item in items:
            value = item.get(args[0])
            if value is not None:
                yield value
    else:
        # Если несколько полей, выдаем словари
        for item in items:
            result = {key: item.get(key) for key in args if item.get(key) is not None}
            if result:  # Пропускаем, если все поля были None
                yield result

if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    print(list(field(goods, 'title')))
    print(list(field(goods, 'title', 'price')))
