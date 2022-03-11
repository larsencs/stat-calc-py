#!/usr/bin/env python3
import math

def events(A, B):
    # Finds all available events for the variables A and B
    eventAnd = A * B
    eventOr = (A + B) - eventAnd
    conditionA = eventAnd / B
    conditionB = eventAnd / A
    if conditionA == A or conditionB == B:
        print("Variables are independent.")
    if eventAnd == 0:
        print("Events are mutually exclusive.")
    if A == 1 - B or B == 1 - A:
        print("Variables are complementary")
    print("[And Event]: ", eventAnd)
    print("[Or Event]: ", eventOr)
    print("[Conditional] (A | B): ", conditionA)
    print("[Conditional] (B | A): ", conditionB)

def zScore(X, Mu, Sigma):
    # finds the zScore given the variables of X, Mu, and Sigma
    zScore = (X - Mu) / Sigma
    return zScore

def lssr(A, B, X, operation):
    # Performs linear A +- (B * X) linear regression
    if operation == '+':
        yhat = A + (B * X)
    if operation == '-':
        yhat = A - (B * X)
    return yhat

def stDev(X, Mu, Sigma):
    # Finds the standard deviation given the variables X, mu, and Sigma
    stDeviation = (Mu + X) * Sigma
    return stDeviation

def sme(n):
    # finds the Simple Margin of Error given n
    sme = 1 / (math.sqrt(n))
    return sme

def smeSample(sme):
    # finds n given the Simple Margin of Error
    n = 1 / (math.sqrt(sme))
    return n

def cltSigma(P, n):
    # finds Sigma using Central Limit Theorem
    pSigma = math.sqrt(P * (1 - P))
    pSigma = pSigma / (math.sqrt(n))
    return pSigma

def cltMean(mean, sigma, n):
    # Central Limit Theorem for means only
    mean = mean * n
    sigma = sigma * (math.sqrt(n))
    return mean,sigma

def cltPop(P, n,):
    # Central Limit Theorem for populations
    pSigma = math.sqrt(P * (1 - P))
    pSigma = pSigma / (math.sqrt(n))
    return pSigma

def exValue():
    # Find the expected value for a set of data pairs
    pass
def slope(y,x):
    # Finds slope
    slope = y / x
    return slope

def cIntervalPop(sample, population, cInt, zScore):
    # Confidence intervals for populations
    pPrime = sample / population
    alpha = 1 - cInt
    alpha2 = alpha / 2
    stError = math.sqrt(pPrime * ((population - sample) / population) / population)
    moe = (zScore * stError)
    intervalOne = pPrime - moe
    intervalTwo = pPrime + moe
    return alpha, alpha2, stError, moe, intervalOne, intervalTwo, pPrime

def cIntervalMean(cInt, xbar, n, sigma, tDist):
    # Confidence intervals for means
    se = sigma / (math.sqrt(n))
    alpha = 1 - cInt
    alphaTwo = alpha / 2
    degree = n - 1
    moe = tDist * se
    intervalOne = xbar - moe
    intervalTwo = xbar + moe
    return se, alpha, alphaTwo, degree, moe, intervalOne, intervalTwo

def cIntervalPopMoe(pPrime, zInterval, margin):
    N = ((pPrime * (1 - pPrime)) * (math.pow(zInterval, 2))) / (math.pow(margin, 2))
    N2 = (math.ceil(N))
    return N, N2

def cIntervalMeanMoe():
    pass

def testHypoPop(n, x, pNot):
    # Performs tests of hypothesis
    pPrime = x / n
    z = (pPrime - pNot) / (math.sqrt(((pNot * (1 - pNot))) / n))
    return z

def testHypoMean(xbar, sigma, n, mean):
    t = (xbar - mean) / (sigma / (math.sqrt(n)))
    df = n - 1
    return t, df



print("[1] Events \n[2] Zscore \n[3] Linear Regression(LSSR) \n[4] Standard Deviation \n[5] Simple Margin of Error (SME) \n[6] Central Limit Theorem \n[7] Expected Value \n[8] Slope \n[9] Confidence Intervals \n[10] Test of Hypothesis")

choice = int(input("Choose an option: "))

while choice > 10 or choice < 1:
    choice = int(input("Choose an option: "))

if choice == 1:
    print("[1] Decimals \n[2] Fractions")
    choice = int(input("Choose and option: "))
    while choice > 3 or choice < 1:
        choice = int(input("Choose and option: "))
    if choice == 1:
        A = float(input("Enter A: "))
        B = float(input("Enter B: "))

        events(A,B)

    if choice == 2:
        anum = int(input("Enter A numerator: "))
        adenom = int(input("Enter A denominator: "))
        bnum = int(input("Enter B numerator: "))
        bdenom = int(input("Enter B denominator: "))

        A = anum / adenom
        B = bnum / bdenom

        events(A, B)

if choice == 2:
    X = float(input("Enter X: "))
    Mu = float(input("Enter Mu: "))
    Sigma = float(input("Enter Sigma: "))

    answer = zScore(X, Mu, Sigma)

    print("[Zscore]: ", answer)
if choice == 3:
    A = float(input("Enter A: "))
    B = float(input("Enter B: "))
    X = float(input("Enter X: "))
    operation = input("Enter operation (+/-): ")
    if operation == '+' or '-':
        yhat = lssr(A, B, X, operation)

        print("[yHat 1]: ", yhat)

    # if operation != '+' or '-':
    #     operation = input("Enter operation (+/-): ")



if choice == 4:
    X = float(input("Enter X: "))
    Mu = float(input("Enter Mu: "))
    Sigma = float(input("Enter Sigma: "))

    stDeviation = stDev(X, Mu, Sigma)

    print("[St. Deviation]: ", stDeviation)
if choice == 5:
    print("[1] for Simple Margin of Error \n[2] for finding n given a Simple Margin of Error ")
    choice = int(input("Choose an option: "))
    # while choice > 2 or choice < 1:
    #     choice = int(input("Choose an option: "))
    if choice == 1:
       n = int(input("Enter the value of n (sample size): "))

       sme = sme(n)

       print("[SME]: ", sme)
    if choice == 2:
        sme = float(input("Enter the Simple Margin of Error: "))

        n = smeSample(sme)

        print("[n]: ", n)
if choice == 6:
    print("[1] Standard Deviation \n[2] Sum Taken \n[3] Mean Taken")
    choice = int(input("Choose an option: "))
    while choice > 4 or choice < 1:
        choice = int(input("Choose an option: "))

    if choice == 1:
        P = float(input("Enter the value of P: "))
        n = int(input("Enter the value of n (Sample Size): "))

        pSigma = math.sqrt(P * (1 - P))

        pSigma = pSigma / (math.sqrt(n))

        print("[Sigma for Population]: ", pSigma)
    if choice == 2:
        mean = float(input("Enter mean: "))
        n = int(input("Enter the sample size: "))
        sigma = float(input("Enter given sigma: "))

        mean = mean * n
        sigma = sigma * (math.sqrt(n))
        print("[Mean]: ", mean)
        print("[Sigma]: ", sigma)

        choice = int(input("Do you need to find the probability of something? 0/1: "))
        if choice == 1:
            X = float(input("Enter the value of X: "))
            zScore = (X - mean) / sigma
            print("The zscore (if you are cursed with using a table) is: ", zScore)
            print("Otherwise, use the NormCDF function on your calculator.")
if choice == 7:
    choice = int(input("How many sets of data do you need to enter?: "))
    n = []
    p = []
    total = 0

    for num in range(0, choice):
        ndata = float(input("Enter data point for n: "))
        pdata = float(input("Enter data point for p (success rate): "))
        n.append(ndata)
        p.append(pdata)
    for i in range(0, choice):
        total += n[i] * p[i]
    exValue = total / choice
    print("[Expected Value]: ", exValue)
if choice == 8:
    x = float(input("Enter run (X): "))
    y = float(input("Enter rise (Y): "))

    slope = slope(y,x)

    print("[Slope]: ", slope)
if choice == 9:
    print("[1] Population \n[2]Mean \n[3] More Population \n[4] More Mean")
    choice = int(input("Choose an option: "))
    # while choice > 4 or choice < 1:
    #     choice = int(input("Choose an option: "))

    if choice == 1:
        cInt = float(input("Enter Confidence Interval: "))
        sample = int(input("Enter sample size: "))
        population = float(input("Enter population: "))

        print("Find zScore by using the zInterval function on your calculator \nStats >> tests >> zInterval(7) \nSet sigma to 1, xbar to 0, and n to 1")
        zScore = float(input("Enter zScore: "))

        results = cIntervalPop(sample, population, cInt, zScore)
        for alpha, alpha2, stError, intervalOne, intervalTwo, pPrime, moe in results:
            print("[Margin of Error]: ", moe)
            print("[Alpha]: ", alpha)
            print("[Alpha/2]: ", alpha2)
            print("[pPrime]: ", pPrime)
            print("[zScore]: ", zScore)
            print("[Std Error]: ", stError)
            print(intervalOne, " <= P <= ", intervalTwo)
            print("I am ", cInt * 100, " confident that the true population proportion <scenario text> is between ",
                  intervalOne, " and ", intervalTwo)
    if choice == 2:
        cInt = float(input("Enter Confidence Interval: "))
        xbar = float(input("Enter the value of Xbar: "))
        sigma = float(input("Enter the value of sigma: "))
        n = int(input("Enter the sample size (n): "))
        print("tDist can be found via your calculator: stat >> tests > Tinterval (8).  set xbar to 0, s = sqrt ", n, ", n = ",n)
        tDist = float(input("Enter the value of tDist: "))

        results = cIntervalMean(cInt, xbar, n, sigma, tDist)

        for se, alpha, alphaTwo, degree, moe, intervalOne, intervalTwo in results:
            print("[s]: ", sigma)
            print("[Degree of freedom]: ", degree)
            print("[Alpha]: ", alpha)
            print("[Alpha / 2]: ", alphaTwo)
            print("[SE](Standard Error): ", se)
            print("[TS]: ", tDist)
            print("[Margin of Error]: ", moe)
            print(intervalOne, " <= xbar <= ", intervalTwo)
            print("I am ", cInt, " confident that the  POPULATION MEAN <SCENARIO TEXT> is between ", intervalOne, " and ", intervalTwo)
    if choice == 3:
        pPrime = float(input("Enter the pPrime.  If you do not have a pPrime, assume 50%: " ))
        zInterval = float(input("Enter the Z Interval: "))
        margin = float(input("Enter the desired margin of error(this is found by taking 1/2 of the given width of the confidence interval): "))

        results = cIntervalPopMoe(pPrime, zInterval, margin)

        for N, N2 in results:
            print("[N]: ", N)
            print("[N2]: ", N2)

    if choice == 4:
        pass
if choice == 10:
    print("[1] for Population\n[2] for Mean")
    choice == int(input("Choose an option: "))

    # while choice != 1 or choice != 2:
    #     choice == int(input("Choose an option: "))

    if choice == 1:
        n = float(input("Enter the value of n (sample size): "))
        X = float(input("Enter the value of X: "))
        pNot = float(input("Enter the hypothesis in decimal format. If not given, assume 50%: "))

        results = testHypoPop(n, x, pNot, 0)

        print("[Z]: ", results)
        print("Enter that shit into normCDF as needed to find p-value")
    if choice == 2:
        xbar = float(input("Enter the value of xbar: "))
        sigma = float(input("Enter the value of sigma: "))
        n = float(input("Enter the value of n: "))
        mean = float(input("Enter the value of the mean: "))

        results = testHypoMean(xbar, sigma, n, mean)

        for t, df in results:
            print("[T]: ", t)
            print("[Degrees of Freedom]: ", df)
            print("Enter these values into tcdf to get your final answer. \n2nd Distr >> Tcdf(6)")











