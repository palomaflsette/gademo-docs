Stopping Criteria in Genetic Algorithms
=======================================

In the context of Genetic Algorithms (GAs), the stopping criterion determines **when the evolutionary process should be interrupted**. This decision plays a fundamental role in both the **efficiency** and **quality** of the final solution. Stopping too early may prevent the algorithm from reaching optimal solutions, while stopping too late may waste computational resources without any significant gain.

Common Stopping Criteria
-------------------------

There are several strategies used to define when a GA should stop. Each of them has its advantages and limitations, and the choice of which to adopt depends on the problem context and computational constraints:

- **Fixed number of generations**: The most common and simplest method. The algorithm stops after a predefined number of generations.  
  *Pros:* easy to implement and predictable in execution time.  
  *Cons:* does not consider whether the population has actually converged.

- **Fitness convergence**: The algorithm stops when the best fitness does not improve significantly over a certain number of generations.  
  *Pros:* avoids unnecessary iterations when no further improvement is occurring.  
  *Cons:* may be sensitive to noise or local optima.

- **Fitness threshold**: Stops when a solution reaches a desired fitness level.  
  *Pros:* goal-oriented.  
  *Cons:* requires prior knowledge of what constitutes an acceptable solution.

- **Evaluation budget**: Limits the number of fitness function evaluations instead of generations.  
  *Pros:* useful when evaluation is computationally expensive.  
  *Cons:* may be less intuitive to the user.

- **Time limit**: Stops after a certain amount of execution time.  
  *Pros:* ideal for real-time systems.  
  *Cons:* does not guarantee any quality of solution.

- **Diversity reduction**: Stops when the population becomes too homogeneous.  
  *Pros:* avoids premature convergence.  
  *Cons:* requires additional tracking of population diversity.

Stopping Criterion Used in GADemo
---------------------------------

GADemo adopts a **fixed number of generations** as its stopping criterion. This means that the user defines in advance how many generations the algorithm will run, regardless of whether the population is still improving or not.

.. code-block:: python

   for gen in range(exec_chars.num_generations):
       ...

This choice is deliberate and well-aligned with GADEMO’s purpose as an **educational and experimental platform**. It ensures that the execution is:

- **Deterministic and predictable**: making it easier to understand and analyze the effects of parameters.
- **Simpler to configure**: avoiding the need to define thresholds, tolerances or convergence heuristics.
- **Aligned with teaching goals**: allowing users to observe and compare how the population evolves over time, generation by generation.

While more advanced stopping criteria could be implemented in the future, the current approach keeps GADEMO accessible and focused on learning the core principles of Genetic Algorithms.

