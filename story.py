from random import randint
def story():
    myHP = 10
    print("Právě jsi se vzbudil v jakési cele, nemáš sebemenší tušení, jak ses tam dostal. Nevzpomínáš si, co se předešlé noci stalo.")
    print("Dveře tvé cely jsou z neznámého důvodu otevřeny.")
    print("Blíží se první rozhodnutí. Možnosti budou vždy označeny -takto-. Prosím vepiš je na určené místo ve stejném tvaru, v jakém je uvidíš.")
    decide = input("Můžeš svou celu -opustit-, nebo v ní -zůstat- a snažit se vzpomenout si na události, které k tomuto bodu vedly. Pro co se rozhodneš? ")
    while decide == "zůstat":
        print("Ani po chvíli usilovného vzpomínání tě nic nenapadá. Nechceš se raději projít?")
        decide = input("Můžeš svou celu -opustit- nebo v ní -zůstat- ještě chvíli. Pro co se rozhodneš? ")
    else:
        print("Vyšel jsi ze své cely, a octl jsi se v malé chodbě s několika otevřenými dveřmi od různých cel.")
        print("Tvou pozornost upoutaly troje dveře na druhém konci chodby.")
        print("Cestou k nim sis všiml meče ležícího na zemi. Když ho sebereš, může ti pomoct.")
        decide = input("Chceš jej -sebrat- nebo jej -nechat- ležet? ")
        if decide == "sebrat":
            print("Sebral jsi meč, a pokračoval ke dveřím.")
            hasSword = True
        else:
            print("Rezavý meč ti za námahu nestál, proto ses vydal rovnou ke dveřím.")
            hasSword = False
        i = randint(0, 2)
        j = randint(0, 2)
        while j == i:
            j = randint(0, 2)
        else:
            doors = ["nalevo", "napravo", "naproti"]
            lock = doors[i]
            fight = doors[j]
            decide = input("Jedny dveře jsou -napravo-, druhé -nalevo- a třetí -naproti-. Které otevřeš? ")
            while decide == lock:
                print("Hmm, tyto dveře jsou zamčeny. Budeš muset zkusit nějaké jiné.")
                decide = input("Pro které dveře se rozhodneš?")
            else:
                if decide == "nalevo":
                    print("Otevřel jsi dveře nalevo.")
                elif decide == "napravo":
                    print("Otevřel jsi dveře napravo. ")
                else:
                    print("Otevřel jsi dveře naproti tobě.")
                if decide == fight:
                    print("Jen, co jsi vešel do místnosti, vrhl se na tebe goblin!")
                    goblinHP = 10
                    myHP -= 1
                    while goblinHP > 0 and myHP > 0:
                        print("Po goblinově útoku ti zbývá " + str(myHP) + " životů. Teď máš šanci mu to vrátit.")
                        decide = input("Můžeš -zaútočit- nebo se -krýt-. Co chceš udělat? ")
                        if hasSword == True and decide == "zaútočit":
                            print("Zaútočil jsi na goblina.")
                            gob = randint(1, 10)
                            if gob == "10":
                                print("Ten se ale tvému útoku vyhl a zasadil ti další ránu.")
                                myHP -= 1
                                print("Goblinovi zbývá " + str(goblinHP) + " životů.")
                            else:
                                print("Tvůj útok byl úspěšný.")
                                swo = randint(1, 4)
                                if swo == "4":
                                    goblinHP -= 3
                                    print("Goblinovi zbývá " + str(goblinHP) + " životů.")
                                    myHP -= 1
                                else:
                                    goblinHP -= 2
                                    print("Goblinovi zbývá " + str(goblinHP) + " životů.")
                                    myHP -= 1
                        elif hasSword == False and decide == "zaútočit":
                            print("Zaútočil jsi na goblina.")
                            gob = randint(1, 10)
                            if gob == "10":
                                print("Ten se ale tvému útoku vyhl a zasadil ti další ránu.")
                                myHP -= 1
                            else:
                                print("Tvůj útok byl úspěšný.")
                                goblinHP -= 1
                                print("Goblinovi zbývá " + str(goblinHP) + " životů.")
                                myHP -= 1
                        else:
                            me = randint(1, 10)
                            if me == "1":
                                print("Pokusil ses uhnout, ale goblin byl příliš rychlý.")
                                myHP -= 1
                            elif me == "10":
                                print("Tvé vyhnutí se zmátlo goblina natolik, že při útoku narazil hlavou do zdi.")
                                goblinHP -= 1
                                print("Goblinovi zbývá " + str(goblinHP) + " životů.")
                            else:
                                print("Úspěšně ses vyhl goblinovu útoku.")
                    else:
                        if myHP == 0:
                            print("Snažil ses, ale goblin byl nad tvé síly.")
                        else:
                            print("Dalo to práci, ale goblina jsi nakonec porazil.")
                            print("Zde příběh zatím končí. Děkujeme za hru.")
                else:
                    print("Vešel jsi do prázdné místnosti.")
                    print("Zde příběh zatím končí. Děkujeme za hru.")

story()
again = input("Chcete hrát znovu? a/n ")
while again == "a":
    story()
    again = input("Chcete hrát znovu? a/n ")

