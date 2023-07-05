from CodonMap import codon_map


def sequence_formatting(object_list):
    """Formats user submissions by using Sequence class functions."""
    # First item of the tuples in object_list is the text_box and the 2nd item is the Sequence object.

    for seq_pair in object_list:
        id_submission = seq_pair[0].get("0.0", "2.0")  # Obtaining ID from the first line
        seq_pair[1].id_retrieve(id_submission)

        seq_pair[1].seq_format(seq_pair[0].get("2.0", "end"))  # Obtaining complete sequence from 2nd line onward.

        seq_pair[1].find_start_stop()  # Diving the sequence into its different parts.


def nucleotide_analysis(object_list):
    """Conducts the nucleotide analysis of submitted sequences."""
    pass


def codon_analysis(object_list):
    """Conducts the codon analysis of submitted sequences."""

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

        # Denoting the remaining/missing codons.
        difference = abs(len(sequence.codingSeq)-len(main_seq.codingSeq))
        for i in range(0, difference):
            sequence.codonResults.append("X")

        # print(sequence.codonResults)
        # print(len(sequence.codonResults))
