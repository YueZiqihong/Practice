# In the town of Cartesian Plains, NY, every resident's address is given by an  xx  and  yy  coordinate. I have a data file called "surveydata.txt", which contains the location of many of the town's residents, as well as their preference for Coke or Pepsi.
#
# I am scouting out locations to open a new deli, and I would like to know whether there are more Coke drinkers or Pepsi drinkers nearby, so that I can know what to carry. I would like a program where I can input an  xx -coordinate and a y-coordinate, and have as output the number of Coke drinkers and the number of Pepsi drinkers that are within a distance of 1 from the input point.
#

import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class Resident:

    def __init__(self,x,y,pref):
        self._x = float(x)
        self._y = float(y)
        self._pref = pref

    def distance(self,x,y):
        '''Return the distance between the resident and a certain place'''
        return math.sqrt( (self._x-x)**2 +(self._y-y)**2 )

    def is_nearby(self,x,y):
        '''Determine if a resident is within a distance of 1 to some place'''
        return self.distance(x,y) <= 1

    def pref(self):
        return self._pref.strip()

    def display(self):
        '''Display a resident's preference on the plot'''
        if self.pref() == 'Coke':
            plt.plot(self._x,self._y,'ro')
        elif self.pref() == 'Pepsi':
            plt.plot(self._x,self._y,'bo')

def main():
    Residents = []
    file = open('surveydata.txt','r')
    for line in file:
        info = line.split()
        Residents.append(Resident(info[0],info[1],info[2]) )
    file.close()

    x = float(input('Enter the x-coordinate: '))
    y = float(input('Enter the y-coordinate: '))
    count = {'Pepsi':0, 'Coke':0}
    plt.figure(figsize = (10,10))
    plt.title('Distribution of Pepsi and Coke fans')
    plt.axis('equal')

    for resident in Residents:
        resident.display()
        if resident.is_nearby(x,y):
            count[resident.pref()] += 1
    # Add legend
    red = mpatches.Patch(color='red', label='Coke')
    blue = mpatches.Patch(color='blue', label='Pepsi')
    plt.legend(bbox_to_anchor=(1.15, 1), handles=[blue,red], loc='upper right')
    # Show the nearby area
    plt.plot(x,y,'X')
    plt.gcf().gca().add_artist(plt.Circle((x,y),1,color='gray'))
    plt.show()
    for i in count:
        print('There are', count[i],'people who prefer', i,'within a distance of 1')

main()
