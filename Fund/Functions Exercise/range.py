def chr_range(a, b):
    sequence=""
    for i in range(ord(a)+1, ord(b)):
        sequence=sequence+chr(i)+" "
    return sequence

chr1=input()
chr2=input()
print(chr_range(chr1, chr2))