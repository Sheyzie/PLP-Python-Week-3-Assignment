#Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount.

def calculate_discount(price, discount_percent):
  if discount_percent == 20: #check if discount percent is equal to 20%
    print(f'Your discount percent is 20%')
    finalPrice = price - price * (discount_percent/100) #calculate and remove the discount
    return finalPrice #returns the new discounted price 
  elif discount_percent > 20: #check if discount percent is greater 20%
    print(f'Your discount percent over 20%')
    finalPrice = price - price * (discount_percent/100) #calculate and remove the discount
    return finalPrice #returns the new discounted price 
  else: #if condiition i not met
    print(f'Your discount percent not up to 20%')
    return price  #return the initial price
  
getPrice = input('Please enter the price : ')
getPercent = input('Please enter the percentage discount : ')
if not getPrice:
  print('You did not enter any price')
getPrice = float(getPrice) #convert price to a  float datatype

if not getPercent: #if percentage 
  print(f'Your price is : NGN{getPrice}')
else:
  print(f'Your price is : NGN{getPrice}')
  getPercent = float(getPercent)
  finalPrice = calculate_discount(getPrice, getPercent)
  print(f'Your final price is : NGN{finalPrice}')
