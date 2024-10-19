# knapsack-problem
This repository includes three solutions to the **Knapsack Problem**: a dynamic programming approach for optimal results, a greedy algorithm for quick approximations, and a hybrid greedy/local search for further optimization. Each solution balances computational time and result accuracy.



## Algorithms Implemented:
1. **Dynamic Programming Approach** (`dynamic_algo.py`)
   - Provides an exact solution using dynamic programming.
   - **Time Complexity**: O(n * W), where n is the number of items and W is the maximum weight capacity.

2. **Greedy Algorithm** (`greedy_algo.py`)
   - Approximates the solution by selecting items based on their utility-to-weight ratio.
   - **Time Complexity**: O(n log n), due to sorting items by utility-to-weight ratio.

3. **Hybrid Greedy and Local Search Optimization** (`greedy_algo_opti.py`)
   - Improves the greedy solution by performing local search optimizations, refining the selection of items.
   - **Time Complexity**: O(n log n) + local search.

## How to Run:
To execute the algorithms, simply run the respective Python scripts in your terminal :

```bash
python3 dynamic_algo.py
python3 greedy_algo.py
python3 greedy_algo_opti.py
