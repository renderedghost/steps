import colorsys


def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hsl(r, g, b):
    return colorsys.rgb_to_hls(r/255.0, g/255.0, b/255.0)


def hsl_to_rgb(h, s, l):
    return colorsys.hls_to_rgb(h, l, s)


def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))


def interpolate_hsl(hsl1, hsl2, steps):
    return [(hsl1[0] + (hsl2[0] - hsl1[0]) * i / steps,
             hsl1[1] + (hsl2[1] - hsl1[1]) * i / steps,
             hsl1[2] + (hsl2[2] - hsl1[2]) * i / steps) for i in range(steps + 1)]


def create_palette(start_hex, end_hex, num_colours):
    start_rgb = hex_to_rgb(start_hex)
    end_rgb = hex_to_rgb(end_hex)

    start_hsl = rgb_to_hsl(*start_rgb)
    end_hsl = rgb_to_hsl(*end_rgb)

    hsl_palette = interpolate_hsl(start_hsl, end_hsl, num_colours)

    hex_palette = [rgb_to_hex(hsl_to_rgb(*hsl)) for hsl in hsl_palette]

    return list(zip(hex_palette, hsl_palette))


start_hex = input("First colour (hex, without the #): ")
end_hex = input("Last colour (hex, without the #): ")
num_colours = int(
    input("Enter the number of new colours to create between the two colours: "))

palette = create_palette(start_hex, end_hex, num_colours)

for colour in palette:
    print(
        f"Hex: {colour[0]} (HSL: {colour[1][0]:.2f}, {colour[1][2]:.2f}, {colour[1][1]:.2f})")
