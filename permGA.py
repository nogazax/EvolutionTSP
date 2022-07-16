import numpy as np

from eckity.genetic_encodings.ga.vector_individual import Vector
from eckity.genetic_operators.genetic_operator import GeneticOperator

from eckity.creators.ga_creators.simple_vector_creator import GAVectorCreator
from eckity.genetic_encodings.ga.int_vector import IntVector
from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator


import itertools

class PermutationCreator(GAVectorCreator):
    def __init__(self,
                 length = 1,
                 events=None):
        super().__init__(length, None, (0,length), IntVector, events)

    def create_vector(self, individual):
        perm = list(np.random.permutation(individual.length))
        individual.set_vector(perm)



#asuming even number of inidividuals
class PermutationCrossover(GeneticOperator):
    def __init__(self):
        self.applied_individuals = None
        super().__init__(arity = 2)

    def apply(self, individuals):
        for i in range(0, len(individuals) - 1, 2):
            if (i+1<len(individuals)):
                individuals[i], individuals[i+1] = self.cross(individuals[i], individuals[i+1])
        self.applied_individuals = individuals
        return individuals



    def cross(self, individual1 : Vector, individual2 : Vector):
        totalLength = individual1.length
        length_of_section = int(totalLength / 5)
        firstSection = individual1.get_vector_part(0, length_of_section)
        secondSection = individual2.get_vector_part(0, length_of_section)

        for i in range(totalLength):
            first_in_i = individual1.cell_value(i)
            if (first_in_i not in firstSection):
                firstSection.append(first_in_i)
            second_in_i = individual2.cell_value(i)
            if (second_in_i not in secondSection):
                secondSection.append((second_in_i))
        individual1.set_vector(firstSection)
        individual2.set_vector(secondSection)
        return individual1, individual2


class PermutationMutation(GeneticOperator):
    def __init__(self, swap_Probability):
        super().__init__( arity=1, probability=swap_Probability)
        self.applied_individuals = None

    def apply(self, individuals: list[Vector]):
        for ind in individuals:
            range = ind.length
            swapping_indices = np.random.choice(range, 2, replace=False)
            firstval = ind.cell_value(swapping_indices[0])
            secondVal = ind.cell_value(swapping_indices[1])
            ind.set_cell_value(swapping_indices[0], secondVal)
            ind.set_cell_value(swapping_indices[1], firstval)
        self.applied_individuals = individuals

        return individuals


class TSPEvaluator(SimpleIndividualEvaluator):
    def __init__(self, cities_matrix):
        super().__init__()
        self.cities_matrix = cities_matrix

    def _evaluate_individual(self, individual):
        """
        Compute the fitness value of a given individual.
        Parameters
        ----------
        individual: Vector
            The individual to compute the fitness value for.
        Returns
        -------
        float
            The evaluated fitness value of the given individual.
        """
        value = 0.0
        for i in range(individual.length-1):
            orig = individual.cell_value(i)
            dest = individual.cell_value(i + 1)
            if orig >= 0 and orig < len(self.cities_matrix) and dest >= 0 and dest < len(self.cities_matrix):
                value += self.cities_matrix[orig][dest]

        return value
