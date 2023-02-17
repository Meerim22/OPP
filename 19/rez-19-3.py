def min_amount(costs):
    costs.sort(reverse=True)
    total_cost = 0
    summ = sum(costs)
    for i in range(2, len(costs), 3):
        total_cost += costs[i]
    return summ - total_cost
 
n = int(input())
costs = list(map(int, input().split()))
print(min_amount(costs))