import itertools

choiceMap = {}
def main():
    for i in range(1, 9):
        fileName = "choices_" + str(i)
        file = open(fileName, "r")
        choices = []
        raw = file.readlines()
        for txt in raw:
            choices.append( 8 - int(txt.strip()))
        choiceMap[i] = choices

    max = 0
    bestcombo = None
    bestoppcombo = None
    combos = list(itertools.combinations(range(1,9), 4))

    for combo in combos:
        oppCombo = validateAndGetOppCombo(combo)
        if ( oppCombo ):
            result = calculateScore(combo, oppCombo)

            diff = result
            if diff > max:
                max = diff
                bestcombo = combo
                bestoppcombo = oppCombo

    print(max)
    print(bestcombo)
    print(bestoppcombo)

def calculateScore(combo, oppCombo):
    cscore = calcCombo(combo)
    ocscore = calcCombo(oppCombo)
    return min(cscore, ocscore)
    diff = cscore + ocscore
    return [abs(diff), cscore, ocscore]

def calcCombo(combo):
    sumscore = 0
    pairs = list(itertools.combinations(list(combo), 2))
    for pair in pairs:
        p1 = pair[0]
        p2 = pair[1]
        sumscore += (choiceMap[p1][p2 - 1] * choiceMap[p2][p1 - 1]) * (choiceMap[p1][p2 - 1] * choiceMap[p2][p1 - 1])
    return sumscore

def validateAndGetOppCombo(combo):
    check = [False, False, False, False, False, False, False, False]
    seenOne = False
    seenTwo = False
    for i in combo:
        check[i - 1] = True
        if ( i == 1 ):
            seenOne = True
        if ( i == 2 ):
            seenTwo = True

    if seenOne and seenTwo:
        return False

    if not seenOne and not seenTwo:
        return False

    vals = []
    for i in range(0, 8):
        if not check[i]:
            vals.append(i + 1)
    return tuple(vals)



if __name__ == '__main__':
    main()
