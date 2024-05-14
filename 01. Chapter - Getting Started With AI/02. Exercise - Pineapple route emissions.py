portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# Nautical miles converted to km
D = [
    [0, 8943, 8019, 3652, 10545],
    [8943, 0, 2619, 6317, 2078],
    [8019, 2619, 0, 5836, 4939],
    [3652, 6317, 5836, 0, 7825],
    [10545, 2078, 4939, 7825, 0]
]

# CO2 emissions per km per metric ton
co2 = 0.020

# Initialize variables to store the smallest emissions and the best route
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def permutations(route, ports):
    global smallest, bestroute
    if len(ports) == 0:
        # Calculate the total distance for the current route
        distance = 0
        for i in range(len(route) - 1):
            distance += D[route[i]][route[i+1]]
        # Update the smallest distance and best route if the current one is better
        if distance < smallest:
            smallest = distance
            bestroute = route
    else:
        for i in range(len(ports)):
            permutations(route + [ports[i]], ports[:i] + ports[i+1:])

def main():
    global smallest
    # Start the permutation with the initial port PAN (index 0)
    permutations([0], list(range(1, len(portnames))))
    # Calculate CO2 emissions for the smallest distance
    smallest_emission = smallest * co2
    # Print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest_emission)

main()
