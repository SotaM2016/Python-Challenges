def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

list = []
amount = 0
while amount < 6:
    amount += 1
    temp = 0
    while True:
        temp = input("Enter the temperature (Check " + str(amount) + "): ")
        if is_number(temp):
            temp = int(temp)
            break
        else:
            print("Please input a valid number")
    if temp < -30 or temp > -10:
        print("Alarm Activated (Temperature is not between -30 and -10!)")
    list.append(temp)

print("Results:")
print("Minimum Temperature: ", min(list))
print("Maximum Temperature: ", max(list))
print("Mean Temperature: ", sum(list)/len(list))