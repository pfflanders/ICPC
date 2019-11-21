t = int(input())

A = 440
A_sharp = 466.16
B_flat = 466.16
D_sharp = 622.25
E_flat = 622.25
E = 659.26
B = 493.88
F = 698.46
C = 523.25
F_sharp = 739.99
G_flat = 739.99
C_sharp = 554.37
D_flat = 554.37
G = 783.99
D = 587.33
G_sharp = 830.61
A_flat = 830.61
notes = [A, A_sharp, B_flat, D_sharp, E_flat, E, B, F, C, F_sharp, G_flat , C_sharp, D_flat, G, D, G_sharp, A_flat]

g_major = [G, A, B, C, D, E, F]
c_major = [C, D, E, F, G, A, B]
e_flat_major = [E_flat, F, G, A_flat, B_flat, C, D]
f_sharp_minor = [F_sharp, G_sharp, A, B, C_sharp, D, E]
g_minor = [G, A, B_flat, C, D, E_flat, F]
keys = [g_major, c_major, e_flat_major, f_sharp_minor, g_minor]

musical_range = [-4, -3, -2, -1, 0, 1, 2, 3]
valid_keys = [True, True, True, True, True]
used_notes = []
for i in range(t):
    pitch = float(input())
    for power in musical_range:
        for note in notes:
            if abs(round(pitch*(2**power), ndigits=2) - note) < 0.01:
                used_notes.append(note)
                pitch = note
                print("note is " + str(note))

    for j in range(len(keys) - 1):
        if pitch not in keys[j]:
            keys.remove(j)
            valid_keys[j] = False
            j -= 1

print(keys)
print(used_notes)
if sum(valid_keys) > 1:
    print("cannot determine key")
else:
    print(keys)
    for note in used_notes:
        print(note)
