cost_price,selling_price = float(input('Enter Cost Price:')), float(input('Enter Selling Price:'))
#since it is not mentioned in question whether loss will occur or not i am assuming only profit will occur
profit = selling_price-cost_price
print('Profit from this sell:',profit)
new_profit = profit+(profit*0.05)
new_selling_price = cost_price+new_profit
print('New selling price:',new_selling_price)
