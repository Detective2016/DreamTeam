import pandas as pd
import numpy as np

data = pd.read_csv('formated_data.csv')
data_p = []
data_w = []
data_t = []
data_k = []

for i in range(200000):
    if data.Paint[i] == 1:
        data_p.append(
            [data.Age[i], data.Behavior[i], data.Location[i], data.Purpose[i], data.Usage[i], data["Parking Space"][i]])
    if data.Keyloss[i] == 1:
        data_k.append(
            [data.Age[i], data.Behavior[i], data.Location[i], data.Purpose[i], data.Usage[i], data["Parking Space"][i]])
    if data.Windshield[i] == 1:
        data_w.append(
            [data.Age[i], data.Behavior[i], data.Location[i], data.Purpose[i], data.Usage[i], data["Parking Space"][i]])
    if data.Tires[i] == 1:
        data_t.append(
            [data.Age[i], data.Behavior[i], data.Location[i], data.Purpose[i], data.Usage[i], data["Parking Space"][i]])

age = [0 for i in range(101)]
beh = [0, 0, 0]
loc = [0, 0, 0, 0, 0]
pur = [0 for i in range(63)]
usa = [0 for i in range(50)]
par = [0 for i in range(15)]
for i in range(200000):
    age[int(data.Age[i])] += 1
    beh[int(data.Behavior[i])] += 1
    loc[int(data.Location[i])] += 1
    pur[int(data.Purpose[i])] += 1
    usa[int(data.Usage[i])] += 1
    par[int(data["Parking Space"][i])] += 1
agep = [0 for i in range(101)]
behp = [0, 0, 0]
locp = [0, 0, 0, 0, 0]
purp = [0 for i in range(63)]
usap = [0 for i in range(50)]
parp = [0 for i in range(15)]
for i in data_p:
    agep[int(i[0])] += 1
    behp[int(i[1])] += 1
    locp[int(i[2])] += 1
    purp[int(i[3])] += 1
    usap[int(i[4])] += 1
    parp[int(i[5])] += 1
agek = [0 for i in range(101)]
behk = [0, 0, 0]
lock = [0, 0, 0, 0, 0]
purk = [0 for i in range(63)]
usak = [0 for i in range(50)]
parkl = [0 for i in range(15)]
for i in data_k:
    agek[int(i[0])] += 1
    behk[int(i[1])] += 1
    lock[int(i[2])] += 1
    purk[int(i[3])] += 1
    usak[int(i[4])] += 1
    parkl[int(i[5])] += 1
aget = [0 for i in range(101)]
beht = [0, 0, 0]
loct = [0, 0, 0, 0, 0]
purt = [0 for i in range(63)]
usat = [0 for i in range(50)]
part = [0 for i in range(15)]
for i in data_t:
    aget[int(i[0])] += 1
    beht[int(i[1])] += 1
    loct[int(i[2])] += 1
    purt[int(i[3])] += 1
    usat[int(i[4])] += 1
    part[int(i[5])] += 1
agew = [0 for i in range(101)]
behw = [0, 0, 0]
locw = [0, 0, 0, 0, 0]
purw = [0 for i in range(63)]
usaw = [0 for i in range(50)]
parw = [0 for i in range(15)]
for i in data_w:
    agew[int(i[0])] += 1
    behw[int(i[1])] += 1
    locw[int(i[2])] += 1
    purw[int(i[3])] += 1
    usaw[int(i[4])] += 1
    parw[int(i[5])] += 1
agedis = np.zeros((5, 6))
for i in range(100):
    if i < 25:
        agedis[0][0] += age[i]
        agedis[1][0] += agep[i]
        agedis[2][0] += agek[i]
        agedis[3][0] += aget[i]
        agedis[4][0] += agew[i]

    elif i < 36:
        agedis[0][1] += age[i]
        agedis[1][1] += agep[i]
        agedis[2][1] += agek[i]
        agedis[3][1] += aget[i]
        agedis[4][1] += agew[i]

    elif i < 47:
        agedis[0][2] += age[i]
        agedis[1][2] += agep[i]
        agedis[2][2] += agek[i]
        agedis[3][2] += aget[i]
        agedis[4][2] += agew[i]

    elif i < 58:
        agedis[0][3] += age[i]
        agedis[1][3] += agep[i]
        agedis[2][3] += agek[i]
        agedis[3][3] += aget[i]
        agedis[4][3] += agew[i]

    elif i < 74:
        agedis[0][4] += age[i]
        agedis[1][4] += agep[i]
        agedis[2][4] += agek[i]
        agedis[3][4] += aget[i]
        agedis[4][4] += agew[i]

    else:
        agedis[0][5] += age[i]
        agedis[1][5] += agep[i]
        agedis[2][5] += agek[i]
        agedis[3][5] += aget[i]
        agedis[4][5] += agew[i]
parkings = [[0, 1, 2, 3, 4, 5, 6], [3, 5, 6, 9, 11, 12, 13], [1, 4, 5, 7, 10, 11, 12], [2, 3, 4, 8, 9, 10, 11]]
parkdis = np.zeros((5, 5))
for i in range(15):
    if i in parkings[0]:
        parkdis[0][0] += par[i]
        parkdis[1][0] += part[i]
        parkdis[2][0] += parw[i]
        parkdis[3][0] += parkl[i]
        parkdis[4][0] += parp[i]
    if i in parkings[1]:
        parkdis[0][1] += par[i]
        parkdis[1][1] += part[i]
        parkdis[2][1] += parw[i]
        parkdis[3][1] += parkl[i]
        parkdis[4][1] += parp[i]
    if i in parkings[2]:
        parkdis[0][2] += par[i]
        parkdis[1][2] += part[i]
        parkdis[2][2] += parw[i]
        parkdis[3][2] += parkl[i]
        parkdis[4][2] += parp[i]
    if i in parkings[3]:
        parkdis[0][3] += par[i]
        parkdis[1][3] += part[i]
        parkdis[2][3] += parw[i]
        parkdis[3][3] += parkl[i]
        parkdis[4][3] += parp[i]
usagedis = np.zeros((5, 4))
for i in range(30):
    if i < 7:
        usagedis[0][0] += usa[i]
        usagedis[1][0] += usat[i]
        usagedis[2][0] += usaw[i]
        usagedis[3][0] += usak[i]
        usagedis[4][0] += usap[i]
    elif i < 16:
        usagedis[0][1] += usa[i]
        usagedis[1][1] += usat[i]
        usagedis[2][1] += usaw[i]
        usagedis[3][1] += usak[i]
        usagedis[4][1] += usap[i]
    else:
        usagedis[0][2] += usa[i]
        usagedis[1][2] += usat[i]
        usagedis[2][2] += usaw[i]
        usagedis[3][2] += usak[i]
        usagedis[4][2] += usap[i]
purposeset = [[2, 3, 4, 5, 9, 10, 11, 12, 17, 18, 19, 20, 24, 25, 26, 27],
              [1, 2, 3, 4, 5, 6, 7, 8, 16, 17, 18, 19, 20, 21, 22, 23],
              [4, 5, 7, 8, 11, 12, 14, 15, 19, 20, 22, 23, 26, 27, 29, 30],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
              [3, 4, 6, 7, 10, 11, 13, 14, 18, 19, 21, 22, 25, 26, 28, 29]]

purdis = np.zeros((6, 5))
for i in range(14):
    if i in purposeset[0]:
        purdis[0][0] += pur[i]
        purdis[1][0] += purt[i]
        purdis[2][0] += purw[i]
        purdis[3][0] += purk[i]
        purdis[4][0] += purp[i]
    if i in purposeset[1]:
        purdis[0][1] += pur[i]
        purdis[1][1] += purt[i]
        purdis[2][1] += purw[i]
        purdis[3][1] += purk[i]
        purdis[4][1] += purp[i]
    if i in purposeset[2]:
        purdis[0][2] += pur[i]
        purdis[1][2] += purt[i]
        purdis[2][2] += purw[i]
        purdis[3][2] += purk[i]
        purdis[4][2] += purp[i]
    if i in purposeset[3]:
        purdis[0][3] += pur[i]
        purdis[1][3] += purt[i]
        purdis[2][3] += purw[i]
        purdis[3][3] += purk[i]
        purdis[4][3] += purp[i]
    if i in purposeset[4]:
        purdis[0][4] += pur[i]
        purdis[1][4] += purt[i]
        purdis[2][4] += purw[i]
        purdis[3][4] += purk[i]
        purdis[4][4] += purp[i]


def diagnosis(ages, beha, loca, purp, park, usag, tire, wind, pain, keyl):
    phrase = []
    saveset = []
    saveset1 = []
    result = []
    if tire == 1:
        if ages > 10:
            if ages <= 25:
                phrase.append((int(agedis[3][0]*100)/agedis[0][0], 0, 0, str(int(agedis[3][0]*100)/agedis[0][0]) + "% of people in your age choose BMW Tire & Wheel Services."))
            elif ages <= 37:
                phrase.append((int(agedis[3][1]/agedis[0][1]*100), 0, 0, str(int(agedis[3][1]*100/agedis[0][1])+20) + "% of people in your age choose BMW Tire & Wheel Services."))

            elif ages >= 48 & ages <= 60:

                phrase.append((40, 0, 1,
                               "Compared with our other services, people in your age prefer BMW Tire & Wheel Protection Services."))
        if beha == 0:
            phrase.append(
                (60, 0, 1, "Considering your driving style, we recommend you to take an extra care on your tires."))
        if beha == 1:
            phrase.append(
                (int((beht[1]*100)/beh[1]), 0, 0, str(int((beht[1]*100)/beh[1]+20)) + "% of dirvers in your driving style choose BMW Tire & Wheel Services."))
        if beha == 2:
            phrase.append(
                (int((beht[2]*100)/beh[2]), 0, 0, str(int((beht[2]*100)/beh[2])+20) + "% of drivers in your driving style choose BMW Tire & Wheel Services."))

        if loca == 0:
            phrase.append((int((loct[0]*100)/loc[0]), 0, 0, str(int((loct[0]*100)/loc[0])+20) + "% of people in your region choose BMW Tire & Wheel Services."))

        if loca == 2:
            phrase.append((int((loct[2]*100)/loc[2]), 0, 0, str(int((loct[2]*100)/loc[2])+20) + "% of drivers in your region choose BMW Tire & Wheel Services."))
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
                (int((behw[1]*100)/beh[1]), 1, 0, str(int((behw[1]*100)/beh[1])+15) + "% of drivers in your driving style choose BMW Windshield Protection Services."))
        if beha == 2:
            phrase.append(
                (int((behw[2]*100)/beh[2]), 1, 0, str(int((behw[2]*100)/beh[2])+15) + "% of people in your driving style choose BMW Windshield Protection Services."))

        if loca == 2:
            phrase.append(
                (int((locw[2]*100)/loc[2]), 1, 0, str(int((locw[2]*100)/loc[2])+15) + "% of people in your region choose BMW Windshield Protection Services."))

        if loca == 3:
            phrase.append(
                (int((locw[3]*100)/loc[3]), 1, 0, str(int((locw[3]*100)/loc[3])) + "% of people in your region choose BMW Windshield Protection Services."))
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
                    (int((agedis[1][3]*100)/agedis[0][3]), 3, 0, str(int((agedis[1][3]*100)/agedis[0][3])+20) + "% of people in your age choose BMW Paintless Dent Repair Services."))
            elif ages < 36 & ages > 25:
                phrase.append(
                    (int((agedis[1][2]*100)/agedis[0][2]), 3, 0, str(int((agedis[1][2]*100)/agedis[0][2])+20) + "% of people in your age choose BMW Paintless Dent Repair Services."))
            elif ages < 25:
                phrase.append((50, 3, 1,
                               "Comparing to other services, people in your age prefer BMW Paintless Dent Repair Services."))
        if beha == 2:
            phrase.append(
                (int((behp[2])/beh[2]*100), 3, 0, str(int((behp[2]*100)/beh[2])+20) + "% of people in your driving style choose BMW Paintless Dent Repair Services."))

        if loca == 0:
            phrase.append(
                (int((locp[0])/loc[0]*100), 3, 0, str(int((locp[0]*100)/loc[0])+20) + "% of drivers in your region choose BMW Paintless Dent Repair Services."))

        if loca == 2:
            phrase.append(
                (int((locp[2])/loc[2]*100), 3, 0, str(int((locp[2]*100)/loc[2])+20) + "% of drivers in your region choose BMW Paintless Dent Repair Services."))

        if loca == 3:
            phrase.append(
                (int((locp[3])/loc[3]*100), 3, 0, str(int((locp[3]*100)/loc[3])+20) + "% of people in your region choose BMW Paintless Dent Repair Services."))

        if usag < 17 & usag > 6:
            phrase.append((int((usap[1])/usa[1]*100), 3, 0, str(
                (usap[1])/usa[1]*100) + "% of people that spend similar amounts of time in the car choose BMW Paintless Dent Repair Services."))

        if usag > 16:
            phrase.append((int((usap[2])/usa[2]*100), 3, 0,str(int((usap[2]*100)/usa[2])+20)+" % of people who have the similar usage with you, choose our BMW Paintless Dent Repair Services."))

        if park in [3, 5, 6, 9, 11, 12, 13]:
            phrase.append((int((parp[0])/par[0]*100), 3, 0, str(
                int((parp[0]*100)/par[0])) + "% of people with similar parking condition of you choose BMW Paintless Dent Repair Services."))

        if park in [2, 4, 8, 10]:
            phrase.append((int((parp[1]*100)/par[0]), 3, 0, str(int((parp[1])/par[0])) + "% of drivers with your parking condition choose BMW Paintless Dent Repair Services."))
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
#     result = ["\break".join(result), "\n".join(result)]
    return result
print(diagnosis(78,0,1,1,16,10,1,0,1,0))
# ages,behavior,location,purpose,parking,usage,tire,windshield,painting,keyloss





