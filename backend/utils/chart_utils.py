import random

def random_hsl():
    hue = random.randint(0, 360)
    saturation = 70
    lightness = 50
    hsl_string = f"hsl({hue}, {saturation}%, {lightness}%)"
    return hsl_string

