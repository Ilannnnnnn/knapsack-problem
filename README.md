## Knapsack Problem Solver

**Enhanced README**

**Project Description:**

This repository provides efficient Python implementations for solving the Knapsack Problem, a classic combinatorial optimization problem. The goal is to select a subset of items from a given set, where each item has a weight and a value, such that the total value is maximized while the total weight does not exceed a given capacity.

**Algorithms:**

  * **Dynamic Programming:** Offers the optimal solution for any instance of the Knapsack Problem.
  * **Greedy Algorithm:** Provides a fast approximation, suitable for large problem instances.
  * **Hybrid Greedy and Local Search:** Combines the strengths of greedy and local search for improved results.

**Installation:**

Ensure you have Python 3.x installed. 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install time.

```bash
pip install time
```

**Usage:**

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Ilannnnnnn/knapsack-problem.git
    ```

2.  **Run the Scripts:**

    Replace `<weight>` and `<values>` with your own data:

    ```bash
    python dynamic_algo.py <weight> <values>
    python greedy_algo.py <weight> <values>
    python greedy_algo_opti.py <weight> <values>
    ```

**Output:**

The scripts will print the maximum achievable value and the corresponding selected items.

**Example:**

```
Input:
Weight capacity: 50
Items:
  - Weight: 10, Value: 60
  - Weight: 20, Value: 100
  - Weight: 30, Value: 120

Output:
Maximum value: 220
Selected items: 2, 3
```

**Time Complexity:**

  * Dynamic Programming: O(n \* W)
  * Greedy Algorithm: O(n log n)
  * Hybrid Greedy/Local Search: O(n log n) + local search


**License:**

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/)
