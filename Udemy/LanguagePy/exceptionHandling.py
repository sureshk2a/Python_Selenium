itemsInCart = 0
if itemsInCart != 2:
    # raise Exception("Cart items are not 2") #custom exception
    pass
# assert(itemsInCart == 20) #assertion

try:
    with open('filelog.txt','r') as file:
        file.readlines()
except Exception as e:
    print(e)
