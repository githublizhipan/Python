for i in range(1, 10):
    j = 1
    while j <= i:
        print("%d*%d=%d" % (i, j, i * j), end="\t")
        j += 1
    print("")