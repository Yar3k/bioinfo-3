from Bio.Blast import NCBIWWW
import xml.etree.ElementTree as ET

def request_database(seq):
    result_handle = NCBIWWW.qblast("blastn", "nt", seq, entrez_query='txid2[ORGN]')
    root = ET.fromstring(result_handle.read())
    child = root.find("BlastOutput_iterations").find("Iteration").find("Iteration_hits")[0].find("Hit_def")
    print(child.text)

def main():
    Threshold = 0.85

    file1 = open('reads_for_analysis.fastq', 'r')
    lines = file1.readlines()

    size = len(lines)
    index = 1
    seqences = []

    while (index < size):
        seq = lines[index]
        result = sum(map(seq.count, ['C','G'])) / len(seq)
        if result > Threshold:
            seqences.append(lines[index-8])
            seqences.append(lines[index-4])
            seqences.append(lines[index])
            seqences.append(lines[index+4])
            seqences.append(lines[index+8])
        index = index + 4

    with open(r'seq.txt', 'w') as fp:
        fp.write('\n'.join(seqences))
    for seq in seqences:
        request_database(seq)
    
    return 0

if __name__ == "__main__":
    main()