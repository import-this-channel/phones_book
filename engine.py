def create_number(name, number, book):
    book.update({name: number})
    return book

def update_number(name, number, book):
    book[name] = number
    return book

def delete_number(name, book):
    book.remove(name)
    return book

def get_data():
    action = input('action?')
    input_name = input("name:")
    input_number = input("number:")
    return input_name, input_number, action


def make_action(data, book):
    input_name, input_number, action = data
    if action == 'create':
        result = create_number(input_name, input_number, book)
    elif action == 'update':
        result = update_number(input_name, input_number, book)
    elif action == 'delete':
        result = delete_number(input_name, book)
    else:
        return False
    return result