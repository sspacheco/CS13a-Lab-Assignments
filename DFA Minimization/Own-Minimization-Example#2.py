test_case = ["01101", "10110", "01001", "10011"]

for input_text in test_case:

    state = 0

    for ch in input_text:

        if state == 0:
            if ch == '0':
                state = 12
            elif ch == '1':
                state = 12

        elif state == 12:
            if ch == '0':
                state = 34
            elif ch == '1':
                state = 34

        elif state == 34:
            if ch == '0':
                state = 5
            elif ch == '1':
                state = 0

        elif state == 5:
            if ch == '0':
                state = 5
            elif ch == '1':
                state = 5


    if state == 34:
        print(input_text,"→ Input Accepted")
    else:
        print(input_text, "→ Input Rejected")