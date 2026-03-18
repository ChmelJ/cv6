def analyze_password(password,
                     min_length=8,
                     require_digit=True,
                     require_upper=True,
                     require_symbol=False,
                     banned_words=None):
    is_strong = True
    count_active_rules = 0
    count_rules = 0
    missing_rules = []
    if min_length > 0:
        count_active_rules += 1
    if len(password) < min_length:
        is_strong = False
        missing_rules.append("min_length")
    else:
        count_rules += 1
    if require_digit:
        count_active_rules += 1
    ...
    score_percent = count_rules / count_active_rules * 100
    return is_strong, score_percent, missing_rules


print(analyze_password("ahoj", 5,
                       False, True,
                       True, ["12345"]))
print(analyze_password("heslo", min_length=5, require_symbol=True))
print(analyze_password("1234"))
print(analyze_password("1234", banned_words=["1234", "heslo"]))
