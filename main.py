from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
from permGA import PermutationCreator, TSPEvaluator, PermutationCrossover, PermutationMutation


def main():

    tspMatrix = [ [0, 10, 15, 20],
                  [10, 0, 35, 25],
                  [15, 35, 0, 30],
                  [20, 25, 30, 0]]

    population_size = 50
    max_generation = 50
    # Initialize the evolutionary algorithm
    algo = SimpleEvolution(
        Subpopulation(creators=PermutationCreator(length=len(tspMatrix)),
                      population_size=population_size,
                      # user-defined fitness evaluation method
                      evaluator=TSPEvaluator(tspMatrix),
                      # maximization problem (fitness is sum of values), so higher fitness is better
                      higher_is_better=False,
                      elitism_rate=0.0,
                      # genetic operators sequence to be applied in each generation
                      operators_sequence=[
                          PermutationCrossover(),
                          PermutationMutation(swap_Probability=0.05)  # swap two random cities with prob ()
                      ],
                      selection_methods=[
                          # (selection method, selection probability) tuple
                          (TournamentSelection(tournament_size=4, higher_is_better=False), 1)
                      ]),
        breeder=SimpleBreeder(),
        max_workers=1,
        max_generation=max_generation,
        statistics=BestAverageWorstStatistics()
    )
    print("EA Process Presented Bellow:")

    # evolve the generated initial population
    algo.evolve()
    print("#####################################")

    print("The Ultimate solution found by our solver is:")
    algo.finish()

if __name__ == '__main__':
    main()
