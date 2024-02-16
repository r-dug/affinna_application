#!/usr/bin/python3
'''
This is just a little bit of python in response to the prompt for applying to Affinna.

I hope you find it satisfactory.
'''
# imports
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime

# data given in assignment
data = [{'price': 10, 'item': 'a', 'qty': 2}, {'price': 10, 'item': 'a', 'qty': 1}, {'price': 14, 'item': 'b', 'qty': 3}, {'price': 16, 'item': 'b', 'qty': 2}, {'price': 20, 'item': 'c', 'qty': 5}]
# banner for nice readable output
banner = '\n'+'*'*40+'\n'
# helper - The total quantity
def total_qty(data):
    totalQty = 0
    for dictionary in data:
        totalQty += dictionary['qty']
    return totalQty
# helper - The total sales price
def total_prices(data):
    price_sum = 0
    for dictionary in data:
        price_sum += dictionary['price']
    return price_sum
# helper - The average sales price of item 'b'
def avg_b(data):
    totalBPrice = 0
    numB = 0
    for dictionary in data:
        if dictionary['item'] == 'b':
            totalBPrice += dictionary['price']
            numB += 1
    if numB != 0:        
        avgBPrice = totalBPrice/numB
        return avgBPrice
    else:
        print("no items found as 'b'")
        return None
# run main
if __name__ == '__main__':
    # assign returns from helper functions to aptly named variables
    # I have considered that this way of implementing the python code will run three for loops. 
    # all of the data could certainly be collected in a single pass over the data
    start = datetime.now()
    totalQty = total_qty(data)
    totalPrices = total_prices(data)
    avgBPrice = avg_b(data)
    # print output
    print(f"{banner}Total quantity: {totalQty}{banner}Sum of all prices {totalPrices}{banner}Average price of product 'b': {avgBPrice}{banner}")
    end = datetime.now()
    mod_time = end - start
    print(f"time elapsed modular: {mod_time}{banner}")

    # example of collecting data in single pass
    start = datetime.now()
    totalQty = 0
    totalPrices = 0
    totalBPrice = 0
    numB = 0
    for dictionary in data:
        totalQty += dictionary['qty']
        totalPrices += dictionary['price']
        if dictionary['item'] == 'b':
            totalBPrice += dictionary['price']
            numB += 1
    if numB != 0:        
        avgBPrice = totalBPrice/numB
    else:
        print("no items found as 'b'")
        avgBPrice = None
    
    # print output
    print(f"{banner}Total quantity: {totalQty}{banner}Sum of all prices {totalPrices}{banner}Average price of product 'b': {avgBPrice}{banner}")
    end = datetime.now()
    sp_time = end - start
    print(f"time elapsed single pass: {sp_time}{banner}")


    # SEABORN SECTION

    # create pandas dataframe from list of python dictionaries
    df = pd.DataFrame(data)
    
    # plot data according to formatting guidelines in assignment with seaborn
    sns.scatterplot(data=df, x="qty", y="price", hue="item", palette={'a':'#ea0808', 'b':'#07ff25', 'c':'#ffbb07'})
    
    # display scatter plot with matplotlib
    plt.show()
