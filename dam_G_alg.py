import random
from random import shuffle
from random import seed
from collections import Counter


class misisters :

    def make_Population(self) :

        '''Make first genaration of Damon's Minesters'''
        population=[]   #main list 
        chromoz=[0,1,2,3,4,5,6,7]      #shows where's each minister(index),Column
        for i in range(20):
            seed(i*2)
            shuffle(chromoz)
            population.append(chromoz)
            
        print(f'{len(population)} Chromosomes has made successfuly !')
        #for item in population:
        #    print(item)
        return population
            
    def chooice_Best_parents(self):
        '''Select Best Parrents and save them for copy !'''
        sequence=[]   # Ministers columns situation
        gen_Score=[]
        population_List = misisters.make_Population(self)
        for item in population_List :
            #freq_dict=Counter(item)
            print(f'genes and report= {item} ')

        print('cho')


# call
a=misisters()
a.chooice_Best_parents()