import random
from random import randint
import math

class UnboundedKnap_DA():
    def __init__(self):
        self.knapsack_weight= 0
        self.optimal_value = 0
        self.count = 0   #count of solution in
        self.items =[()]

    def individual(self, lenght):
        return [randint(0, 5) for x in range(lenght)]

    def population(self ,count):
        return [self.individual(len(self.items)) for x in range(count)]

    def fitness(self,individual, items):
        total_weight = total_value = 0
        for x in range(len(individual)):
           if individual[x] == 0:
              pass
           else:
              total_weight =(total_weight + items[x][0]*individual[x])
              total_value =(total_value+ items[x][1]*individual[x])
        if total_weight > self.knapsack_weight:
             total_value = 0
        return total_value

    def evolve(self ,pop, retain=0.2, random_select=0.05):
    # choose the best solution with percentage
       graded = [(self.fitness(x, self.items), x) for x in pop]  # [(fitness , [0110])]
       graded = [x[1] for x in sorted(graded, reverse=True)]
       retain_length = math.ceil(int(len(graded) * retain))
       parents = graded[:retain_length]
    # add another solution
       for individual in graded[retain_length:]:  # reminded solution
          if random_select > random.random():
             parents.append(individual)
    # mutation 0 <-> 5
       x_1 = graded[randint(0, len(graded) - 1)]
       x_2 = graded[randint(0, len(graded) - 1)]
       x_3 = graded[randint(0, len(graded) - 1)]
       x_diff = [x_2_i - x_3_i for x_2_i, x_3_i in zip(x_2, x_3)]
       v_donor = [x_1_i + randint(0, 2) * x_diff_i for x_1_i, x_diff_i in zip(x_1, x_diff)]
       for i in range(len(v_donor) ):
         if v_donor[i] < 0:
            v_donor[i] = 0
         elif v_donor[i] > 5:
            v_donor[i] = 5
       parents.append(v_donor)
    # crossover from the selected solution and generate new population
       parents_len = len(parents)
       remind_len = len(pop) - parents_len
       children = []
       while len(children) < remind_len:
        male = randint(0, len(parents) - 1)
        female = randint(0, len(parents) - 1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = round(len(male) / 2)
            child = male[:half] + female[half:]
            children.append(child)

       parents.extend(children)
       return parents

    def run ( self,items ,knapsack_weight , count):
       self.items = items
       self.knapsack_weight = knapsack_weight
       self.count = count

       pop = self.population(count)
       for x in range(1000):
         pop=self.evolve(pop)
       print("the optimal solution after 1000 generation is ",pop[0])
       return pop[0]