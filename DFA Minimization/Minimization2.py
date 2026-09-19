test_case = ["000100", "100000", "010100", "100011"]

for input_text in test_case:

    state = "AB"

    for ch in input_text:

        if state == "AB":
            if ch == '0':
                state = "AB"
            elif ch == '1':
                state = "CDE"

        elif state == "CDE":
            if ch == '0':
                state = "CDE"
            elif ch == '1':
                state = "F"

        elif state == "F":
            if ch == '0':
                state = "F"
            elif ch == '1':
                state = "F"


    if state == "CDE":
        print(input_text,"→ Input Accepted")
    else:
        print(input_text, "→ Input Rejected")