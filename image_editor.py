#!/usr/bin/env python3
import os
from PIL import Image

directory = "images/"
op_directory = "/opt/icons"

for filename in os.listdir(directory):
    if filename != ".DS_Store":
        im = Image.open(os.path.join(directory, filename))
        im = im.rotate(-90).resize((128,128)).convert("RGB")
        im.save(os.path.join(op_directory, filename+".jpeg"))
