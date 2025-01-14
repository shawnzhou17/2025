# A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

# It is ().
# It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
# It can be written as (A), where A is a valid parentheses string.
# You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

# If locked[i] is '1', you cannot change s[i].
# But if locked[i] is '0', you can change s[i] to either '(' or ')'.
# Return true if you can make s a valid parentheses string. Otherwise, return false.

 

# Example 1:


# Input: s = "))()))", locked = "010100"
# Output: true
# Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
# We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
# Example 2:

# Input: s = "()()", locked = "0000"
# Output: true
# Explanation: We do not need to make any changes because s is already valid.
# Example 3:

# Input: s = ")", locked = "0"
# Output: false
# Explanation: locked permits us to change s[0]. 
# Changing s[0] to either '(' or ')' will not make s valid.
 

# Constraints:

# n == s.length == locked.length
# 1 <= n <= 105
# s[i] is either '(' or ')'.
# locked[i] is either '0' or '1'.




class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # A valid parentheses string must have even length
        if len(s) % 2:
            return False
        
        def check(s: str, locked: str, open_paren: str) -> bool:
            # balance: keeps track of the difference between opening and closing parentheses
            # positive balance means we have more opening parentheses
            # negative balance means we have more closing parentheses
            balance = 0
            
            # available: counts positions that we can modify (locked[i] == '0')
            # we can use these positions to fix any imbalances
            available = 0
            
            for i in range(len(s)):
                if locked[i] == '1':
                    # For locked positions, we must use the existing parenthesis
                    if s[i] == open_paren:
                        balance += 1  # Found a locked opening parenthesis
                    else:
                        balance -= 1  # Found a locked closing parenthesis
                else:
                    # For unlocked positions, we can use them later to fix imbalances
                    available += 1
                
                # Key validation: at any point, if we have more closing parentheses than
                # we can fix with our available positions, it's impossible
                # Example: ")" with balance = -1 and available = 0
                if balance < 0 and available + balance < 0:
                    return False
            
            # Final check: we need enough available positions to fix any remaining imbalance
            # abs(balance) represents how many parentheses need to be changed
            # Example: "(((" with balance = 3 needs 3 positions to add closing parentheses
            return abs(balance) <= available
        
        # We need to check in both directions:
        # 1. Left to right: ensures we don't have too many closing parentheses early
        #    Example: ")(" would fail the left-to-right check
        # 2. Right to left: ensures we don't have too many opening parentheses late
        #    Example: "(()" would fail the right-to-left check
        return check(s, locked, '(') and check(s[::-1], locked[::-1], ')')

