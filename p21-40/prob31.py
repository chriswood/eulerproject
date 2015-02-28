#In England the currency is made up of pound, £, and pence, p, and there are
#eight coins in general circulation:
#
#    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#
#It is possible to make £2 in the following way:
#
#    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
#How many different ways can £2 be made using any number of coins?
#£ = Q
# 2Q
# 1Q + 50p + 50p
# 1Q + 50p + 20p + 20p + 5p + 5p

coins = [1,2,5,10,20,50,100,200]

#a*1+b*2+c*5+d*10+e*25+f*50+g*100+h*200
combos = 0
for h in range(2):
    for g in range(3):
        for f in range(5):
            for e in range(11):
                print("g={0},f={1}, e={2}".format(g,f,e))
                for d in range(21):
                    for c in range(41):
                        for b in range(101):
                            for a in range(201):
                                if a*1 + b*2 + c*5 + d*10 + e*20 + f*50 + g*100 + h*200 == 200:
                                    #print("{0}-1 -10 {1}-25 {2}-50 {3}-100 {4}-200".format(a,b,c,d,e,f,g,h))
                                    combos += 1

print("{0} combinations".format(combos))
