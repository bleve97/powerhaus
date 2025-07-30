import math

class barbell:
    def __init__(self, weight=20.0, name="barbell",available=False):
        self.weight = int(weight)
        self.name = name
        self.available = False  # default to not having it

class plate:
    def __init__(self, weight, colour='black'):
        self.weight = float(weight)
        self.colour = colour

class collar:
    def __init__(self, weight=2.5): # a metal Oly collar is 2.5kg per pair, the plastic ones are maybe 200g?
        self.weight = float(weight)

class squatWarmupWeights:
    def __init__(self, barbellWeight=20.0, worksetWeight=100.0):
        self.worksetWeight = worksetWeight
        self.barbellWeight = barbellWeight
        loads = self.normalCalc(worksetWeight)
        self.first = barbellWeight  # 2 x 5 reps or 1 x 10 reps
        self.second  # 40% 5 reps
        self.third    # 60% 5 reps
        self.forth    # 80% 2 reps
        self.secondPerSide
        self.thirdPerSide
        self.forthPerSide
        self.worksetPerSide

        self.increments = 2.5   # 1.25 x 2, standard 1.25kg plates
        self.smallIncrements = 0.5  # change plates, smallest we have is 250g
        self.minRestTimeMins = 3

    def normalCalc(self, worksetWeight):
        self.second = worksetWeight * 0.4
        self.third = worksetWeight * 0.6
        self.forth = worksetWeight * 0.8
        if self.second <= self.barbellWeight:
            print("bugger! second set should be ", self.second)
            self.second = (self.worksetWeight - self.barbellWeight) * 0.3 + self.barbellWeight
            self.third = (self.worksetWeight - self.barbellWeight) * 0.5 + self.barbellWeight
            self.forth = (self.worksetWeight - self.barbellWeight) * 0.8 + self.barbellWeight

        self.second = self.saneWeight(self.second)
        self.third = self.saneWeight(self.third)
        self.forth = self.saneWeight(self.forth)
        self.worksetPerSide = (self.worksetWeight - self.barbellWeight) / 2.0
        self.secondPerSide = (self.second - self.barbellWeight) / 2.0
        self.thirdPerSide = (self.third - self.barbellWeight) / 2.0
        self.forthPerSide = (self.forth - self.barbellWeight) / 2.0
        return True

    def saneWeight(self, weight, increment=2.5):
        # returns a weight that's a multiple of the increment, rounded up, so the lifter can
        # use the weights in the gym.  Typically 2.5kg is the smallest step unless you
        # have fractionals, 2.5 being 2 1.25kg plates. Duh maffs hard ...

        numOfIncs = math.ceil(weight/increment)
        rem = math.remainder(weight, increment)
        saneWeight = float(numOfIncs * increment)
        # print("weight :", weight, "inc :", increment, "number? : ", numOfIncs, saneWeight, rem)
        return saneWeight

class BBLoad:
    def __init__(self, load=20, barweight=20, availweights=[25.0,20.0,15.0,10.0,5.0,2.5,1.25]):
        self.barweight = barweight
        self.availweights = availaweights
        self.requiredLoad = load - barweight
        self.eachside = 0

        # https://en.wikipedia.org/wiki/Barbell#Bumper_plates
        self.WeightColours = {25 : 'Red', 20 : 'Blue', 15 : 'Yellow', 10 : 'Green', 5 : 'White',
                              2.5 : 'Red', 2 : 'Blue', 1.5 : 'Yellow', 1 : 'Green', 1.25 : 'Black', 0.5 : 'White'}

        if self.requiredLoad == 0:  # the no load case
            self.eachside = 0


