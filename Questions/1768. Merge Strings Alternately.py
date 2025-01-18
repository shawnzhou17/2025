def mergeAlternately(word1: str, word2: str) -> str:
    # Initialize result string and pointers
    result = []
    i = j = 0
    
    # Merge strings alternately until we reach the end of either string
    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1
    
    # Append remaining characters from word1, if any
    result.extend(word1[i:])
    
    # Append remaining characters from word2, if any
    result.extend(word2[j:])
    
    return ''.join(result) 