
# EvolvingLikePokemon

## Intro
The project handles TSP (traveling salesman) problem using Evolutionary Algorithm. To implement EA we used the EC-KitY package.

We chose to solve the following version of TSP problem:
- The agent is allowed to choose the starting city.
- Each passage is valid (all cities are connected).

## Implementation Details
To map the TSP problem to EA we used the following:

**Genotype** - the Phenotype will be represented as a permutation array of all numbers in [0, numOfCities-1]. The permutation will define the order of cities visited, when the first entry is the starting city. So **Valid Genotype** will be defined a valid permutation as described before.

**Initial Population** - is created as random permutations (random genotypes).

**Fitness** - will be defined as the sum of distances between the cities based on the order defined in the genotype. Best fitness will be defined as the minimal one.

**Selection Method** - Tournament based, using size of 4. 

**Used Operators**: (both keep the resulting genotype valid)

- Crossover - We "mixed" between 2 different genotypes. We took the first 20% of the entries in each genotype and swapped it with the other. Then, in order to keep it a legal permutation, we filled the other 80% according to the original's order of the values in the genotype.
I.E: [1,2,3,4,5] and [5,4,3,2,1]  yield - [5,1,2,3,4] and [1,4,3,2,5] respectively.

- Mutation - for the new generation created by crossover, we'll mutate each entity with probability of 0.05. mutation is implemeted by choosing 2 random indices, and swaping their values.


## Using Our Solver

In order to use our TSP solver, please follow the following steps:

- Clone our git repository

- Swap the *tspMatrix* parameter to a value of your choosing. Note that it should be a 2D, [n,n] array, with non-negative values and zero diagonal. Entry [i,j] in the array will define the distance between city i and city j.

- Feel free to change the *max_generation* and *population_size* variables to any positive integer.

- Run the script. The result will be presented, same as the process log.


*Our git folder includes the current (as of 16.7.22) EC-Kity version (using fork from the git) to use EA abilities that were not yet published.
https://github.com/EC-KitY/EC-KitY/tree/c9c38c5616e99af7214580e1a962af7f173b647d*


### Citation
```
@misc{eckity2022git,
    author = {Sipper, Moshe and Halperin, Tomer and Tzruia, Itai and  Elyasaf, Achiya},
    title = {{EC-KitY}: Evolutionary Computation Tool Kit in {Python}},
    year = {2022},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://www.eckity.org/} }
}
