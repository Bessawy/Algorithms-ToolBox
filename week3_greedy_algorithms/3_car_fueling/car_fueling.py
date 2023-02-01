from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    location = 0
    current_tank = tank
    total = 0

    for stop in stops:
        #print("location: " + str(location) + " current_tank: " + str(current_tank))
        #print("next_stop: " + str(stop))
        #print("total: " + str(total))
    
        if(location + current_tank < stop):
            current_tank = tank
            total +=1

        if(location + current_tank >= d):
            return total

        if(location + current_tank >= stop):
            current_tank = current_tank - (stop - location)
            location = stop
        else:
            return -1


    if(location + current_tank >= d):
        return total
    elif(location + m >= d):
        return 1 + total
    else:
        return -1



if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
