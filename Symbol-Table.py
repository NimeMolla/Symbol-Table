class Entry:
    def __init__(self, hash_key, name, data_type):
        self.hash_key = hash_key
        self.name = name
        self.data_type = data_type


symbol_table = []

def is_comma_separated(my_input):
    for charecter in my_input:
        if charecter == ',':
            return True
    return False

def get_hash_key(name):
    ascii_value = 0
    #for cha in name:
    #    ascii_value += ord(cha)
    #return ascii_value % 100
    ascii_value=id(name)

    return ascii_value

def is_match_found(name):
    index = -1
    if len(symbol_table) > 0:
        for index, element in enumerate(symbol_table):
            if element.name == name:
                return True, index
        return False, index

    return False, index

# Insert new String Data ( Nime,string)

def insert(my_input):
    if is_comma_separated(my_input):
        users_input = my_input.split(',')
        name = users_input[0].strip()
        data_type = users_input[1].strip()
        hash_key = get_hash_key(name)
        new_entry = Entry(hash_key, name, data_type)

        match_found, index = is_match_found(name)
        if not match_found:
            symbol_table.append(new_entry)
            return 'Successfully insert'
        return "Name already exists."

    return "Sorry! You didn't enter comma between words...."

def show():
    for entry in symbol_table:
        print(f"Hash key is: {entry.hash_key}  --->  Name: {entry.name}  --->  Data Type: {entry.data_type} ")

def search(name):
    match_found, index = is_match_found(name)

    if match_found:
        return f"Match found. Hash Key is --> {symbol_table[index].hash_key} and Data Type --> {symbol_table[index].data_type}"

    return "No match found with this Name. "

def update(name):
    match_found, index = is_match_found(name)

    if match_found:
      data_type = input("Enter new data type to update: ")
      if symbol_table[index].data_type == data_type:
        return "There is nothing to update. You entered same data type."

      symbol_table[index].data_type = data_type
      return "Update data type successfully."

    return "No match found with this name. "


def delete(name):
  match_found, index = is_match_found(name)

  if match_found:
    del symbol_table[index]
    return "Delete successfully"

  return "No match found with this name. "



while True:
    print("Enter 1 for Insert")
    print("Enter 2 for Show")
    print("Enter 3 for Search")
    print("Enter 4 for Update")
    print("Enter 5 for Delete")
    print("Enter 6 for Exit")

    user_input = input('Enter your option: ')

    if user_input == '1':
        new_data = input("Input {Info,Data type} like inside the bracket :")
        print('')
        print(insert(new_data))
        print('')

    elif user_input == '2':
      if len(symbol_table) > 0:
          print('')
          show()
          print('')
      else:
        print("Symbol table is empty. Please insert data. \n")

    elif user_input == '3':
      if len(symbol_table) > 0:
        new_data = input("Enter existing name from symbol table: ")
        print('')
        print(search(new_data))
        print('')
      else:
        print("Symbol table is empty. Please insert data. \n")

    elif user_input == '4':
      if len(symbol_table) > 0:
        new_data = input("Enter existing name from symbol table update: ")
        print('')
        print(update(new_data))
        print('')
      else:
        print("Symbol table is empty. Please insert data.\n ")

    elif user_input == '5':
      if len(symbol_table) > 0:
        new_data = input("Enter existing name from symbol table to delete: ")
        print('')
        print(delete(new_data))
        print('')
      else:
        print("Symbol table is empty. Please insert data. \n")

    elif user_input == '6':
      break

    else:
        print("Wrong input")