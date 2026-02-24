# Method 1
def calculate_love_score(name1, name2):
    name_combo = name1 + name2
    compare_true = "true"
    compare_love = "love"
    true_val = 0
    for i in name_combo:
        if i in compare_true:
            true_val += 1
    love_val = 0
    for i in name_combo:
        if i in compare_love:
            love_val += 1
    print(str(true_val)+str(love_val))
calculate_love_score("Kanye West", "Kim Kardashian")



# Method 2
def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    score = int(str(first_digit) + str(second_digit))
    print(score)
calculate_love_score("Kanye West", "Kim Kardashian")
