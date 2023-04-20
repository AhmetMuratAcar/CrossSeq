import re


class Sequence:
    def __init__(self):
        self.completeFile = []
        self.totalSeq = ""
        self.id = ""
        self.leftUTR = ""
        self.codingSeq = []
        self.rightUTR = ""

    def parse_fasta(self, fasta_file):
        """Parses a FASTA file and creates a list in which each line in the FASTA file is an element. Works on the
        assumption that the system has enough memory to store read sequence. If this becomes a problem just use the
        yield function.
        """
        with open(fasta_file, "r") as ff:
            for line in ff:
                self.completeFile.append(line)
        for line in self.completeFile:
            if line == "\n":
                self.completeFile.remove(line)  # Removing the empty last elements.

    def parse_input(self, user_input):
        """Parses user input and creates a list in which each line in the input is an element."""
        pass

    def id_retrieve(self):
        """Obtains ID of sequence from parsed FASTA file"""
        self.id = re.split('>|\\s', self.completeFile[0])[1]

    def seq_retrieve(self):
        """Obtains total sequence from parsed FASTA file"""
        temp_seq = self.completeFile[:]
        del temp_seq[0]
        self.totalSeq = "".join(temp_seq)
        self.totalSeq = self.totalSeq.replace('\n', '')

    def find_start_stop(self):
        """Finds the start and stop codon of given sequence"""
        # Finding start codon
        first_split = self.totalSeq.split("ATG", 1)
        first_split[1] = "ATG" + first_split[1]
        self.leftUTR = first_split[0]

        # Finding stop codon
        remaining_seq = first_split[1]
        stop_codons = ["TAA", "TAG", "TGA"]
        for i in range(-1, len(remaining_seq), 3):
            curr_codon = remaining_seq[i+1:i+4]
            if curr_codon in stop_codons:
                self.rightUTR = remaining_seq[i+1:]  # Sets right UTR to remaining DNA.
                break
            else:
                self.codingSeq.append(curr_codon)
        print(f"left UTR: {self.leftUTR}\ncoding Seq: {self.codingSeq}\nright UTR: {self.rightUTR}")
