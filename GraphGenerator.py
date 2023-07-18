from PIL import Image, ImageDraw, ImageOps
from SequenceClass import Sequence

green = (0, 255, 0)  # Matching
yellow = (255, 255, 0)  # Same codon encoded by different sequence
gray = (169, 169, 169)  # Not matching
red = (255, 0, 0)  # Outside of comparison scope


def graph_gen(seq_objects):
    """Generates horizontal graphs by using nucleotide and codon results.
    Input: list of Sequence objects.
    Return: list of generated tuples (graph_image, split_boolean) where the odd numbered locations are codon and even
    are nucleotide graphs."""

    images = []
    max_length = 800
    pixel_width = 2

    for seq in seq_objects:
        curr_graph = seq.codonResults
        num_graphs = 0
        split = False

        while num_graphs < 2:
            # Determining if graph is too long
            graph_len = len(curr_graph)*2
            if graph_len > max_length:
                split = True

            # Generating the initial bare-bones graph.
            rectangle = Image.new("RGBA", (graph_len, 30), red)  # (width, height)
            # Code for editing the initial rectangle goes here.

            # Outlining graph for visual clarity.
            graph = ImageOps.expand(rectangle, border=2, fill="black")
            draw = ImageDraw.Draw(graph)
            # img.save("test.png")
            graph.show()
            images.append((graph, split))

            num_graphs += 1
            curr_graph = seq.nucleotideResults  # Running again to generate nucleotide results graph.

        return images


# main_seq = oryza
# comparison_seq = arabidopsis
codon_result = ['G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'Y', 'N', 'Y', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'Y', 'N', 'N', 'N', 'G', 'Y', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'Y', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N',
 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'Y', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N',
 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N',
 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'Y', 'N', 'N', 'N', 'N', 'N', 'N',
 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N',
 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N',
 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'Y', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N',
 'Y', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'Y', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'Y', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'Y', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'Y', 'N', 'N', 'N',
 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']

# main_seq = oryza
# comparison_seq = arabidopsis
nuc_result = ['G', 'G', 'G', 'N', 'N', 'G', 'N', 'G', 'G', 'N', 'G', 'G', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'G', 'G', 'N', 'G', 'N', 'N', 'G', 'G', 'N', 'N', 'N', 'G', 'N', 'G', 'N', 'N', 'N', 'G', 'G',
 'G', 'G', 'G', 'N', 'G', 'N', 'G', 'N', 'G', 'N', 'N', 'N', 'N', 'G', 'G', 'G', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'G', 'G', 'G', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N',
 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'G', 'N', 'N', 'N', 'G', 'N', 'N',
 'N', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'N', 'N', 'G', 'G', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'G', 'N', 'N', 'G', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'G', 'N', 'N', 'N', 'N', 'N', 'G', 'G', 'G', 'N',
 'G', 'N', 'N', 'G', 'G', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'G', 'G', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'G', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N',
 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'G', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'N', 'N', 'G', 'N', 'G', 'G', 'G', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G',
 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'G', 'N', 'G', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'G', 'N', 'G', 'N', 'G', 'N', 'N', 'N', 'N',
 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'G', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'G', 'G', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N',
 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N',
 'N', 'G', 'N', 'N', 'G', 'G', 'G', 'G', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'G', 'N', 'G', 'G', 'G', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N',
 'N', 'N', 'N', 'N', 'N', 'G', 'G', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'G', 'G', 'N', 'N', 'G', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'G', 'N', 'G', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N',
 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'G', 'G', 'N', 'G', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N',
 'N', 'N', 'N', 'N', 'N', 'G', 'G', 'G', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N',
 'N', 'G', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'G', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'G', 'G', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'G',
 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'G', 'N', 'N', 'N', 'N', 'G', 'G', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'G', 'G', 'N', 'G', 'N', 'G', 'N', 'N', 'G', 'N',
 'N', 'N', 'N', 'G', 'N', 'G', 'G', 'N', 'G', 'N', 'G', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'G',
 'N', 'N', 'N', 'G', 'N', 'G', 'G', 'G', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N',
 'N', 'G', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'G', 'G', 'N', 'G', 'N', 'G', 'G', 'G', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'G',
 'N', 'G', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'G', 'G', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'G', 'N', 'G', 'G',
 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'G', 'G', 'N', 'G', 'N', 'G', 'N', 'G', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'G', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'G', 'N', 'G', 'G', 'N', 'N', 'N', 'N',
 'G', 'G', 'N', 'G', 'N', 'G', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'G', 'G', 'G', 'N', 'G', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'G', 'N', 'G', 'N', 'G', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G',
 'G', 'G', 'N', 'N', 'N', 'G', 'N', 'G', 'G', 'G', 'N', 'N', 'G', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'G', 'G', 'G', 'N', 'N', 'G', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'G', 'G', 'G', 'N', 'N', 'N', 'N',
 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'G', 'G', 'G', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'G', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'G',
 'N', 'N', 'G', 'G', 'N', 'G', 'G', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'N', 'N', 'N', 'N', 'G', 'G', 'G', 'G', 'N', 'G', 'N', 'N', 'N', 'G', 'N', 'G', 'N', 'N', 'G', 'N', 'G', 'N', 'N', 'N',
 'N', 'N', 'N', 'N', 'N', 'G', 'N', 'G', 'N', 'G', 'N', 'G', 'N', 'G', 'G', 'N', 'G', 'G', 'G', 'N', 'N', 'N', 'N', 'N', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']


test_obj = Sequence()
test_obj_2 = Sequence()

test_obj.nucleotideResults = nuc_result
test_obj.codonResults = codon_result

test_obj_2.nucleotideResults = codon_result  # Purposefully mis-assigning results.
test_obj_2.codonResults = nuc_result

test_results = [test_obj, test_obj_2]
graph_gen(test_results)
