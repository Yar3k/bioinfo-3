import matplotlib.pyplot as plt

Threshold = 0.85

file1 = open('reads_for_analysis.fastq', 'r')
lines = file1.readlines()

size = len(lines)
index = 1
lenghts = []

while (index < size):
    seq = lines[index]
    result = sum(map(seq.count, ['C','G'])) / len(seq)
    lenghts.append(result)
    index = index + 4

count = len([i for i in lenghts if i > Threshold])
x = list(range(0, len(lenghts)))

plt.plot(x, lenghts)
plt.savefig("CG_nukleotidai.png")

print(count)