from PIL import Image, ImageDraw, ImageOps
from Sample_codon_result import codon_result
from Sample_nucleotide_result import nuc_result
from SequenceClass import Sequence

green = (0, 255, 0)  # Matching
yellow = (255, 255, 0)  # Same codon encoded by different sequence
gray = (169, 169, 169)  # Not matching
red = (255, 0, 0)  # Outside of comparison scope


def graph_gen(seq_objects):
    """Generates horizontal graphs by using nucleotide and codon results. Input: list of Sequence objects."""
    max_length = 800
    pixel_width = 2
    comp_value = int(max_length / pixel_width)

    for object in seq_objects:
        # Determining if multiple graphs are needed due to length of results.
        curr_graph = object.codonResults

        for i in range (0, 2):
            graph_len = len(curr_graph.len)
            split = False
            if graph_len > max_length:
                split = True

            # Generating the initial bare-bones graph.
            rectangle = Image.new("RGBA", (graph_len, 30), red)  # (width, height)
            graph = ImageOps.expand(rectangle, border=2, fill="black")
            # draw = ImageDraw.Draw(graph)
            # img.save("test.png")
            graph.show()

            if split is True:
                # Use a loop to generate other graphs
                split_count = graph_len - max_length
                pass

            curr_graph = object.nucleotideResults  # Running again to generate nucleotide results graph.


test_obj = Sequence()
test_obj_2 = Sequence()

test_obj.nucleotideResults = nuc_result
test_obj.codonResults = codon_result

test_obj_2.nucleotideResults = codon_result  # Purposefully mis-assigning results.
test_obj_2.codonResults = nuc_result

test_results = [test_obj, test_obj_2]
graph_gen(test_results)
