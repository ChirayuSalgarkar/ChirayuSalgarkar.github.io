import math

def solve(options, ansKey):
    # Check if the answer key has more unique characters than options available
    if len(set(ansKey)) > options:
        return "Impossible Answer Key!"
    
    # Calculate the probability of matching the answer key in one attempt
    prob_match = (1 / options) ** len(ansKey)
    
    # Calculate the minimum number of attempts required for > 50% success
    if prob_match == 1:
        a = 1
    else:
        a = math.ceil(math.log(0.5) / math.log(1 - prob_match))
    
    # Return the result modulo 1,000,000
    return a % 1000000


# Test cases
print(solve(1, "ab"))  # Impossible answer key
print(solve(1, "aa"))  # 1
print(solve(2, "aba"))  # 6
print(solve(2, "aaa"))  # 6
print(solve(3, "aba"))  # 19
print(solve(3, "abc"))  # 19
print(solve(4, "abc"))  # 45
print(solve(4, "abbabcabbacad"))  # 516320
print(solve(5, "abbabcabbacad"))  # 126887