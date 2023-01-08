
#my_global_var = 3.14

def hello_simple():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("Hello there")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def hello_name(name):
  #  global my_global_var
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'Hello, {name}!')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

if __name__ == "__main__":
    input_name = input("name = ")
    hello_name(input_name)
    hello_simple()
    hello_simple()

