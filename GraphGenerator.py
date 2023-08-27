from PIL import Image, ImageDraw, ImageOps

color_map = {"G": "green",
             "N": "gray",
             "Y": "yellow"}


def graph_gen(seq_objects):
    """Generates horizontal graphs by using nucleotide and codon results.
    Input: list of Sequence objects.
    Return: list of generated graphs where the odd numbered locations are codon and even are nucleotide graphs."""

    images = []
    pixel_width = 2
    to_be_constructed = []

    for seq in seq_objects:
        to_be_constructed.extend([seq.nucleotideResults, seq.codonResults])

        # Passing lengths into seq objects for proper construction in the results page.
        nuc_len = len(seq.nucleotideResults) * pixel_width
        codon_len = len(seq.codonResults) * pixel_width
        seq.graphLengths.extend([nuc_len, codon_len])

    for result in to_be_constructed:
        graph_len = len(result)*pixel_width

        # Generating the initial bare-bones graph.
        init_graph = Image.new("RGBA", (graph_len, 60), color="red")  # (width, height)
        draw = ImageDraw.Draw(init_graph)

        # Editing the bare-bones rectangle into graph.
        x_val = 0
        for location in result:
            if location == "X":
                break
            draw.line((x_val, 0, x_val, 60), fill=color_map[location], width=pixel_width)
            x_val += pixel_width

        # Outlining graph for visual clarity.
        fin_graph = ImageOps.expand(init_graph, border=2, fill="black")
        # fin_graph.show()
        images.append(fin_graph)

    return images
