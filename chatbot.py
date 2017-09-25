# elena thornton
# 9/22/17
# unit 2 project

# This programs that talks it will go through a basic conversation with the user.
print("Hello my name is Chatbot 1.0")
print("^////^")
# this gets the users name
users_name = input("What's you name?:")
print("It's very nice to meet you", users_name)
# this get the place the user is from
where_user_is_from = input("Where are you from:")
print("I've heard it's very nice in", where_user_is_from)
# this gets the users favorite number
users_favorite_number = input("What you favorite number?:")

chatbots_favorite_number = float(users_favorite_number) * 3

print(users_favorite_number, "is a really cool number. My favorite number is", chatbots_favorite_number)
print("=^_^=")
# this gets the users favorite computer type
users_favorite_computer = input("I have a random question, what your favorite computer type?:")
print("ooooooooo", users_favorite_computer, "is a nice computer!")
# this gets the price of the computer
computer_price = input("do you know how much that cost?:",)
print("that's seem like a reasonable prince")
# this gets the interest rate
interest_rate = input("what is the interest rate on the lovely computer:",)
print("finally if you had to take out a loan for the computer")
# this get the number of years that it would take to pay back the loan
computer_loan = input("how many years would you take the loan out for?:",)

# this is formula the for the calculation
monthly_interest_rate = float(interest_rate)/100/12
monthly_payment = float(computer_loan) * 12
price = float(computer_price)

monthly_payment_price = monthly_interest_rate * price / (1-(1 + monthly_interest_rate) ** - monthly_payment)


print("now that I know these numbers I can tell you that over", computer_loan)
print("years you would have to pay ", monthly_payment_price, "per month")
print("", users_name, "it was very nice talking with you but now i must go as i here motherbot calling me bye bye")
