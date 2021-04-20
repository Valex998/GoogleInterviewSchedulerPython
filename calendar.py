calendar1 = [['09:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
boundaries1 = ['09:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
boundaries2 = ['10:00', '18:30']
interviewTime = 30
bookedTimes = []
freeTimes = []
totalBoundary = []

def formatMinutesOnly(schedule):   #formatam orele in minute pentru a fi mai usor de comparat
    i = 0
    while i < len(schedule):
        j = 0
        while j < len(schedule[i]):
            hour, minutes = schedule[i][j].split(':')
            schedule[i][j] = int(hour)*60 + int(minutes)
            j+=1
        i+=1

def formatBoundaryMinutesOnly(boundary):   #formatam intervalele de activitate in minute
    i = 0
    while i < len(boundary):
        hour, minutes = boundary[i].split(':')
        boundary[i] = int(hour)*60 + int(minutes)
        i += 1


formatMinutesOnly(calendar1)
formatMinutesOnly(calendar2)
formatBoundaryMinutesOnly(boundaries1)
formatBoundaryMinutesOnly(boundaries2)

def compareTimes(time1, time2):   #comparam 2 ore intre ele, made it for quality of life
    if time1 > time2:
        return 1
    elif time1 < time2:
        return -1
    else:
        return 0

def uniteBooked(schedule1, schedule2):  #reunim partile ocupate din program din cele 2 calendare
    i = 0
    j = 0
    while i < len(schedule1) and j < len(schedule2):
        if compareTimes(schedule1[i][0], schedule2[j][0]) == -1:
            bookedTimes.append(schedule1[i])
            i += 1
        elif compareTimes(schedule1[i][0], schedule2[j][0]) == 1:
            bookedTimes.append(schedule2[j])
            j += 1
        elif compareTimes(schedule1[i][1], schedule2[j][1]) == 1:
            bookedTimes.append(schedule1[i])
            i += 1
        else:
            bookedTimes.append(schedule2[j])
            j += 1
    l = 0
    while l < len(bookedTimes) - 1:
            end1 = bookedTimes[l][1]
            start2 = bookedTimes[l+1][0]
            end2 = bookedTimes[l+1][1]
            if compareTimes(end1, start2) == 1:
                if compareTimes(end1, end2) == 1:
                    bookedTimes.pop(l+1)
                else:
                    bookedTimes[l][1] = end2
                    bookedTimes.pop(l+1)
            l +=1

if compareTimes(boundaries1[0], boundaries2[0]) == 1:   # verificam care este intervalul comun de lucru
    totalBoundary.append(boundaries1[0])
else:
    totalBoundary.append(boundaries2[0])

if compareTimes(boundaries1[1], boundaries2[1]) == 1:
    totalBoundary.append(boundaries2[1])
else:
    totalBoundary.append(boundaries1[1])



uniteBooked(calendar1, calendar2)


if totalBoundary[0] < bookedTimes[0][0] and bookedTimes[0][0] - totalBoundary[0] >= 30:  #timp liber intre inceputul programului de lucru si prima ocupatie
    freeTimes.append([totalBoundary[0], bookedTimes[0][0]])

x = 0

while x < len(bookedTimes) - 1:                                                         #timp liber intre ocupatii
    if bookedTimes[x + 1][0] - bookedTimes[x][1] >= 30:
        freeTimes.append([bookedTimes[x][1], bookedTimes[x+1][0]])
    x += 1

if totalBoundary[1] > bookedTimes[len(bookedTimes)-1][1] and totalBoundary[1] - bookedTimes[len(bookedTimes)-1][1] >= 30: #timp liber intre ultima ocupatie si finalul programului de lucru
    freeTimes.append([bookedTimes[len(bookedTimes)-1][1], totalBoundary[1]])

for i in range(len(freeTimes)):         #schimbam timpul inapoi in format 24h
    for j in range(len(freeTimes[i])):
        hour = freeTimes[i][j] // 60
        minute = freeTimes[i][j] % 60
        freeTimes[i][j] = f"{hour}:{minute}"
        if minute == 0:
            freeTimes[i][j] = f"{hour}:00"




print(freeTimes)