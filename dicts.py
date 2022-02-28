from multiprocessing.sharedctypes import Value


my_dict={3:9,6:36,9:81}

print(my_dict)

Value=my_dict[9]
print(Value)