# input bill
# replace $ with 0
# ask for tip %
# calculate tip in resonable .00
# print

x = input("pls enter bill in $")
bill = x.strip("$")
bill = float(bill)
tip_percentage =  input("what percent do u want to tip")
tip_percentage = tip_percentage.replace("%", " ")
tip_percentage = float(tip_percentage)
tip = (bill * (tip_percentage / 100))
total = bill + tip
print(f"ur tip is {tip:.0f}$ and ur total is {total:.2f}$")
