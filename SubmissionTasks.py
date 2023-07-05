def sequence_formatting(object_list):
    """Formats user submissions by using Sequence class functions."""
    # First item of the tuples in object_list is the text_box and the 2nd item is the Sequence object.

    for seq_pair in object_list:
        id_submission = seq_pair[0].get("0.0", "2.0")  # Obtaining ID from the first line
        seq_pair[1].id_retrieve(id_submission)
        print(seq_pair[1].id)

        seq_pair[1].seq_format(seq_pair[0].get("2.0", "end"))  # Obtaining complete sequence from 2nd line onward.

        seq_pair[1].find_start_stop()  # Diving the sequence into its different parts.


def nucleotide_analysis(object_list):
    pass


def codon_analysis(object_list):
    """Conducts the codon analysis of submitted sequences."""

    main_seq = object_list[0]
    for sequence in object_list[1:]:
        for codon in range(0, len(sequence.codingSeq)):
            if sequence[codon] == main_seq[codon]:
                pass
