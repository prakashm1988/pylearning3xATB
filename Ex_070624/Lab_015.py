num = 42
num_str = str(num)
print(num_str)  # Output: "42"
print(type(num_str))  # Output: <class 'str'>


num_str = "42"
num = int(num_str)
print(num)  # Output: 42
print(type(num))  # Output: <class 'int'>


#num_str = "42.5"
#num = int(num_str)  # ValueError: invalid literal for int() with base 10: '42.5'

num_str = "42.5"
num = float(num_str)
print(num)  # Output: 42.5
print(type(num))  # Output: <class 'float'>
