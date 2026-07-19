# 01_01
# # edge cases:
# Normal case:  "abcdef"
# bad case:  "abcdea"
# Empty case: ""
# Single element: "a"
# extreme case: "a" * 10000

# # other clarifications
# are spaces treated as characters
# # assumptions:
# considering only ASCII 128 characters, uniicode char is inefficient

# # LOGIC:
# traverse through the string, maintaining hashset or hashdict
# skipping through all spaces
# when encountered duplicate, return False immediately
# after passing through the entire string, return True
# for no extra data structure: we can use 128-size (ASCII) array with bool values, initialised to False, if ever encounter True at a char while traversing, we return False

# CODE
def is_unique(s: str) -> bool:
	# base null case
	if len(s) == 0:
		return True
	
	track_arr = [False] * 128
	
	for c in s:
		if not c.isascii():
			continue
		idx = ord(c) # ord() gets ascii code for the char, generally unicode, but for first 128, its equal to ascii code
		if track_arr[idx] == True:
			return False
		track_arr[idx] = True
	
	return True

# TEST CASES : "input": expected_output
test_cases = {
	"abcdef": True,
	"abcdea": False,
	"" : True,
	"a": True,
	"a" * 1000: False
}

# testing 
print("Running test cases: ")
all_passed = True

for idx, (input_val, exp_output) in enumerate(test_cases.items(), 1):
	result = is_unique(input_val)
	if result == exp_output:
		print(f"passed Test {idx}.")
	else:
		print(f"failed Test {idx} - Input: {input_val} | Expected: {exp_output} | Got: {result}")
		all_passed = False

if all_passed == True:
	print("\n All cases PASSED.")


