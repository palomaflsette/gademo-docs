******************************************
How GADemo Implements Genetic Algorithms?
******************************************

GADemo integrates a robust and modular implementation of Genetic Algorithms (GAs) using the `DEAP <https://deap.readthedocs.io/>`_ framework in Python. The platform allows users to define their own objective functions, which are directly used as fitness functions — a pragmatic choice for educational purposes, though in real-world applications, it is often ideal to separate the fitness evaluation from the objective function itself.

Upon receiving the function from the user, GADemo supports both single-variable and two-variable symbolic expressions, ensuring adaptability through symbolic processing with the **SymPy** library. Depending on the user's input, the platform dynamically creates individuals with either one or two genes (variables).

Core Implementation Aspects
----------------------------

- **Individual and Population Creation**:  
  Individuals are initialized with random values within user-defined intervals. The population is generated using ``deap.tools.initRepeat`` with appropriate gene sizes.

- **Selection, Crossover, and Mutation**:  
  - Selection is performed via **tournament selection**.  
  - Crossover operators include **one-point**, **two-point**, and **uniform crossover**, chosen based on user input.  
  - Mutation is implemented with **Gaussian noise**, bounded within specified limits.

- **Fitness Evaluation**:  
  The system evaluates each individual using the user-defined symbolic function, returning the value as a tuple to conform to DEAP’s expectations.

- **Fitness Normalization**:  
  Optionally, users can apply **linear normalization** to scale fitness values between arbitrary min-max ranges.

- **Steady-State Evolution**:  
  Users may enable steady-state reproduction modes, with or without duplicate removal, and configure the **gap** percentage controlling how many individuals are replaced per generation.

- **Elitism**:  
  An optional elitism strategy retains top-performing individuals across generations, with the number of elites dynamically determined based on the population size.

- **Parallel Execution**:  
  To increase robustness and enable comparative learning, GADemo supports **parallel execution of multiple experiments** using Python's ``concurrent.futures.ThreadPoolExecutor``.

At the end of the process, the platform collects and returns comprehensive data, including the best individuals per generation, final population fitness values, and aggregated statistics across experiments.