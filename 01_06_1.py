# PROBLEM 01_06

# # clairifications & assumptions
# given string only has alphabets
# are lowercase and uppercase treated differently : then == operator does the work
# otherwise: we can convert entire string to lower or upper before starting

# if res doesnot give a string shorter than input, return original string

# # logic
# convert string to char_list, keep results char_list separate with separate index
# traverse input string from starting
# keep running frequency counter, for each character, while same character ahead
# increment iterator using freq counter

# compare both res and input

# edge cases
# TEST CASES
test_cases = {
	"aabcccccaaa": "a2b1c5a3",
	"abcd" : "abcd",
	"" : "",
	"aa" : "aa",
	"AAAaaBB": "A3a2B2"
}

# CODE
def str_comprsn(s: str) -> str:
	# base case
	if not s or len(s) == 0:
		return s

	res = []
	i = 0
	while i < len(s):
		char = s[i]
		freq = 1
		while (i + freq) < len(s) and s[i + freq] == char:
			freq += 1
		res.append(char)
		res.append(str(freq)) # convert freq int to str, before appending, sice .join() only joins str characters
		i += freq

	result = "".join(res)
	result.strip()
	return result if len(result) < len(s) else s



# TESTING
print("Running test cases: ")
all_passed = True

for idx, (input_val, exp_output) in enumerate(test_cases.items(), 1):
	result = str_comprsn(input_val)
	if result == exp_output:
		print(f"passed Test {idx}.")
	else:
		print(f"failed Test {idx} - Input: {input_val} | Expected: {exp_output} | Got: {result}")
		all_passed = False

if all_passed == True:
	print("\n All cases PASSED.")