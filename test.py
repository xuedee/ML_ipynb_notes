max_inst=17

for i in range(max_inst):
    if i % (3*5)==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)

"""


    if i % (3*5)==0:
        return "fizzbuzz"
    elif i%3==0:
        return "fizz"
    elif i%5==0:
        return "buzz"
    else:
        return i

"""