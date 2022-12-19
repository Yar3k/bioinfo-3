RANGES = {
    'Sanger': (33, 73),
    'Illumina-1.8': (33, 74),
    'Solexa': (59, 104),
    'Illumina-1.3': (64, 104),
    'Illumina-1.5': (66, 105)
}

file1 = open('reads_for_analysis.fastq', 'r')
lines = file1.readlines()

size = len(lines)
index = 3

boundaries = {
    "min" : 126,
    "max" : 33
}

while (index < size):
    for c in lines[index]:
        ascii = ord(c)
        if ascii == 10:
            break
        if ascii < boundaries["min"]:
            boundaries["min"] = ascii
        if ascii > boundaries["max"]:
            boundaries["max"] = ascii
    index = index + 4

def get_encodings_in_range(rmin, rmax, ranges=RANGES):
    valid_encodings = []
    for encoding, (emin, emax) in ranges.items():
        if rmin >= emin and rmax <= emax:
            valid_encodings.append(encoding)
    return valid_encodings

print(get_encodings_in_range(boundaries["min"], boundaries["max"]))
print(boundaries)