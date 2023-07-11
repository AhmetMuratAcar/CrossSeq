from PIL import Image, ImageDraw, ImageOps
from Sample_codon_result import codon_result
from Sample_nucleotide_result import nuc_result

green = (0, 255, 0)  # Matching
yellow = (255, 255, 0)  # Same codon encoded by different sequence
gray = (169, 169, 169)  # Not matching
red = (255, 0, 0)  # Outside of comparison scope

rectangle = Image.new("RGBA", (400, 30), red)  # (width, height)
graph = ImageOps.expand(rectangle, border=2, fill="black")
draw = ImageDraw.Draw(graph)

# img.save("test.png")
graph.show()
