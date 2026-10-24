from collections import defaultdict

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        if not s or not len(s):
            return None
        
        char_indices = defaultdict(list)
        # record char indices for all letters in the string
        for idx, char in enumerate(s):
            char_indices[char].append(idx)

        # single pass through string
        # calculate contribution for every character
        total_unique_count = 0
        n = len(s)
        for char, indices in  char_indices.items():
            padded_indices = [-1] + indices + [n]

            for i in range(1, len(padded_indices) - 1):
                curr_index = padded_indices[i]
                prev_index = padded_indices[i - 1]
                next_index = padded_indices[i + 1]

                contribution = (curr_index - prev_index) * (next_index - curr_index)
                total_unique_count += contribution

        return total_unique_count