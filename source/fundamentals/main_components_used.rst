**********************
Main Components Used
**********************


In the GADemo platform, the implementation of Genetic Algorithms (GAs) is guided by fundamental components that simulate an evolutionary process in a simplified yet functional manner. Below, we outline each core element used in the platform:

.. rubric:: 1. Objective Function

The **objective function** represents the mathematical expression the algorithm seeks to optimize. In the current version of GADemo, this function acts simultaneously as the **fitness function**, meaning the optimization target also determines the performance of each individual in the population. Although not ideal in real-world applications—where the fitness function often incorporates additional evaluation criteria—this approach simplifies the process for didactic purposes. Future versions aim to decouple these functions to better simulate practical scenarios.

.. rubric:: 2. Number of Experiments and Generations

Users can define how many **experiments** will be run under the same configuration, and for how many **generations** the population should evolve in each experiment. These settings allow users to observe consistency and variability in the GA's performance.

.. rubric:: 3. Population Size

The **population size** determines the number of candidate solutions maintained at each generation. A larger population enhances diversity but increases computational cost, while a smaller one accelerates execution at the risk of premature convergence.

.. rubric:: 4. Genetic Operators

- **Crossover Rate (%):** Specifies the probability of applying crossover between selected parents. GADemo provides multiple crossover methods: *One Point*, *Two Point*, and *Uniform*.
- **Mutation Rate (%):** Indicates the chance of introducing random modifications in offspring chromosomes, promoting exploration of the search space.

.. rubric:: 5. Variable Interval

Users can define the **lower and upper bounds** for each variable, restricting the search space. This ensures solutions remain within meaningful and computationally feasible domains.

.. rubric:: 6. Objective Direction

The optimization objective can be set to **maximize** or **minimize** the output of the objective function. This influences the selection process during evolution.

.. rubric:: 7. Elitism

When enabled, **elitism** preserves the best individuals from one generation to the next. This strategy prevents the loss of high-quality solutions and accelerates convergence.

.. rubric:: 8. Crossover Type

Users can choose among three crossover strategies:
- *One Point*: Splits chromosomes at a single position.
- *Two Point*: Splits at two points, swapping the segment between them.
- *Uniform*: Mixes genes from both parents based on a fixed probability.

.. rubric:: 9. Steady-State Strategy

GADemo supports three options for **steady-state evolution**:
- *OFF*: A generational replacement is performed.
- *Normal*: A fraction of the population is replaced per generation.
- *Without Duplicates*: Ensures that identical individuals are not reintroduced.

The `Gap (%)` field defines the percentage of the population to be replaced in steady-state mode.

---

This design enables students and practitioners to experiment with different GA configurations and immediately visualize their effects on convergence behavior, population diversity, and solution quality.
