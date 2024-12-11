
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