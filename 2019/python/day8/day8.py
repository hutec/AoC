from collections import Counter


def split_to_layers(image: str, width: int, height: int):
    layers = []
    pixels_per_layer = width * height
    n_layers = len(image) // pixels_per_layer
    for i in range(n_layers):
        layers.append(image[i * pixels_per_layer : (i + 1) * pixels_per_layer])

    return layers


with open("input", "r") as f:
    img = f.read()

layers = split_to_layers(img, width=25, height=6)
counters = [Counter(l) for l in layers]
counter = min(counters, key=lambda c: c["0"])
print(counter["1"] * counter["2"])


def top_visible(pixels):
    for pixel in pixels:
        if pixel == "0":
            return " "
        elif pixel == "1":
            return "X"


decoded = list(map(top_visible, zip(*layers)))
for row in range(6):
    print("".join(decoded[row * 25 : (row + 1) * 25]))
