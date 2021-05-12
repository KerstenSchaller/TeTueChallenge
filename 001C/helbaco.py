# -*- coding: utf-8 -*-
import timeit

'''
Attention: to measure the runtime we use the module timeit. For this the complete code should be in a string at the end.
'''

test_code = '''
import time
class player:
    def __init__(self, name, secrets=0, playtime_s=0, kills=0):
        self.gameid = int(time.time()*10000) # create unique id
        self.name = name
        self.secrets = secrets
        self.playtime_s = playtime_s # playing time in seconds
        self.kills = kills



def main():
    list_player = [player("Max", 3, 50, 10), player("Moritz", 2, 20, 30), player("Witwe Bolte", 3, 49, 9), player("Mecke", 1, 10, 79), player("Lämpel", 3, 49, 10), player("Fritz", 2, 20, 31), player("Böck", 1, 10, 80)]
    
    print('unsorted list')
    for p in list_player:
        print(p.secrets, p.playtime_s, p.kills, p.name)

    print('secrets ascending')
    for p in sorted(list_player, key=lambda obj: obj.secrets):
        print(p.secrets, p.name)

    print('playtime decending')
    for p in sorted(list_player, key=lambda obj: obj.playtime_s, reverse=True):
        print(p.playtime_s, p.name)

    print('kills ascending')
    for p in sorted(list_player, key=lambda obj: obj.kills):
        print(p.kills, p.name)

if __name__ == "__main__":
    main()
'''
laufzeit = timeit.Timer(test_code)
print(laufzeit.repeat(repeat=5, number=1))
