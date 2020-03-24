# Created input.txt along with this and enterd 'pyton'

fin = open("input.txt", "rt")
fout = open("output.txt", "wt")

# Replacing string 'pyton' with 'python'

for line in fin:
    fout.write(line.replace('pyton', 'python'))

fin.close()
fout.close()