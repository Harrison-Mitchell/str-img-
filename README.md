# str(img)
Encodes an image to a string for cryptography uses.

### Dependencies
* Python >= 3.5
* PIL `pip install Pillow`

### Usage
Either call the program with an image to be encoded (-e) or an image to be decoded (-d) e.g: `python3 strimg.py -e myImage.png`
It works by converting each R/G/B value (0-255) to the relevant ASCII character. E.g: this dark green color: `RGB(72,105,33)` becomes: `Hi!`
