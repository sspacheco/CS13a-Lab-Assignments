test_case = ["00010", "10000","00011", "10110"]

for input_text in test_case:

    state = "A"

    for ch in input_text:
        if state == "A":
            if ch == '0':
                state = "B"
            elif ch == '1':
                state = "C"
        
        elif state == "B":
            if ch == '0':
                state = "A"
            elif ch == '1':
                state = "DE"

        elif state == "C":
            if ch == '0':
                state = "DE"
            elif ch == '1':
                state = "F"
        
        elif state == "DE":
            if ch == '0':
                state = "DE"
            elif ch == '1':
                state = "F"
        
        elif state == "F":
            if ch == '0':
                state = "F"
            elif ch == '1':
                state = "F"

    if state == "DE":
        print(input_text,"→ Input Accepted")
    else:
        print(input_text,"→ Input Rejected")
