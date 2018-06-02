def grabPrice(data) :
    return data.findAll("p", {"class": "pl-list-price"})

def grabName(data) :
    return data.findAll("div", {"class": "pl-list-pname"})

def printData(data):
    prices = grabPrice(data)
    names = grabName(data)
    for x in range(len(prices)):
        print("(" + str(x) + ")\tName:" + names[x].text)
        print("Price: " + prices[x].text + "\n")
