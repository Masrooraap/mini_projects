import random
lower_letters = "abcdefghigklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
total = lower_letters + upper_letters + numbers
gen_password = "".join(random.sample(total, 12))
print("the password generator is:", gen_password)