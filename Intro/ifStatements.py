is_male = False
is_tall = True

if is_male and is_tall:
    print("User is male and tall")
elif is_male and not is_tall:
    print("User is male and short")
elif not is_male and is_tall:
    print("You are not a male but you are tall")
else:
    print("User is female and not tall")
