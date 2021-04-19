import random
from Bio import SeqIO
import numpy as np
import timeit

def mutation(rate, seq):
    records = SeqIO.parse(seq, "fasta")
    for sequence in records:
        curSeq = sequence.seq
        vectorisedSec =np.array(list(str(sequence.seq).replace("A", "0").replace("T", "1").replace("C", "2").replace("G", "3")), dtype = float)
        randomList = np.random.rand(len(curSeq))
        booleanList = randomList < rate
        vectorisedSec = vectorisedSec + ( booleanList * random.randint(1, 3))
        vectorisedSec[vectorisedSec  > 3] = 0 + vectorisedSec[vectorisedSec  > 3]% 4
        vectorisedSec = vectorisedSec.astype(dtype = str)

        vectorisedSec[vectorisedSec == '0.0'] = 'A'
        vectorisedSec[vectorisedSec == '1.0'] = 'T'
        vectorisedSec[vectorisedSec == '2.0'] = 'C'
        vectorisedSec[vectorisedSec == '3.0'] = 'G'
        # s = vectorisedSec.tostring()
        # s = vectorisedSec.view(f'U{vectorisedSec.size}')[0].replace(" ", "")
        # s = vectorisedSec.view('U' + str(vectorisedSec.size))[0].replace(" ", "")

        # s = ["".join(row) for row in vectorisedSec]
        # print(s)

        # with open("f1.txt", "w") as f:
            # f.write(s)

        # print(vectorisedSec)





def main():
    for i in range(100):
            mutation(1/1000, "./ressources/Araport11_genes.201606.cdna1.fasta")
    print("finit")



if __name__ == '__main__':
    main()