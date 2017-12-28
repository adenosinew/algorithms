def minion_game(string):
    vowel_list = []
    consonant_list = []
    kevin_point , stuart_point = 0 , 0
    for i in range(len(string)):
        if string[i] in ['A','E','I','O','U']:
            kevin_point += len(string) - i
        else:
            stuart_point += len(string) - i
    if stuart_point > kevin_point:
        print('Stuart %d'%stuart_point)
    elif stuart_point == kevin_point:
        print("Draw")
    else:
        print('Kevin %d'%kevin_point)
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)

