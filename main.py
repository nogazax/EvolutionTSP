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

    # Initialize the evolutionary algorithm
    algo = SimpleEvolution(
        Subpopulation(creators=PermutationCreator(length=len(tspMatrix)),
                      population_size=50,
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
        max_generation=50,
        statistics=BestAverageWorstStatistics()
    )

    # evolve the generated initial population
    algo.evolve()
    # Execute (show) the best solution
    print(algo.execute())


if __name__ == '__main__':
    main()
