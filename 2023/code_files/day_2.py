import sys

def p1():
    red = 12
    green = 13
    blue = 14

    filename = sys.argv[1]
    f = open(filename, "r")

    sumids = 0
    id=1

    for line in f.readlines():
        valid = True
        print('Game', id)
        line2 = line.split(':')[1].strip()
        game = line2.split(';')
        print(game)

        for trial in game:
            handfuls = trial.split(',')
            print(handfuls)

            for handful in handfuls:
                handful = handful.strip().split()
            
                if handful[1] == 'green':
                    if int(handful[0]) > 13:
                        valid = False
                elif handful[1] == 'red':
                    print('HIELO')
                    if int(handful[0]) > 12:
                        valid = False
                elif handful[1] == 'blue':
                    if int(handful[0]) > 14:
                        valid = False
                print(valid)

        if valid:
            sumids += id
            print('valid')
                    

        id = id +1

    f.close()

    print(sumids)

def p2():

    ans = 0

    filename = sys.argv[1]
    f = open(filename, "r")
    for line in f.readlines():
        line2 = line.split(':')[1].strip()
        game = line2.split(';')
        print(game)

        rmax = 0
        gmax = 0
        bmax = 0

        for trial in game:
            handfuls = trial.split(',')
            for handful in handfuls:
                handful = handful.strip().split()
                if handful[1] == 'green':
                    if int(handful[0]) > gmax:
                        gmax = int(handful[0])
                elif handful[1] == 'red':
                    if int(handful[0]) > rmax:
                        rmax = int(handful[0])
                elif handful[1] == 'blue':
                    if int(handful[0]) > bmax:
                        bmax = int(handful[0])
        
        print(rmax, gmax, bmax)
        ans += rmax*gmax*bmax
    print(ans)

p2()