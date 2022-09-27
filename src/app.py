from number_processor import NumberProcessor

if __name__ == '__main__':
    processor = NumberProcessor([[1], [2], [3]])

    res = processor.execute()

    print(res)