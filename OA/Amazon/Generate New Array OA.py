
# Generate New Array


# Your project team needs to work closely with a group of software testers. They have requested that your team
# create an array generator service to assist with testing software functionality. Create an array generator service.
# Its input parameters are:
# ⚫ arr[n] contains n positive integers.
# • state is a string that contains n characters.
# If state[i] = '0', arr[i] is blocked, 249cd44-fe9e-403f-b50e-8c92be8074fb@hook.com
# • Each character is a '0' or '1'.
# • If state[i] = '1', arr[i] is available.
# •
# To create an integer array, S, the following operation is performed exactly m times. Sis initially empty.
# HackerRank Confidential
# • Choose any arr[i] that is available, that is, where state[i] = '1', the same element can be chosen any number of times. Append the value in arr[i] to S.
# • For all state[i]='0' such that state[i-1] = '1', change state[i] to '1'. For example, if state = '0100101' before the operation, it equals '0110111' after the operation.
# hook+4249cd44-fe9e-
# Find the lexicographically largest sequence S that can be obtained after moperations.
# ranyj (0 <j<1) XUJJ = Y[J].
# Maske/Rank Cor
# Note: A sequence x of length mis lexicographically larger than sequence y of length m if there exists such i(0 <i< m), that x[i]> y[i], and
# Example
# HackerRank Comma
# Start with arr = [10, 5, 7, 6], state = '0101', and m = 2.
# Blockedon hook+4249cc44-198-40811506-8692be807
# Blocked
# Blocked
# Blocked
# 10
# 5
# 7
# 6
# Choose 6 10
# 5
# 7
# 6
# Choose 7- 10
# 5
# 7
# 6
# Available
# fb@hook.com
# Available
# -Available-
# Confidential
# -Available-
# HackerRank Confidy
# state = '0101'so indices 1 and 3 are available.
# arr[3] is the higher value so append 6 to S. S = [6] Modify '0101'to get '0111'.
# Now indices 1, 2, and 3 are available.
# zon_hook+4249cd44-169e-4031-550e-8c92be8074fb@hook.com
# [6, arr[2] is the highest value, so append 7 to SS1
# @hook.com Exactly m = 2 operations were performed. Return [6, 7].
# HackerRank
# Confidential
# Q Search
# 2be8074fb@hook
# Te
# am