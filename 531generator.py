import numpy as np
import pickle
import csv

def makeLift(name, baseweight, musclegroups, interval):
    """
       str, float, str, float -> dict of dicts
       loads lift dictionary from file, creates a new dictionary
       subentry in master dictionary of lifts, then pickles the dictionary
    """
    #if it exists, open the liftdict file
    try:
        with open('lifts.pkl','rb') as infile:
            liftdict = pickle.load(infile)
    except:
        print('Lifts Dictionary not found!  Initializing new database...')
        liftdict = {}
    #create the subdictionary entry using the information passed to function
    dictentry = {'Starting Weight': baseweight, 'Current Weight': baseweight, 'Muscle Groups':musclegroups,
                 'Loading Interval': interval}
    #add entry to main dictionary
    liftdict[name] = dictentry
    #pickle the dict file
    print('Saving dictionary...')
    with open('lifts.pkl', 'wb') as outfile:
        pickle.dump(liftdict, outfile, -1)
    print('Success!')


def roundToPlate(weight, micro = False):
    """
    float -> float
    Takes a postive float and rounds it to the nearest possible
    barbell weight. By default, will round to the nearest 5lb
    increment, but can round to the nearest 2.5lb possible weight
    when micro is set to True.
    >>>roundToPlate(51)
    50
    >>>roundToPlate(54)
    55
    >>>roundToPlate(52, micro = True)
    52.5
    """
#set smallest plate size
    if micro == True:
        smallplate = 2.5
    else:
        smallplate = 5
#first, check to see if the weight is already rounded and can
#be returned directly; otherwise continue
    if weight % smallplate == 0:
        return weight
    else:
        pass
#determine whether to round up or down based on remainder
    if weight % smallplate >= smallplate/2:
        roundup = True
    else:
        roundup = False
#generate final value based on rounding rules
    if roundup == True:
        weight = weight + smallplate - (weight % smallplate)
        return weight
    else:
        weight = weight - (weight % smallplate)
        return weight

def percentWeight(max,percent,micro = False):
    """
    float -> float
    returns the weight value for a given percentage
    of the max weight for the lift
    >>>percentWeight(100,65)
    65.0
    >>>percentWeight(100,72.6)
    75.0
    >>>percentWeight(100,72.6, micro = True)
    72.5
    """
    liftweight = max * (percent/100)
    return roundToPlate(liftweight, micro)

class Week:
    def __init__(self,week):
        self.week = week

    def percents(week):
        """
        int -> 3x1 array
        Returns the three percentages for a given week's lifts.
        """
        if week == 1:
            return np.array([65,75,85])
        if week == 2:
            return np.array([70,80,90])
        if week == 3:
            return np.array([75,85,95])
        else:
            return np.array([40,50,60])
    def reps(week):
        """
        int -> 3x1 array
        Returns the three rep ranges for a given week's lifts.
        """
        if week == 1:
            return np.array([5,5,5])
        if week == 2:
            return np.array([3,3,3])
        if week == 3:
            return np.array([5,3,1])
        else:
            return np.array([5,5,5])


def weekOutput(weekNumber, maxWeight, micro = False):
    weekArray = Week.percents(weekNumber)
    for w in weekArray:
        print('Lift:', w,': ', percentWeight(maxWeight,w, micro = micro))


# class Lift:
#     def __init__(self,lift):
#         self.name = lift
