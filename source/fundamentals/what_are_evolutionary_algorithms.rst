**********************************
What Are Evolutionary Algorithms?
**********************************

Evolutionary Algorithms (EAs) are computational tools inspired by natural evolutionary processes. These algorithms are widely applied to complex problem-solving, leveraging mechanisms such as selection, mutation, and crossover to iteratively improve candidate solutions.

The foundational idea, introduced by Holland (1975), is to simulate evolution through a population of candidate solutions that evolve over time. Inspired by Darwinian principles such as "survival of the fittest," EAs evaluate each individual based on its fitness within a problem environment, promoting those that best solve the task at hand.

Goldberg (1989) further developed these ideas, structuring the process around a series of genetic operators that guide the evolution. The resulting method balances exploration and exploitation, iterating until a satisfactory solution is found. Schwefel (1995) and Michalewicz (1997) reinforced the algorithm's adaptability across domains.

This pseudocode outlines the general structure of a standard Genetic Algorithm. The process begins with the initialization of a random population of candidate solutions. In each iteration, individuals are evaluated according to a fitness function, and a subset of the population is selected to undergo genetic operations such as crossover and mutation. The resulting offspring are combined with the existing population, and a selection step determines which individuals survive to the next generation. This iterative cycle continues until a termination condition is met, such as reaching a maximum number of generations or achieving a satisfactory fitness level.

.. code-block:: python

    Algorithm 1: Genetic Algorithm Pseudocode

    Initialize population P(t) at time t = 0

    while (termination condition not met):
        Evaluate fitness of individuals in P(t)
        
        P’ ← Select parents from P(t)
        P’’ ← Apply genetic operators (crossover, mutation) to P’

        P(t+1) ← Select survivors from P ∪ P’’
        t ← t + 1
