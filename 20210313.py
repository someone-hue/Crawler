
import random
answer = random.randint(1,100)
counts = 3

while counts > 0:
    temp = input("猜猜我几岁？")
    guess = int(temp)
    
    if guess == answer:
        print("猜对啦！")
        break
    else:
        if guess < answer:
            print("小啦")
        else:
            print("大啦")    
    counts = counts -1
    
