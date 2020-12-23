prc = float(input("Enter the price for meal: "))

Tax = (13/100) * prc

Tip = (15/100) * prc

print("Bill description is down below")

print("Meal price is: %.2f" %prc)

print("Given Tip is: %.2f" %Tip)

print("Tax on the meal: %.2f" %Tax)

print("Total meal price: %0.2f" %(prc+Tip+Tax))
