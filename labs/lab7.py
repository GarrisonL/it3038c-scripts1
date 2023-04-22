import random

print(random.randint(1, 25))

for i in range(5):
    print(random.random())

items = ["cashew", "almond", "walnut","hazlenut","peanut","raisin","milk","almondmilk","vanilla-bean"]
print(random.choice(items))