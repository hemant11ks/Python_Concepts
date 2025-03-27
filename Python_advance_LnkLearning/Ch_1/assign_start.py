import pprint

# Regular assignment statement assign a value
# x = 5
# print(x)

# Assignment operator is part of an expression
# It evaluates to the value on the right

# ( x:= 10 )
# print(x)
# 10

# Assignment expression is usefull for writting concise code
# thestr = input("Give me a string: ")
# while thestr != "exit":
#     print(thestr)
#     thestr = input("Give me a string: ")

# Give me a string: hemant
# hemant
# Give me a string: exit

# Here in this example we are calling input two times which decreases the performance of the code.
# while(thestr := input("Give me a string:")) != "exit":
#     print(thestr)

# The walrus operator can help reduce the number of same function calls.

values = [1,2,3,4,5,6,7,8,9,10]
# val_data = {
#     "length": len(values),
#     "total": sum(values),
#     "mean": sum(values)/len(values),
# }

# print(val_data)
# {'length': 10, 'total': 55, 'mean': 5.5}

# Now lets use walrus operator to do the same thing
if (n:= len(values))>0:
    print(f"Mean: {sum(values)/len(values)} | Length: {len(values)} | Total: {sum(values)}")