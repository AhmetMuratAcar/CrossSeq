from decimal import Decimal

codon_map = {
        "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
        "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
        "TAT": "Y", "TAC": "Y", "TAA": "STOP", "TAG": "STOP",
        "TGT": "C", "TGC": "C", "TGA": "STOP", "TGG": "W",
        "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
        "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
        "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
        "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }


def sequence_formatting(object_list):
    """Formats user submissions by using Sequence class functions."""
    # First item of the tuples in object_list is the text_box and the 2nd item is the Sequence object.

    for seq_pair in object_list:
        id_submission = seq_pair[0].get("0.0", "2.0")  # Obtaining ID from the first line
        seq_pair[1].id_retrieve(id_submission)

        seq_pair[1].seq_format(seq_pair[0].get("2.0", "end"))  # Obtaining complete sequence from 2nd line onward.

        seq_pair[1].find_start_stop()  # Dividing the sequence into its different parts.


def nucleotide_analysis(object_list):
    """Conducts the nucleotide analysis of submitted sequences."""

    # Comparing nucleotide sequence to main nucleotide sequence
    main_seq = object_list[0]
    for sequence in object_list[1:]:
        # Calculating which sequence is shorter for the comparison.
        if len(sequence.nucleotideSeq) < len(main_seq.nucleotideSeq):
            comparison_length = len(sequence.nucleotideSeq)
        else:
            comparison_length = len(main_seq.nucleotideSeq)

        # Comparing the two sequences.
        for nucleotide in range(0, comparison_length):
            if sequence.nucleotideSeq[nucleotide] == main_seq.nucleotideSeq[nucleotide]:
                # Green
                sequence.nucleotideResults.append("G")
            else:
                # Grey
                sequence.nucleotideResults.append("N")

        # Denoting the remaining/missing nucleotides for the comparison sequence.
        difference = len(sequence.nucleotideSeq) - len(main_seq.nucleotideSeq)
        if difference > 0:
            for i in range(0, difference):
                sequence.nucleotideResults.append("X")

        # print(sequence.nucleotideResults)
        # print(len(sequence.nucleotideResults))

    # Nucleotide statistics calculations
    for sequence in object_list[1:]:
        length = len(sequence.nucleotideResults)

        temp_decimal = Decimal(str(sequence.nucleotideResults.count("G") / length * 100))
        sequence.nucleotideStats["G"] = round(temp_decimal, 3)

        temp_decimal = Decimal(str(sequence.nucleotideResults.count("N") / length * 100))
        sequence.nucleotideStats["N"] = round(temp_decimal, 3)

        temp_decimal = Decimal(str(sequence.nucleotideResults.count("X") / length * 100))
        sequence.nucleotideStats["X"] = round(temp_decimal, 3)


def codon_analysis(object_list):
    """Conducts the codon analysis of submitted sequences."""

    # Comparing codon sequence to main codon sequence
    main_seq = object_list[0]
    for sequence in object_list[1:]:
        # Calculating which sequence is shorter for the comparison.
        if len(sequence.codingSeq) < len(main_seq.codingSeq):
            comparison_length = len(sequence.codingSeq)
        else:
            comparison_length = len(main_seq.codingSeq)

        # Comparing the two sequences.
        for codon in range(0, comparison_length):
            if sequence.codingSeq[codon] == main_seq.codingSeq[codon]:
                # Green
                sequence.codonResults.append("G")
            elif codon_map[sequence.codingSeq[codon]] == codon_map[main_seq.codingSeq[codon]]:
                # Yellow
                sequence.codonResults.append("Y")
            else:
                # Grey
                sequence.codonResults.append("N")

        # Denoting the remaining/missing codons for the comparison sequence.
        difference = len(sequence.codingSeq)-len(main_seq.codingSeq)
        if difference > 0:
            for i in range(0, difference):
                sequence.codonResults.append("X")

        # print(sequence.codonResults)
        # print(len(sequence.codonResults))

    # Codon statistics calculations
    for sequence in object_list[1:]:
        length = len(sequence.codonResults)

        temp_decimal = Decimal(str(sequence.codonResults.count("G") / length * 100))
        sequence.codonStats["G"] = round(temp_decimal, 3)

        temp_decimal = Decimal(str(sequence.codonResults.count("N") / length * 100))
        sequence.codonStats["N"] = round(temp_decimal, 3)

        temp_decimal = Decimal(str(sequence.codonResults.count("X") / length * 100))
        sequence.codonStats["X"] = round(temp_decimal, 3)

        temp_decimal = Decimal(str(sequence.codonResults.count("Y") / length * 100))
        sequence.codonStats["Y"] = round(temp_decimal, 3)
