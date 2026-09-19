test_case = ["001001011", "101110011","011101001", "110100111"]

for input_text in test_case:

    state = "AC"

    for ch in input_text:
        if state == "AC":
            if ch == '0':
                state = "B"
            elif ch == '1':
                state = "AC"
        
        elif state == "B":
            if ch == '0':
                state = "B"
            elif ch == '1':
                state = "D"
        
        elif state == "D":
            if ch == '0':
                state = "B"
            elif ch == '1':
                state = "E"
        
        elif state == "E":
            if ch == '0':
                state = "B"
            elif ch == '1':
                state = "AC"

    if state == "E":
        print(input_text,"→ Input Accepted")
    else:
        print(input_text,"→ Input Rejected")
