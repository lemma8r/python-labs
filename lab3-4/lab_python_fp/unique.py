class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.seen = set()

    def __next__(self):
        while True:
            item = next(self.items)
            # Строки приводим к нижнему регистру, если нужно
            check_item = item.lower() if self.ignore_case and isinstance(item, str) else item

            if check_item not in self.seen:
                self.seen.add(check_item)
                return item

    def __iter__(self):
        return self

if __name__ == '__main__':
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(list(Unique(data1)))

    data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(list(Unique(data2)))
    print(list(Unique(data2, ignore_case=True)))
