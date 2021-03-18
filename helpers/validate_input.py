def validate_data_type(value):
    while True:
        try:
            data = float(value)
            break
        except ValueError:
            print('Invalid data type')

    print('Data type is valid')


def validate_list(values):
    if values == []:
        print('List is empty')
