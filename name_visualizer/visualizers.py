"""
Visualization functions for the name_visualizer module.

This module contains all the visualization functions that generate SVG representations
of text using various encoding methods.
"""

import math
import io
import base64
import svgwrite
import treepoem

# Constants
LETTER_PATTERNS = {
    'A': "01110100011000111111000110001",
    'B': "11110100011111010001111101000111110",
    'C': "011101000110000100001000010000100001000101110",
    'D': "111101000110001100011000110001100011000111110",
    'E': "111111000010000100001111110000100001000011111",
    'F': "111111000010000100001111110000100001000010000",
    'G': "011101000110000100001000011111100011000101110",
    'H': "100011000110001111111000110001100011000110001",
    'I': "111110010000100001000010000100001000111110",
    'J': "0011100010000100001000010000101001010010110",
    'K': "1000110010101001100011100010100101001010001",
    'L': "10000100001000010000100001000010000111111",
    'M': "100011100111101101011000110001100011000110001",
    'N': "100011100111101101011011011000111000110001",
    'O': "011101000110001100011000110001100011000101110",
    'P': "111101000110001100011111010000100001000010000",
    'Q': "01110100011000110001100011010110010100101110",
    'R': "111101000110001100011111010100101001010001",
    'S': "011101000110000011100000100001000101110",
    'T': "111110010000100001000010000100001000010000",
    'U': "100011000110001100011000110001100011000101110",
    'V': "100011000110001100011000101010101010010001",
    'W': "1000110001100011000110001101011010111010001",
    'X': "100011000101010100010001010101000110001",
    'Y': "100011000101010100010000100001000010000",
    'Z': "111110000100010001000100011111"
}

MORSE_DICT = {
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
    'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
    'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--',
    'Z':'--..', ' ':' '
}

SEMAPHORE_DICT = {
    'A':(0,45), 'B':(0,90), 'C':(0,135), 'D':(0,180), 'E':(0,225), 'F':(0,270), 'G':(0,315),
    'H':(45,90), 'I':(45,135), 'J':(90,315), 'K':(45,180), 'L':(45,225), 'M':(45,270), 'N':(45,315),
    'O':(90,135), 'P':(90,180), 'Q':(90,225), 'R':(90,270), 'S':(90,315),
    'T':(135,180), 'U':(135,225), 'V':(135,270), 'W':(135,315),
    'X':(180,225), 'Y':(180,270), 'Z':(180,315)
}

BRAILLE_DICT = {
    'A':[1], 'B':[1,2], 'C':[1,4], 'D':[1,4,5], 'E':[1,5], 'F':[1,2,4], 'G':[1,2,4,5],
    'H':[1,2,5], 'I':[2,4], 'J':[2,4,5], 'K':[1,3], 'L':[1,2,3], 'M':[1,3,4], 'N':[1,3,4,5],
    'O':[1,3,5], 'P':[1,2,3,4], 'Q':[1,2,3,4,5], 'R':[1,2,3,5], 'S':[2,3,4], 'T':[2,3,4,5],
    'U':[1,3,6], 'V':[1,2,3,6], 'W':[2,4,5,6], 'X':[1,3,4,6], 'Y':[1,3,4,5,6], 'Z':[1,3,5,6]
}

def generate_binary_stripe(name, filename, bar_width=20, bar_height=200, spacing=5, color='black'):
    """
    Generate a binary stripe visualization of a name using SVG.
    
    Args:
        name (str): The text to encode into binary
        filename (str): Path to save the SVG file
        bar_width (int): Width of each binary bar
        bar_height (int): Height of the binary stripe
        spacing (int): Space between bars
        color (str): Color of the bars
    """
    bits = ''.join(f'{ord(c):08b}' for c in name)
    total_width = len(bits) * (bar_width + spacing)
    dwg = svgwrite.Drawing(filename, size=(total_width, bar_height))
    x = 0
    for bit in bits:
        if bit == '1':
            dwg.add(dwg.rect(insert=(x, 0), size=(bar_width, bar_height), fill=color))
        x += bar_width + spacing
    dwg.save()

def generate_morse_code_band(text, filename, dot_diameter=16, dash_width=48, height=16, spacing_symbol=8, spacing_letter=16, color='black'):
    """
    Generate a Morse code visualization of text using dots and dashes in SVG.
    
    Args:
        text (str): The text to encode into Morse code
        filename (str): Path to save the SVG file
        dot_diameter (int): Diameter of dots
        dash_width (int): Width of dashes
        height (int): Height of the band
        spacing_symbol (int): Space between symbols
        spacing_letter (int): Space between letters
        color (str): Color of the symbols
    """
    sequence = [MORSE_DICT.get(c, '') for c in text.upper()]
    total_symbols = sum(len(seq) for seq in sequence)
    total_width = total_symbols * (dot_diameter + spacing_symbol) + len(sequence) * spacing_letter
    dwg = svgwrite.Drawing(filename, size=(total_width, height))
    x = 0
    for seq in sequence:
        for symbol in seq:
            if symbol == '.':
                dwg.add(dwg.circle(center=(x + dot_diameter/2, height/2), r=dot_diameter/2, fill=color))
                x += dot_diameter + spacing_symbol
            elif symbol == '-':
                dwg.add(dwg.rect(insert=(x, 0), size=(dash_width, height), fill=color))
                x += dash_width + spacing_symbol
        x += spacing_letter
    dwg.save()

def generate_circuit_trace_silhouette(text, filename, pad_radius=8, pad_spacing=30, trace_width=4, color='black'):
    """
    Generate a circuit trace silhouette visualization of text using a 5x7 grid pattern.
    
    Args:
        text (str): The text to encode into circuit traces
        filename (str): Path to save the SVG file
        pad_radius (int): Radius of connection pads
        pad_spacing (int): Space between pads
        trace_width (int): Width of connecting traces
        color (str): Color of the circuit elements
    """
    cols, rows = 5, 7
    width = cols * pad_spacing
    height = rows * pad_spacing
    dwg = svgwrite.Drawing(filename, size=(width * len(text) + pad_spacing*(len(text)-1), height))
    for i, ch in enumerate(text.upper()):
        bits = LETTER_PATTERNS.get(ch, '')
        if not bits: continue
        x_ofs = i * (width + pad_spacing)
        # draw pads
        for idx, bit in enumerate(bits):
            if bit == '1':
                c = idx % cols; r = idx // cols
                x = x_ofs + c * pad_spacing; y = r * pad_spacing
                dwg.add(dwg.circle(center=(x, y), r=pad_radius, fill=color))
        # draw traces
        for idx, bit in enumerate(bits):
            if bit != '1': continue
            c = idx % cols; r = idx // cols
            x1 = x_ofs + c * pad_spacing; y1 = r * pad_spacing
            # right
            if c + 1 < cols and idx + 1 < len(bits) and bits[idx + 1] == '1':
                x2 = x_ofs + (c+1) * pad_spacing; y2 = y1
                dwg.add(dwg.line(start=(x1,y1), end=(x2,y2), stroke=color, stroke_width=trace_width))
            # down
            if r + 1 < rows and (r + 1) * cols + c < len(bits) and bits[(r + 1) * cols + c] == '1':
                x2 = x1; y2 = (r+1) * pad_spacing
                dwg.add(dwg.line(start=(x1,y1), end=(x2,y2), stroke=color, stroke_width=trace_width))
    dwg.save()

def generate_dot_grid_steganography(text, filename, rows=6, cols=6, spacing=40, dot_r=6, hl_r=12, base='black', hl='red'):
    """
    Generate a steganographic dot grid pattern where letters are highlighted in a grid.
    
    Args:
        text (str): The text to encode in the grid
        filename (str): Path to save the SVG file
        rows (int): Number of rows in the grid
        cols (int): Number of columns in the grid
        spacing (int): Space between dots
        dot_r (int): Radius of base dots
        hl_r (int): Radius of highlighted dots
        base (str): Color of base dots
        hl (str): Color of highlighted dots
    """
    width = (cols-1)*spacing + 2*hl_r
    height = (rows-1)*spacing + 2*hl_r
    dwg = svgwrite.Drawing(filename, size=(width, height))
    for r in range(rows):
        for c in range(cols):
            x = hl_r + c*spacing; y = hl_r + r*spacing
            dwg.add(dwg.circle(center=(x,y), r=dot_r, fill=base))
    for ch in text.upper():
        if not ch.isalpha(): continue
        idx = ord(ch) - ord('A')
        r, c = divmod(idx, cols)
        x = hl_r + c*spacing; y = hl_r + r*spacing
        dwg.add(dwg.circle(center=(x,y), r=hl_r, fill=hl))
    dwg.save()

def generate_semaphore_flags(text, filename, icon_size=80, spacing=20, circle='white', flag='black'):
    """
    Generate a semaphore flag visualization of text using flag positions.
    
    Args:
        text (str): The text to encode into semaphore flags
        filename (str): Path to save the SVG file
        icon_size (int): Size of each flag icon
        spacing (int): Space between flags
        circle (str): Color of the background circle
        flag (str): Color of the flags
    """
    total = len(text)*(icon_size+spacing)
    dwg = svgwrite.Drawing(filename, size=(total, icon_size))
    x=0
    for ch in text.upper():
        ang = SEMAPHORE_DICT.get(ch,())
        cx, cy = x+icon_size/2, icon_size/2
        dwg.add(dwg.circle(center=(cx,cy), r=icon_size/2, fill=circle, stroke=flag, stroke_width=4))
        for a in ang:
            rad = math.radians(a)
            x2,y2 = cx+math.cos(rad)*icon_size/2, cy-math.sin(rad)*icon_size/2
            for off in (15,-15):
                rad2 = math.radians(a+off)
                x3,y3 = x2+math.cos(rad2)*icon_size/6, y2-math.sin(rad2)*icon_size/6
                dwg.add(dwg.polygon(points=[(cx,cy),(x3,y3),(x2,y2)], fill=flag))
        x += icon_size+spacing
    dwg.save()

def generate_a1z26_stripe(text, filename, font=48, sp=10, delim='·', fam='Arial', color='black'):
    """
    Generate an A1Z26 numeric stripe where letters are converted to their position in the alphabet.
    
    Args:
        text (str): The text to encode into numbers
        filename (str): Path to save the SVG file
        font (int): Font size
        sp (int): Spacing
        delim (str): Delimiter between numbers
        fam (str): Font family
        color (str): Text color
    """
    nums=[str(ord(c)-64) for c in text.upper() if c.isalpha()]
    s=delim.join(nums)
    w=len(s)*(font*0.6)+sp; h=font*1.2
    dwg=svgwrite.Drawing(filename,size=(w,h))
    dwg.add(dwg.text(s,insert=(sp,font),font_size=font,font_family=fam,fill=color))
    dwg.save()

def generate_code128_barcode(text, filename):
    """
    Generate a Code 128 barcode of the text embedded in an SVG.
    
    Args:
        text (str): The text to encode into barcode
        filename (str): Path to save the SVG file
    """
    img=treepoem.generate_barcode(barcode_type='code128',data=text)
    im=img.convert('RGB');w,h=im.size
    buf=io.BytesIO();im.save(buf,format='PNG')
    data=base64.b64encode(buf.getvalue()).decode()
    dwg=svgwrite.Drawing(filename,size=(w,h))
    dwg.add(dwg.image(href=f"data:image/png;base64,{data}",insert=(0,0),size=(w,h)))
    dwg.save()

def generate_waveform_stripe(name, filename, w=1200, h=300, spc=50, color='black'):
    """
    Generate a waveform visualization of text using sine waves.
    
    Args:
        name (str): The text to encode into waveform
        filename (str): Path to save the SVG file
        w (int): Width of the waveform
        h (int): Height of the waveform
        spc (int): Samples per character
        color (str): Color of the waveform
    """
    pts=[]
    tot=len(name)*spc
    for i in range(tot):
        idx=i//spc
        amp=math.sin(2*math.pi*(i/spc)+ord(name[idx]))
        x=i/(tot-1)*w; y=h/2-amp*(h/2-20)
        pts.append((x,y))
    dwg=svgwrite.Drawing(filename,size=(w,h))
    dwg.add(dwg.polyline(points=pts,stroke=color,fill='none',stroke_width=4))
    dwg.save()

def generate_chevron_stripe(name, filename, wu=30, hu=30, sp=5, color='black'):
    """
    Generate a chevron stripe visualization of text using binary encoding.
    
    Args:
        name (str): The text to encode into chevrons
        filename (str): Path to save the SVG file
        wu (int): Width of each unit
        hu (int): Height of each unit
        sp (int): Space between units
        color (str): Color of the chevrons
    """
    bits=''.join(f'{ord(c):08b}' for c in name)
    tw=len(bits)*(wu+sp); dwg=svgwrite.Drawing(filename,size=(tw,hu))
    x=0
    for b in bits:
        pts=[(x,hu),(x+wu/2,0),(x+wu,hu)] if b=='1' else [(x,0),(x+wu/2,hu),(x+wu,0)]
        dwg.add(dwg.polygon(points=pts,fill=color)); x+=wu+sp
    dwg.save()

def generate_braille_stripe(text, filename, cs=60, dr=8, sp=20, color='black'):
    """
    Generate a Braille stripe visualization of text.
    
    Args:
        text (str): The text to encode into Braille
        filename (str): Path to save the SVG file
        cs (int): Cell size
        dr (int): Dot radius
        sp (int): Space between cells
        color (str): Color of the Braille dots
    """
    cols=len(text); w=cols*(cs+sp); h=cs; dwg=svgwrite.Drawing(filename,size=(w,h))
    POS={1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2)}
    for i,ch in enumerate(text.upper()):
        dots=BRAILLE_DICT.get(ch,[]); bx=i*(cs+sp)
        for d in dots:
            c,r=POS[d]; x=bx+c*(cs/2)+cs/4; y=r*(cs/3)+cs/6
            dwg.add(dwg.circle(center=(x,y),r=dr,fill=color))
    dwg.save() 