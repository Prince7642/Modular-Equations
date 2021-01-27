# Python Program to find number of possible 
# values of X to satisfy P mod X = Q 
import math


# Returns the number of divisors of (P - Q)
# greater than Q
def calculateDivisors(P, Q):
    N = P - Q
    noOfDivisors = 0

    a = math.sqrt(N)
    for i in range(1, int(a + 1)):
        # if N is divisible by i
        if ((N % i == 0)):
            # count only the divisors greater than B
            if (i > Q):
                noOfDivisors += 1

            # checking if a divisor isnt counted twice
            if ((N / i) != i and (N / i) > Q):
                noOfDivisors += 1;

    return noOfDivisors


# Utility function to calculate number of all
# possible values of X for which the modular 
# equation holds true 

def numberOfPossibleWaysUtil(P, Q):
    # if P = Q there are infinitely many solutions
    # to equation or we say X can take infinitely
    # many values > A. We return -1 in this case
    if (P == Q):
        return -1

    # if P < Q, there are no possible values of
    # X satisfying the equation
    if (P < Q):
        return 0

    # the last case is when P > Q, here we calculate
    # the number of divisors of (P - Q), which are
    # greater than Q

    noOfDivisors = 0
    noOfDivisors = calculateDivisors;
    return noOfDivisors


# Wrapper function for numberOfPossibleWaysUtil() 
def numberOfPossibleWays(P, Q):
    noOfSolutions = numberOfPossibleWaysUtil(P, Q)

    # if infinitely many solutions available
    if (noOfSolutions == -1):
        print("For P = ", P, " and Q = ", Q
              , ", X can take Infinitely many values"
              , " greater than ", P)

    else:
        print("For P = ", P, " and Q = ", Q
              , ", X can take ", noOfSolutions
              , " values")
    # main()


P = 26
Q = 2
numberOfPossibleWays(P, Q)

P = 21
Q = 5
numberOfPossibleWays(P, Q)

# Contributed by _omg
