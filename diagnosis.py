def diagnosis(ages, beha, loca, purp, park, usag, tire, wind, pain, keyl):
    phrase = []
    saveset = []
    saveset1 = []
    result = []
    if tire == 1:
        if ages > 10:
            if ages < 25:
                phrase.append((53, 0, 0, str(72.5833) + "% of people in your age choose BMW Tire & Wheel Services."))
            elif ages < 36:
                phrase.append((48, 0, 0, str(68.8480) + "% of people in your age choose BMW Tire & Wheel Services."))

            elif ages > 47 & ages < 58:

                phrase.append((40, 0, 1,
                               "Compared with our other services, people in your age prefer BMW Tire & Wheel Protection services."))
        if beha == 0:
            phrase.append(
                (60, 0, 1, "Considering your driving style, we recommend you to take an extra care on your tires."))
        if beha == 1:
            phrase.append(
                (46, 0, 0, str(75.594) + "% of people in your driving style choose BMW Tire & Wheel Services."))
        if beha == 2:
            phrase.append(
                (41, 0, 0, str(60.828) + "% of people in your driving style choose BMW Tire & Wheel Services."))

        if loca == 0:
            phrase.append((46, 0, 0, str(66.189) + "% of people in your region choose BMW Tire & Wheel Services."))

        if loca == 2:
            phrase.append((39, 0, 0, str(59.211) + "% of people in your region choose BMW Tire & Wheel Services."))
        if usag < 17 & usag > 6:
            phrase.append((45, 0, 1, "People with your weekly driving hours love BMW Tire & Wheel Protection."))
        if usag > 16:
            phrase.append(
                (47, 0, 0, "67.565 % of people with your weekly driving hours choose BMW Tire & Wheel Services."))
        if park in [0, 1, 2, 3, 4, 5, 6]:
            phrase.append((50, 0, 0, str(
                79.173) + "% of people with similar parking condition choose BMW Tire & Wheel Services."))

        if purp in [1, 2, 3, 4, 5, 6, 7, 8, 16, 17, 18, 19, 20, 21, 22, 23]:
            phrase.append(
                (51, 0, 0, "For people have your car usage, 71.990 % of them would choose BMW Tire & Wheel Services"))
        elif purp in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
            phrase.append(
                (52, 0, 0, "72.904 % of people who have similar car usage would choose BMW Tire & Wheel Services"))
        elif purp in [2, 3, 4, 5, 9, 10, 11, 12, 17, 18, 19, 20, 24, 25, 26, 27]:
            phrase.append(
                (64, 0, 0, "84.005 % of people who have similar car usage would like BMW Tire & Wheel Services"))

    if wind == 1:

        if ages > 76:
            phrase.append((65, 1, 1,
                           "Comparing with our other services, people in your age prefer BMW Windshield Protection Service."))
        if beha == 0:
            phrase.append(
                (40, 1, 1, "From our data in driving behavior, you should take an extra care on your windshield."))
        if beha == 1:
            phrase.append(
                (40, 1, 0, str(55.012) + "% of people in your driving style choose BMW Windshield Protection Service"))
        if beha == 2:
            phrase.append(
                (38, 1, 0, str(53.563) + "% of people in your driving style choose BMW Windshield Protection Service"))

        if loca == 2:
            phrase.append(
                (43, 1, 0, str(58.209) + "% of people in your region choose BMW Windshield Protection Service"))

        if loca == 3:
            phrase.append(
                (49, 1, 0, str(64.351) + "% of people in your region choose BMW Windshield Protection Service"))
        if usag < 17 & usag > 6:
            phrase.append((55, 1, 1,
                           "People with your weekly driving hours would like BMW Windshield Protection Service the most."))  #

        if park in [3, 5, 6, 9, 11, 12, 13]:
            phrase.append((60, 1, 0, str(
                75.339) + "% of people with your parking condition choose BMW Windshield Protection Service"))

        if park in [2, 4, 8, 10]:
            phrase.append((48, 1, 0, str(
                63.636) + "% of people with your parking condition choose BMW Windshield Protection Service"))  # 38
        if tire == 0:
            if purp in [2, 3, 4, 5, 9, 10, 11, 12, 17, 18, 19, 20, 24, 25, 26, 27]:
                phrase.append((39, 1, 0, str(
                    53.941) + "% of people with similar using purpose choose BMW Windshield Protection Service"))
    if keyl == 1:
        if ages > 47:
            phrase.append((58, 2, 1,
                           "People in your age have a relatively higher ratio in choosing BMW Key Protection Services "))

        if loca == 2:
            phrase.append((53, 2, 1,
                           "People in your region have a relatively higher ratio in choosing BMW Key Protection Services  "))

        if usag < 17:
            if usag > 6:
                phrase.append(
                    (53, 2, 1, "People with your weekly driving hours love BMW Key Protection Services the most."))
        if park in [1, 4, 5, 7, 10, 11, 12]:
            phrase.append(
                (50, 2, 1, "People with your parking condition like BMW Key Protection Services than other range does"))

        if tire == 0 & wind == 0 & pain == 0:
            if purp in [4, 5, 7, 8, 11, 12, 14, 15, 19, 20, 22, 23, 26, 27, 29, 30]:
                phrase.append((50, 2, 1,
                               "People with similar car usage have a relatively higher ratio in choosing BMW Key Protection Services "))

    if pain == 1:
        if ages > 10:
            if ages < 47 & ages > 36:
                phrase.append(
                    (42, 3, 0, str(62.362) + "% of people in your age choose BMW Paintless Dent Repair service"))
            elif ages < 36 & ages > 25:
                phrase.append(
                    (47, 3, 0, str(67.173) + "% of people in your age choose BMW Paintless Dent Repair service"))
            elif ages < 25:
                phrase.append((50, 3, 1,
                               "Comparing to other services, people in your age prefer BMW Paintless Dent Repair service."))
        if beha == 2:
            phrase.append(
                (41, 3, 0, str(61.117) + "% of people in your driving style choose BMW Paintless Dent Repair service"))

        if loca == 0:
            phrase.append(
                (45, 3, 0, str(65.628) + "% of people in your region choose BMW Paintless Dent Repair service"))

        if loca == 2:
            phrase.append(
                (44, 3, 0, str(64.023) + "% of people in your region choose BMW Paintless Dent Repair service"))

        if loca == 3:
            phrase.append(
                (43, 3, 0, str(63.246) + "% of people in your region choose BMW Paintless Dent Repair service."))

        if usag < 17 & usag > 6:
            phrase.append((43, 3, 0, str(
                63.063) + "% of people with your weekly driving hours choose BMW Paintless Dent Repair service."))

        if usag > 16:
            phrase.append((48, 3, 0,
                           "47.565 % of people who have the similar usage with you, choose our BMW Paintless Dent Repair service"))

        if park in [3, 5, 6, 9, 11, 12, 13]:
            phrase.append((60, 3, 0, str(
                80.107) + "% of people with similar parking condition of you choose BMW Paintless Dent Repair service"))

        if park in [2, 4, 8, 10]:
            phrase.append((40, 3, 0, str(
                59.956) + "% of people with your parking condition choose BMW Paintless Dent Repair service"))
        if tire == 0 & wind == 0 & purp in [1, 2, 3, 4, 5, 6, 7, 8, 16, 17, 18, 19, 20, 21, 22, 23]:
            phrase.append((45, 3, 1,
                           "Comparing to our services, people with your car usage prefer BMW Paintless Dent Repair service."))
    import heapq
    phrase = heapq.nlargest(len(phrase), phrase)
    save = [0, 0, 0, 0]
    for i in range(len(phrase)):
        save[phrase[i][1]] += 1
        if save[phrase[i][1]] < 3:
            saveset.append(phrase[i])
    save = [0, 0]
    for i in range(len(saveset)):
        save[saveset[i][2]] += 1
        if save[saveset[i][2]] < 3:
            saveset1.append(saveset[i])

    if len(saveset1) > 3:
        saveset1 = heapq.nlargest(3, saveset1)
    for i in saveset1:
        result.append(i[3])
    if tire == 1:
        result.append("You expect to save $800 by BMW Tire and Wheel Protection service.")
    if wind == 1:
        result.append("You could be able to save $400 by BMW Windshield Protection service.")
    if keyl == 1:
        result.append("BMW Key Protection services would prevent the yearly money loss of $700.")
    if pain == 1:
        result.append("BMW Paintless Dent Repair will decrease your cost $500 per year.")
    return result
diagnosis(78,0,1,1,16,10,1,0,1,0)
# ages,behavior,location,purpose,parking,usage,tire,windshield,painting,keyloss
