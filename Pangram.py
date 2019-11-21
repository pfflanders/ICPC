t = int(input())
alpha = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')


def foxy(x):
    death = ""
    for character in alpha:
        if character in x:
            continue
        else:
            death = death + character
    if death == "":
        print("pangram")
    else:
        print("missing " + death)


for i in range(t):
    foxy(input().lower())
