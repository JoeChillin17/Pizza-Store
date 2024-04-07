#List of Toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#Prices
prices = [2, 6, 1, 3, 2, 7, 2]

#Number of $2 slices
num_two_dollar_slices = prices.count(2)
#print(num_two_dollar_slices)

#The number of toppings
num_pizzas = len(toppings)

#Headline for store
print("We sell", num_pizzas, "different kinds of pizza!")

#Menu
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
pizza_and_prices = sorted(pizza_and_prices)
print(pizza_and_prices)


#Lowest Priced Pizza
cheapest_pizza = pizza_and_prices[0]
print("Our lowest priced pizza is:", cheapest_pizza)

#The most expensive pizza
priciest_pizza = pizza_and_prices[-1]
print("Our most expensive pizza is:", priciest_pizza, )

#Last slice of anchovies was bought
pizza_and_prices.pop(-1)
print("The last slice of anchovies has been purchased. We will introduce our new pizza topped with peppers!")

#New Topping
pizza_and_prices.insert(-2, [2.5, "peppers"])
print("Our new updated menu looks as such:", pizza_and_prices)

#Three cheapest pizzas
three_cheapest = pizza_and_prices[0:3]
#print(three_cheapest)






