# PROBLEM 01_01:
  
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

# CODE
def is_unique(s: str) -> bool:
	# base null case
	if len(s) == 0:
		return True
	
	hash_set = set()
	for c in s:
		if c == " ":
			continue

		if c in hash_set:
			return False
		hash_set.add(c)
	
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
