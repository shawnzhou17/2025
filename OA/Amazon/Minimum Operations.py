# Minimum Operations
 
# In this challenge, the task is to debug the existing code to successfully execute all provided test files.

# There are  boxes in front of you. For each , box  contains  red balls,  green balls, and  blue balls.

# You want to separate the balls by their color. In each operation, you can pick a single ball from some box and put it into another box. The balls are separated if no box contains balls of more than one color.

# Debug the given function min_operations and compute the minimal number of operations required to separate the balls.

# Note: In this problem you can modify at most six lines of code and you cannot add any new lines.

# To restore the original code, click on the icon to the right of the language selector.

# Input Format

# The first line contains a single integer . The next  lines  contain three space-separated integers, , , and , respectively.

# Constraints



# Output Format

# Print the minimal number of operations required to separate the balls. If this is impossible, return .

# Sample Input

# 3
# 1 1 1
# 1 1 1
# 1 1 1
# Sample Output

# 6
# Explanation

# Each box contains 1 ball of each color. In this explanation, the goal will be to let the first box contain only red balls, the second box only blue balls, and the third box only green balls.

# Move 1 blue ball and 1 green ball from the first box to the second and third boxes.
# Move 1 red ball and 1 green ball from the second box to the first and third boxes.
# Move 1 red ball and 1 blue ball from the third box to the first and second boxes.
# The number of operations is 6.












# # There are n points, the ith point initially has a weight of weight[i] and is located at position i on x-axis. In a single operation, the ith point can be moved to right by a dist[i]. Given the weight and dist find the minimum number of operations required to sort the points by their weights.


# # Example:
# # n=4, weight=[3,6,5,1] and dist = [4,3,2,1]
# # number of operations = 1+2+2=5


# # First move weights[0]=3 to 0+4 place (1move)
# # Next move weights[1]=6 to 1+3 = 4 and 4+3=7 place (2moves)
# # Next move weights[2]=5 to 2+2=4 and 4+2=6 place (2moves)


# # Constraints:
# # 2 <= n <= 2 * 10^5
# # 1 <= wieghts[i] <= 10^9
# # 1 <= dist[i] <= 10^3


# # public static long getMinOperations(List<Integer> weights, List<Integer> dist){...}