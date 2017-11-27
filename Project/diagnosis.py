def diagnosis(ages, beha, loca, purp, park, usag, tire, wind, pain, keyl):
    phrase = []
    saveset = []
    saveset1 = []
    result = []
    if tire == 1:
        if ages > 10:
            if ages <= 25:
                phrase.append((53, 0, 0, str(72) + "% of people in your age choose BMW Tire & Wheel Services."))
            elif ages <= 37:
                phrase.append((48, 0, 0, str(68) + "% of people in your age choose BMW Tire & Wheel Services."))

            elif ages >= 48 & ages <= 60:

                phrase.append((40, 0, 1,
                               "Compared with our other services, people in your age prefer BMW Tire & Wheel Protection Services."))
        if beha == 0:
            phrase.append(
                (60, 0, 1, "Considering your driving style, we recommend you to take an extra care on your tires."))
        if beha == 1:
            phrase.append(
                (46, 0, 0, str(75) + "% of dirvers in your driving style choose BMW Tire & Wheel Services."))
        if beha == 2:
            phrase.append(
                (41, 0, 0, str(60) + "% of drivers in your driving style choose BMW Tire & Wheel Services."))

        if loca == 0:
            phrase.append((46, 0, 0, str(66) + "% of people in your region choose BMW Tire & Wheel Services."))

        if loca == 2:
            phrase.append((39, 0, 0, str(59) + "% of drivers in your region choose BMW Tire & Wheel Services."))
        if usag < 17 & usag > 6:
            phrase.append((45, 0, 1, "Drivers that spend similar amounts of time in the car benefited the most from BMW Tire & Wheel Protection Services."))
        if usag > 16:
            phrase.append(
                (47, 0, 0, "67 % of people that spend similar amounts of time in the car choose BMW Tire & Wheel Services."))
        if park in [0, 1, 2, 3, 4, 5, 6]:
            phrase.append((50, 0, 0, str(
                79) + "% of people with similar parking condition choose BMW Tire & Wheel Services."))

        if purp in [1, 2, 3, 4, 5, 6, 7, 8, 16, 17, 18, 19, 20, 21, 22, 23]:
            phrase.append(
                (51, 0, 0, "For drivers with similar primary car usage, 71 % of them would choose BMW Tire & Wheel Services."))
        elif purp in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
            phrase.append(
                (52, 0, 0, "72 % of people who have similar primary car usage would choose BMW Tire & Wheel Services."))
        elif purp in [2, 3, 4, 5, 9, 10, 11, 12, 17, 18, 19, 20, 24, 25, 26, 27]:
            phrase.append(
                (64, 0, 0, "84 % of people who have similar primary car usage would like BMW Tire & Wheel Services."))

    if wind == 1:

        if ages >= 60:
            phrase.append((45, 1, 1,
                           "Comparing with our other services, people in your age prefer BMW Windshield Protection Services."))
        if beha == 0:
            phrase.append(
                (40, 1, 1, "From our data in driving behavior, you should take an extra care on your windshield."))
        if beha == 1:
            phrase.append(
                (40, 1, 0, str(55) + "% of drivers in your driving style choose BMW Windshield Protection Services."))
        if beha == 2:
            phrase.append(
                (38, 1, 0, str(53) + "% of people in your driving style choose BMW Windshield Protection Services."))

        if loca == 2:
            phrase.append(
                (43, 1, 0, str(58) + "% of people in your region choose BMW Windshield Protection Services."))

        if loca == 3:
            phrase.append(
                (49, 1, 0, str(64) + "% of people in your region choose BMW Windshield Protection Services."))
        if usag < 17 & usag > 6:
            phrase.append((55, 1, 1,
                           "People that spend similar amounts of time in the car benefited the most from BMW Windshield Protection Services."))  #

        if park in [3, 5, 6, 9, 11, 12, 13]:
            phrase.append((60, 1, 0, str(
                75) + "% of drivers with your parking condition choose BMW Windshield Protection Services."))

        if park in [2, 4, 8, 10]:
            phrase.append((48, 1, 0, str(
                63) + "% of drivers with your parking condition choose BMW Windshield Protection Services."))  # 38
        if tire == 0:
            if purp in [2, 3, 4, 5, 9, 10, 11, 12, 17, 18, 19, 20, 24, 25, 26, 27]:
                phrase.append((39, 1, 0, str(
                    53) + "% of people with similar primary car usage choose BMW Windshield Protection Services."))
    if keyl == 1:
        if ages >= 47:
            phrase.append((68, 2, 1,
                           "Drivers in your age have a relatively higher ratio in choosing BMW Key Protection Services. "))

        if loca == 2:
            phrase.append((53, 2, 1,
                           "People in your region have a relatively higher ratio in choosing BMW Key Protection Services.  "))

        if usag < 17:
            if usag > 6:
                phrase.append(
                    (53, 2, 1, "Drivers that spend similar amounts of time in the car benefited the most from BMW Key Protection Services."))
        if park in [1, 4, 5, 7, 10, 11, 12]:
            phrase.append(
                (50, 2, 1, "People with your parking condition like BMW Key Protection Services."))

        if tire == 0 & wind == 0 & pain == 0:
            if purp in [4, 5, 7, 8, 11, 12, 14, 15, 19, 20, 22, 23, 26, 27, 29, 30]:
                phrase.append((50, 2, 1,
                               "People with similar primary car usage are likely to choose BMW Key Protection Services. "))

    if pain == 1:
        if ages > 10:
            if ages <= 47 & ages >= 37:
                phrase.append(
                    (42, 3, 0, str(62) + "% of people in your age choose BMW Paintless Dent Repair Services."))
            elif ages < 36 & ages > 25:
                phrase.append(
                    (47, 3, 0, str(67) + "% of people in your age choose BMW Paintless Dent Repair Services."))
            elif ages < 25:
                phrase.append((50, 3, 1,
                               "Comparing to other services, people in your age prefer BMW Paintless Dent Repair Services."))
        if beha == 2:
            phrase.append(
                (41, 3, 0, str(61) + "% of people in your driving style choose BMW Paintless Dent Repair Services."))

        if loca == 0:
            phrase.append(
                (45, 3, 0, str(65) + "% of drivers in your region choose BMW Paintless Dent Repair Services."))

        if loca == 2:
            phrase.append(
                (44, 3, 0, str(64) + "% of drivers in your region choose BMW Paintless Dent Repair Services."))

        if loca == 3:
            phrase.append(
                (43, 3, 0, str(63) + "% of people in your region choose BMW Paintless Dent Repair Services."))

        if usag < 17 & usag > 6:
            phrase.append((43, 3, 0, str(
                63) + "% of people that spend similar amounts of time in the car choose BMW Paintless Dent Repair Services."))

        if usag > 16:
            phrase.append((48, 3, 0,
                           "47 % of people who have the similar usage with you, choose our BMW Paintless Dent Repair Services."))

        if park in [3, 5, 6, 9, 11, 12, 13]:
            phrase.append((60, 3, 0, str(
                80) + "% of people with similar parking condition of you choose BMW Paintless Dent Repair Services."))

        if park in [2, 4, 8, 10]:
            phrase.append((40, 3, 0, str(
                59) + "% of drivers with your parking condition choose BMW Paintless Dent Repair Services."))
        if tire == 0 & wind == 0 & purp in [1, 2, 3, 4, 5, 6, 7, 8, 16, 17, 18, 19, 20, 21, 22, 23]:
            phrase.append((45, 3, 1,
                           "Comparing to our services, people with similar primary car usage prefer BMW Paintless Dent Repair Services."))
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
        result.append("You expect to save $800 from BMW Tire and Wheel Protection Services.")
    if wind == 1:
        result.append("You could be able to save about $400 from BMW Windshield Protection Services.")
    if keyl == 1:
        result.append("BMW Key Protection Services would save you upto $700 per year.")
    if pain == 1:
        result.append("BMW Paintless Dent Repair Services would save you about $500 per year.")
    result = "\n".join(result)
    return result
#diagnosis(78,0,1,1,16,10,1,0,1,0)
# ages,behavior,location,purpose,parking,usage,tire,windshield,painting,keyloss



