def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
        return
    for i in ["0", "1"]:
        gen_bin(M-1, prefix+i)

gen_bin(4)