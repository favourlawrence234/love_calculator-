your_name = input('enter your name '"\n")
person_name = input('enter the persons name '"\n")


join_names = your_name + person_name
lower_names = join_names.lower()

t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')

first_digit = t + r + u + e

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')

second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit) )
if score < 10 or score > 90:
    print(f'Your score is {score} you go together like coke and mentos.')
elif score >= 40 or score <= 50:
    print(f'Your score is {score} you are alright together')
else:
    print(f'Your score is score')