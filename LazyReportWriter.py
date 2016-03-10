import random
comments = ["Did really bad", "Did really good", "Did average", "Didn't do well at all", "Did a great job"]
amount = int(input("Enter the amount of students: "))
current = 1
while current <= amount:
    print("Student", current, "Comment: " + random.choice(comments))
    current += 1