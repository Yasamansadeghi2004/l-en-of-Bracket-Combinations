def BracketCombinations(num):
    memo = {}

    def count_combinations(open_brackets, closed_brackets):
        if open_brackets == 0 and closed_brackets == 0:
            return 1
        if (open_brackets, closed_brackets) in memo:
            return memo[(open_brackets, closed_brackets)]

        total_combinations = 0
        if open_brackets > 0:
            total_combinations += count_combinations(open_brackets - 1, closed_brackets + 1)
        if closed_brackets > 0:
            total_combinations += count_combinations(open_brackets, closed_brackets - 1)

        memo[(open_brackets, closed_brackets)] = total_combinations
        return total_combinations

    return count_combinations(num, 0)

# Example usage:
print(BracketCombinations(int(input(":"))))  # Output should be 5
