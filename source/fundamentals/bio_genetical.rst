Biological Genetics and Its Analogy in Genetic Algorithms
=========================================================

To better understand how Genetic Algorithms (GAs) work, it is useful to draw parallels with concepts from biological genetics. This analogy allows us to view the optimization process as an evolutionary system, where individuals (solutions) are evaluated, selected, recombined, and mutated over generations. The table below summarizes the most relevant biological terms and their corresponding interpretations within the context of GAs:

.. list-table:: Comparison Between Biological Genetics and Genetic Algorithms
   :header-rows: 1
   :widths: 20 25 35 40

   * - Biological Term 🧫
     - GA Equivalent 🤖
     - Meaning in Genetic Algorithms
     - Practical Example (GADEMO)

   * - Gene
     - Variable in the solution
     - A single unit of encoded information; represents a variable in the objective function
     - In ``f(x, y)``, the genes are ``x`` and ``y``

   * - Allele
     - Value of a gene
     - The specific value assigned to a variable (gene)
     - If ``x = 2.3``, then the allele of gene ``x`` is ``2.3``

   * - Chromosome
     - Individual / Candidate solution
     - A complete vector containing all genes (i.e., the full solution)
     - Chromosome = ``[x, y] = [2.3, 1.1]``

   * - Population
     - Set of candidate solutions
     - Group of chromosomes (individuals) evaluated in the same generation
     - Population = 5 chromosomes = 5 possible solutions

   * - Genome
     - Search space
     - The range of all possible genes and alleles, defined by the variable bounds
     - Ranges: ``x ∈ [0,4]``, ``y ∈ [0,4]``

   * - Sexual reproduction
     - Crossover
     - Combination of genes from two parents to generate offspring
     - Average of parents: ``[1.0, 2.0]`` + ``[3.0, 0.0]`` → ``[2.0, 1.0]``

   * - Genetic mutation
     - Mutation
     - Random alteration in one or more gene values (alleles)
     - Change ``x = 2.0`` to ``x = 2.2``

   * - Natural selection
     - Selection (e.g., tournament, roulette)
     - Process of choosing parents based on their fitness (quality)
     - Individuals with higher fitness are more likely to reproduce

   * - Biological fitness
     - Fitness
     - Measure of how well a solution solves the problem (objective function value)
     - ``f(x, y) = x² + y²``; if ``x = 2, y = 2``, then fitness = 8

   * - Evolution
     - Iteration of generations
     - Gradual improvement of the population through genetic operations
     - Each generation tends to perform better than the previous one

Additional Biological Terms in the Context of Genetic Algorithms
----------------------------------------------------------------

Some additional terms from classical genetics are also relevant in the context of Genetic Algorithms, especially when considering encoding strategies:

.. list-table:: Supplementary Biological Analogies in GAs
   :header-rows: 1
   :widths: 20 25 45

   * - Biological Term
     - GA Equivalent
     - Explanation

   * - Locus
     - Bit or variable position
     - Specific position of a gene or bit in the chromosome vector; used especially in binary representations

   * - Genotype
     - Encoded candidate solution
     - The internal representation of a solution, such as a binary string or real-valued vector

   * - Phenotype
     - Evaluated solution
     - The expressed result of the genotype when passed through the objective function, i.e., ``f(x)``
