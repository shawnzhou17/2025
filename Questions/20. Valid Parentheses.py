def isValid(s: str) -> bool:
    # Initialize stack to store opening brackets
    stack = []
    
    # Define mapping of closing to opening brackets
    brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    # Iterate through each character in the string
    for char in s:
        # If it's a closing bracket
        if char in brackets:
            # Check if stack is empty or top element doesn't match
            if not stack or stack.pop() != brackets[char]:
                return False
        # If it's an opening bracket
        else:
            stack.append(char)
    
    # Return true if stack is empty (all brackets matched)
    return len(stack) == 0 