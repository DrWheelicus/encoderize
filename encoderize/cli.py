"""
Command-line interface for the encoderize package.
"""

import os
import argparse
from . import (
    generate_binary_stripe,
    generate_morse_code_band,
    generate_circuit_trace_silhouette,
    generate_dot_grid_steganography,
    generate_semaphore_flags,
    generate_a1z26_stripe,
    generate_code128_barcode,
    generate_waveform_stripe,
    generate_chevron_stripe,
    generate_braille_stripe
)

def main():
    parser = argparse.ArgumentParser(description='Generate visual representations of text in SVG format.')
    parser.add_argument('--text', '-t', required=True, default='Hello, World!', help='Text to visualize')
    parser.add_argument('--output-dir', '-o', default='output', help='Output directory')
    parser.add_argument('--dark', action='store_true', help='Generate dark mode versions')
    parser.add_argument('--light', action='store_true', help='Generate light mode versions')
    
    args = parser.parse_args()
    
    # Default to both modes if neither is specified
    if not (args.dark or args.light):
        args.dark = args.light = True
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # List of all visualization functions
    funcs = [
        generate_binary_stripe,
        generate_morse_code_band,
        generate_circuit_trace_silhouette,
        generate_dot_grid_steganography,
        generate_semaphore_flags,
        generate_a1z26_stripe,
        generate_code128_barcode,
        generate_waveform_stripe,
        generate_chevron_stripe,
        generate_braille_stripe
    ]
    
    # Generate visualizations
    print("Generating SVGs...")
    
    if args.light:
        print("Generating light mode SVGs...")
        for f in funcs:
            filename = os.path.join(args.output_dir, f"{f.__name__[9:]}.svg")
            f(args.text, filename)
    
    if args.dark:
        print("Generating dark mode SVGs...")
        for f in funcs:
            filename = os.path.join(args.output_dir, f"{f.__name__[9:]}_dark.svg")
            # white on black for dark mode: override color param if supported else wrap
            if 'color' in f.__code__.co_varnames:
                f(args.text, filename, color='white')
            else:
                f(args.text, filename)
    
    print(f"All SVGs generated in {args.output_dir}")

if __name__ == '__main__':
    main() 