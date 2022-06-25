import random
from random import randint
import math

class knapsack_GA():   
    def __init__(self):
        self.knapsack_weight= 0
        self.optimal_value = 0
        self.count = 0   #count of solution in
        self.items =[()]

    def individual(self,lenght):
        return [randint(0,1) for x in range(lenght)]

    def population(self,count):
        return [self.individual(len(self.items)) for x in range(count)]

    def fitness (self,individual , items):
        total_weight=total_value=0
        for x in range(len(individual)):
            if individual[x] == 0:
                pass
            else:
                total_weight += items[x][0]
                total_value += items[x][1]
        if total_weight > self.knapsack_weight:
            total_value = 0
        return total_value

    def evolve(self ,pop, retain=0.2, random_select=0.05, mutate=0.01):
        #choice best solution with persentage 
        graded = [(self.fitness(x,self.items), x) for x in pop ] #[(fitness , [0110])]
        graded = [x[1] for x in sorted(graded ,  reverse=True)]
        retain_length = math.ceil(int(len(graded)*retain))
        parents = graded[:retain_length]

        #add another solution
        for individual in graded[retain_length:]: #reminded solution
            if random_select > random.random():
                parents.append(individual)

        #mutation 0 <-> 1 
        for individual in parents:
            if mutate > random.random(): 
                index_to_mutate = randint(0, len(individual)-1)
                if individual[index_to_mutate] == 1:
                    individual[index_to_mutate] = 0
                else:
                    individual[index_to_mutate] = 1
        
        #crossover from the selected solution and generate new population
        parents_len = len(parents)
        remind_len = len(pop) - parents_len
        children = []
        while len(children) < remind_len:
            male = randint(0 , len(parents)-1)
            female = randint(0 , len(parents)-1)
            if male != female:
                male = parents[male]
                female = parents[female]
                half = round(len(male) / 2)
                child = male[:half] + female[half:]
                children.append(child)
        
        parents.extend(children)
        return parents

    def run (self , items ,knapsack_weight , count):
        #initial values 
        self.items = items
        self.knapsack_weight = knapsack_weight
        self.count = count
        for x in range(len(items)):
            self.optimal_value += items[x][1]

        #initial population
        initial_pop = self.population(count) 
        p = initial_pop
        #stop find solution after 30 iteration 
        for x in range(30):
            p = self.evolve(p)
        #print all fitness in population to test but we will print max fitness
        for x in p:
            final_results =[(self.fitness(x ,items) , x)]
        final_results = [x[1] for x in sorted(final_results ,  reverse=True)] #sort to ensure the optimal in the first
        print("The optimal solution after 20 itiration is {} with value {}".format(final_results[0] , self.fitness(final_results[0],items)))
        return final_results[0]