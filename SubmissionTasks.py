def sequence_formatting(object_list):
    # First item of the tuples in object_list is the text_box and the 2nd item is the Sequence object.

    for seq_pair in object_list:
        id_submission = seq_pair[0].get("0.0", "2.0")  # Obtaining ID from the first line
        seq_pair[1].id_retrieve(id_submission)
        print(seq_pair[1].id)

        seq_pair[1].seq_format(seq_pair[0].get("2.0", "end"))  # Obtaining complete sequence from 2nd line onward.

        seq_pair[1].find_start_stop()  # Diving the sequence into its different parts.

# Maybe the comparison on submission should happen here as well?
