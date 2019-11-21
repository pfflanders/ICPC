t = int(input())
for pooop in range(1, t+1):
    compressed_rna = input()
    max_CG = int(input())
    rna = ""
    #
    # for i in range(len(compressed_rna)):
    #     if i % 2 == 0:
    #         rna += (compressed_rna[i] * int(compressed_rna[i+1]))
    for a in compressed_rna
        if a  in ("A","G","U","C"):
            compressed_
    #
    # AUs = 0
    # CGs = 0
    # length = len(rna)
    # for i in rna:
    #     for j in rna:
    #         if i == "A":
    #             if j == "U":
    #                 AUs += 1
    #                 rna = rna[:rna.find("A")] + rna[rna.find("A") + 1:]
    #                 rna = rna[:rna.find("U")] + rna[rna.find("U") + 1:]
    #         else:
    #             if j == "G" and CGs < max_CG:
    #                 CGs += 1
    #                 rna = rna[:rna.find("C")] + rna[rna.find("C") + 1:]
    #                 rna = rna[:rna.find("G")] + rna[rna.find("G") + 1:]
    # total = CGs + AUs
    # print("Case %d: " % pooop + str(total))
