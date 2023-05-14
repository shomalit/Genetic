import random


class misisters :

    def make_Population(self) :
        '''Make first genaration of Damon's Minesters'''
        population=[]   #main list 
        chromoz=[]      #shows where's each minister(index),Column
        for _ in range(20):
            for _ in range(8):
                chromoz.append(random.randint(0,1))
            population.append(chromoz)
            chromoz=[]
        print(f'{len(population)} Chromosomes has made successfuly !')
        for item in population:
            print(item)
            
a=misisters()
a.make_Population()