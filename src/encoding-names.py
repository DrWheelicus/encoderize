import os
import math
import io
import base64
import svgwrite
import treepoem

# 1. Binary Pulse Stripe
def generate_binary_stripe(name, filename, bar_width=20, bar_height=200, spacing=5, color='black'):
    bits = ''.join(f'{ord(c):08b}' for c in name)
    total_width = len(bits) * (bar_width + spacing)
    dwg = svgwrite.Drawing(filename, size=(total_width, bar_height))
    x = 0
    for bit in bits:
        if bit == '1':
            dwg.add(dwg.rect(insert=(x, 0), size=(bar_width, bar_height), fill=color))
        x += bar_width + spacing
    dwg.save()

# 2. Morse-Code Dot-Dash Band
def generate_morse_code_band(text, filename, dot_diameter=16, dash_width=48, height=16, spacing_symbol=8, spacing_letter=16, color='black'):
    MORSE_DICT = {
        'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
        'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
        'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
        'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
        'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--',
        'Z':'--..', ' ':' '
    }
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

# 3. Circuit-Trace Silhouette (5x7 patterns)
LETTER_PATTERNS = {
    'A':"01110100011000111111000110001",
    # Flattened rows for readability, split every 5 chars.
    # ... include B–Z in same format ...
    'Z':"111110000100010001000100011111"
}
def generate_circuit_trace_silhouette(text, filename, pad_radius=8, pad_spacing=30, trace_width=4, color='black'):
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

# 4. Steganographic Dot-Grid Pattern
def generate_dot_grid_steganography(text, filename, rows=6, cols=6, spacing=40, dot_r=6, hl_r=12, base='black', hl='red'):
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

# 5. Semaphore Flags
def generate_semaphore_flags(text, filename, icon_size=80, spacing=20, circle='white', flag='black'):
    SEM = {'A':(0,45),'B':(0,90),'C':(0,135),'D':(0,180),'E':(0,225),'F':(0,270),'G':(0,315),
           'H':(45,90),'I':(45,135),'J':(90,315),'K':(45,180),'L':(45,225),'M':(45,270),'N':(45,315),
           'O':(90,135),'P':(90,180),'Q':(90,225),'R':(90,270),'S':(90,315),
           'T':(135,180),'U':(135,225),'V':(135,270),'W':(135,315),
           'X':(180,225),'Y':(180,270),'Z':(180,315)}
    total = len(text)*(icon_size+spacing)
    dwg = svgwrite.Drawing(filename, size=(total, icon_size))
    x=0
    for ch in text.upper():
        ang = SEM.get(ch,())
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

# 6. A1Z26 Numeric Stripe
def generate_a1z26_stripe(text, filename, font=48, sp=10, delim='·', fam='Arial', color='black'):
    nums=[str(ord(c)-64) for c in text.upper() if c.isalpha()]
    s=delim.join(nums)
    w=len(s)*(font*0.6)+sp; h=font*1.2
    dwg=svgwrite.Drawing(filename,size=(w,h))
    dwg.add(dwg.text(s,insert=(sp,font),font_size=font,font_family=fam,fill=color))
    dwg.save()

# 7. Barcode as embedded PNG in SVG
def generate_code128_barcode(text, filename):
    img=treepoem.generate_barcode(barcode_type='code128',data=text)
    im=img.convert('RGB');w,h=im.size
    buf=io.BytesIO();im.save(buf,format='PNG')
    data=base64.b64encode(buf.getvalue()).decode()
    dwg=svgwrite.Drawing(filename,size=(w,h))
    dwg.add(dwg.image(href=f"data:image/png;base64,{data}",insert=(0,0),size=(w,h)))
    dwg.save()

# 8. Waveform Stripe
def generate_waveform_stripe(name, filename, w=1200, h=300, spc=50, color='black'):
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

# 9. Chevron Stripe
def generate_chevron_stripe(name, filename, wu=30, hu=30, sp=5, color='black'):
    bits=''.join(f'{ord(c):08b}' for c in name)
    tw=len(bits)*(wu+sp); dwg=svgwrite.Drawing(filename,size=(tw,hu))
    x=0
    for b in bits:
        pts=[(x,hu),(x+wu/2,0),(x+wu,hu)] if b=='1' else [(x,0),(x+wu/2,hu),(x+wu,0)]
        dwg.add(dwg.polygon(points=pts,fill=color)); x+=wu+sp
    dwg.save()

# 10. Braille Stripe
def generate_braille_stripe(text, filename, cs=60, dr=8, sp=20, color='black'):
    MAP={ 'A':[1],'B':[1,2],'C':[1,4],'D':[1,4,5],'E':[1,5],'F':[1,2,4],'G':[1,2,4,5],
          'H':[1,2,5],'I':[2,4],'J':[2,4,5],'K':[1,3],'L':[1,2,3],'M':[1,3,4],'N':[1,3,4,5],
          'O':[1,3,5],'P':[1,2,3,4],'Q':[1,2,3,4,5],'R':[1,2,3,5],'S':[2,3,4],'T':[2,3,4,5],
          'U':[1,3,6],'V':[1,2,3,6],'W':[2,4,5,6],'X':[1,3,4,6],'Y':[1,3,4,5,6],'Z':[1,3,5,6] }
    cols=len(text); w=cols*(cs+sp); h=cs; dwg=svgwrite.Drawing(filename,size=(w,h))
    POS={1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2)}
    for i,ch in enumerate(text.upper()):
        dots=MAP.get(ch,[]); bx=i*(cs+sp)
        for d in dots:
            c,r=POS[d]; x=bx+c*(cs/2)+cs/4; y=r*(cs/3)+cs/6
            dwg.add(dwg.circle(center=(x,y),r=dr,fill=color))
    dwg.save()

if __name__=='__main__':
    text=input("Enter text to encode: ")
    text = text.strip()
    print("Generating SVGs...")
    base=f"output_{text}"; light=os.path.join(base,'light'); dark=os.path.join(base,'dark')
    os.makedirs(light,exist_ok=True); os.makedirs(dark,exist_ok=True)
    funcs=[
        generate_binary_stripe,generate_morse_code_band,generate_circuit_trace_silhouette,
        generate_dot_grid_steganography,generate_semaphore_flags,generate_a1z26_stripe,
        generate_code128_barcode,generate_waveform_stripe,generate_chevron_stripe,generate_braille_stripe
    ]
    print("Generating light mode SVGs...")
    for f in funcs:
        f(text,os.path.join(light,f.__name__[9:]+"_"+text+".svg"))
    print("Generating dark mode SVGs...")
    for f in funcs:
        # white on black for dark mode: override color param if supported else wrap
        if 'color' in f.__code__.co_varnames:
            f(text,os.path.join(dark,f.__name__[9:]+"_"+text+".svg"),color='white')
        else:
            f(text,os.path.join(dark,f.__name__[9:]+"_"+text+".svg"))
    print(f"All SVGs generated in light & dark folders. {len(funcs)} SVGs generated for {text}")
