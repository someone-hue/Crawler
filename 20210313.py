'''猜猜我的年龄'''
import random
answer = random.randint(1,100)
counts = 3
guess = input("猜猜我几岁？")
while counts > 0:
    counts = counts - 1
    if guess = answer:
        print("猜对啦！")
        break
    else:
        if guess < answer:
            print("小啦")
        else:
            print("大啦")    

