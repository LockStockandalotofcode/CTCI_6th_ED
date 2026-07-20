# PPROBLEM 01_03

# PPROBLEM 01_03

# # EDGE CASES
# normal case: "Mr John  Smith    ",  13

# no negative case
# empty case: "", 0
# edge case: " ", 0
# edge case: "a  ": 1

# # CLARIFICATIONS ASSUMPTIONS
# suffiicient space is given for the expected output to fit into input string

# # LOGIC
# traverse from end of string, starting at true_len - 1, 
# for every space encountered, shift the right segment by 2 places to the right

# CODE
def urlify(s: str, true_len: int) -> str:
    # empty case
    if true_len == 0:
        return s
    
    char_list = list(s)
    start_idx = len(char_list)

    # main logic
    for input_idx in range(true_len - 1, -1, -1):
        if char_list[input_idx] == " ":
            char_list[start_idx - 3: start_idx] = "%20"
            start_idx -= 3
        else:
            char_list[start_idx - 1] = char_list[input_idx]
            start_idx -= 1
                  
    res = "".join(char_list[start_idx:])
    # res.strip()
    return res


# TESTCASES : "input" : expected_output; Dict
test_cases = {
    ("Mr John Smith     ", 13): "Mr%20John%20Smith",
    ("Mr John  Smith        ", 14): "Mr%20John%20%20Smith",
    ("a  Smith        ", 8): "a%20%20Smith",
    ("", 0): "",
    ("    ", 1): "%20",
    ("a  ", 1) : "a",
    (" a b     ", 4): "%20a%20b",
    (" a b       ", 5): "%20a%20b%20",
    ("much ado about nothing      ", 22): "much%20ado%20about%20nothing"
}

# TESTING
print("\nRunning all test CASES")
all_passed = True

for idx, (input_val, exp_output) in enumerate(test_cases.items(), 1):
    result = urlify(*input_val)

    print(f"\nidx {idx} result len = {len(result)}, exp_output len = {len(exp_output)}")
    if result == exp_output:
        print(f"Test Case {idx} PASSED")
    else:
        print(f"failed Test {idx} - Input: {input_val} | Expected: {exp_output} | Got: {result}")
        all_passed = False

if all_passed == True:
    print("\n All cases PASSED.")