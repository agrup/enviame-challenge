CADENA = 'afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood'

def contadorPalinromos(cadena):
    
    largoCadena = len(cadena)

    countsPalindormo = [[0 for x in range(largoCadena)] for y in range(largoCadena)]

    palindromo = [[False if x != y else True for x in range(largoCadena)] for y in range(largoCadena)]

    for i in range(largoCadena-1):
        if (cadena[i] == cadena[i+1]):
            countsPalindormo[i][i+1]= 1
            palindromo[i][i+1]= True

    for largoSubCadena in range(2, largoCadena):

        for x in range(largoCadena - largoSubCadena):

            dist = largoSubCadena + x
            if (cadena[x] == cadena[dist] and palindromo[x+1][dist-1]):
                palindromo[x][dist]= True

            if (palindromo[x][dist]):
                countsPalindormo[x][dist] = countsPalindormo[x][dist -1] +\
                    countsPalindormo[x+1][dist] +1 - countsPalindormo[x + 1][dist - 1]
            else:
                countsPalindormo[x][dist] = countsPalindormo[x][dist -1] +\
                    countsPalindormo[x+1][dist] - countsPalindormo[x + 1][dist - 1]
    # print(palindromo)
    # print(countsPalindormo)

    return countsPalindormo[0][largoCadena -1]


print(contadorPalinromos(CADENA))