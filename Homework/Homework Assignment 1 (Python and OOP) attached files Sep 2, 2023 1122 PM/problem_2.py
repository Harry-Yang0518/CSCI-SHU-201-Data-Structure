class IterableIterator:
    def __init__(self):
        self.limit = 20
        self.index = 0

    def __len__(self):
        return self.limit

    def __getitem__(self, idx):
        return (idx % self.limit) + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > self.limit:
            self.index = 1
        return self.index

def main():
    my_obj = IterableIterator()
    my_it = iter(my_obj)
    print(my_obj[41])  # Output: 2
    print(next(my_it), next(my_it), next(my_it), next(my_it))  # Output: 1 2 3 4


if __name__ == '__main__':
    main()