# a Java.Map equivalent in Python is called 'Dictionary'
my_dict = {'some-key' : 'some-value', 'another-key' : 'another-value'}
print(my_dict)

# get the value by key using brackets
print(my_dict['another-key'])


# you can loop through all keys
for k in my_dict.keys():
    print(k)

# ommiting .keys() loops also on keys
for k in my_dict:
    print(k)

# you can loop through all values
for v in my_dict.values():
    print("this is a map value: " + v)


# you can loop through all key-values
for k, v in my_dict.items():
    print("key: " + k + ", with value: " + v)
    
