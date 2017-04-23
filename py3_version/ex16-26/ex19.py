def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses." % cheese_count)
    print("You have %d boxes of crackers." % boxes_of_crackers)
    print("Dang! That's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly.")
cheese_and_crackers(20, 40)

print("OR we can use variables from our script.")
amount_of_cheese = 10
amount_of_crackers = 30

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can do Math inside too!")
cheese_and_crackers(10 + 5, 20 + 3)

print("We can even do both.")
cheese_and_crackers(amount_of_cheese + 4, amount_of_crackers + 7)
