import random


def growth(year=2022, population=7850000000, ratio=0,cur_pop=10000000000,n=0):

        new_year = year + 1
        ratio = new_year // year
        cur_pop = population * ratio ^ (n-1)
        print(n)
        #print(random.randint(year,population))


growth()
