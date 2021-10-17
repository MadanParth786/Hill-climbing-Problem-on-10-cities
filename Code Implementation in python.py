#Implement travelling salesman problem.

import random 
def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []
    for i in range (len(tsp)):
        randomCity = cities[random.randint(0,len(cities)-1)]
        solution.append(randomCity)
        cities.remove(randomCity)
        
        
    return solution

def routeLen(tsp,solution):
    routelen =0
    for i in range(len(solution)):
        routelen += tsp[solution[i-1]] [solution[i]]
        
    return routelen    

def getneibours(solution):
    neibours =[]
    length =[]
    for i in range (len(solution)):
        for j in range (i+1,len(solution)):
            neibour = solution.copy()
            neibour[i] = solution[j]
            neibour[j] =solution[i]
            neibours.append(neibour)
            
     return neibours       
        

def getbestsoln(tsp,neibours):
    bestlen =routeLen(tsp,neibours[0])
    bestsoln = neibours[0]
    for neibour in neibours:
            currentroutelen =routeLen(tsp,neibour)
            if currentroutelen <bestlen:
                bestlen = currentroutelen
                bestsoln =neibour
                
    return bestsoln,bestlen    
    
    
    
    

def hillclimbing(tsp):
    print("Current Optimal(Random) Solution: ")
    currentsoln = randomSolution(tsp)
    print(currentsoln)
    currentroutelen =routeLen(tsp,currentsoln)
    print("Total Distance:")
    print(currentroutelen)
    neibour =getneibours(currentsoln)
    print("All possible solutions are: ")
    print(neibour)
    bestsolution ,bestsolutionlen  = getbestsoln(tsp,neibour)
    
    while bestsolutionlen <currentroutelen:
        currentsoln = bestsolution
        currentroutelen = bestsolutionlen
        bestsolution ,bestsolutionlen  = getbestsoln(tsp,neibour)
        print("Best Optimal Solution:")
    return currentsoln,currentroutelen                                       
        
                  
                  
def main():
    tsp = [ [0,231,71,572,722,431,233,155,462,712],
            [231,0,480,341,490,200,478,85,518,769],
            [711,480,0,307,254,281,963,592,989,1240],
            [572,341,307,0,196,143,825,454,851,1102],
            [722,490,254,196,0,291,974,602,999,1250],
            [431,200,281,143,291,0,684,312,710,960],
            [233,478,963,825,974,684,0,375,317,545],
            [155,85,592,454,602,312,375,0,514,764],
            [462,518,989,851,999,710,317,514,0,319],
            [712,769,1240,1102,1250,960,545,764,319,0]
          ]
    print(hillclimbing(tsp))
    
if __name__ == "__main__":
    main()
