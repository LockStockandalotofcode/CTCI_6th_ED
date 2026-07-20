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
	curr_end = true_len - 1 # initialised to the end point
	
	def helper(idx: int):
		nonlocal curr_end, true_len
		for i in range(curr_end, idx, -1): # shifting right segment by 2 places to its right
			char_list[i + 2] = char_list[i]
		if curr_end + 2 < len(char_list):
			curr_end += 2
		else:
			curr_end = len(char_list) - 1
		char_list[idx] = "%"
		char_list[idx + 1] = "2"
		char_list[idx + 2] = "0"

	# main logic
	for i in range(true_len - 1, -1, -1):
		if char_list[i] == " ":
			helper(i)
	
	res = "".join(char_list)
	# .rstrip() to get rid of trailiing spaces in a string
	cleaned_res = res.rstrip()
	return cleaned_res


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
