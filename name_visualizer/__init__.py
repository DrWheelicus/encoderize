"""
Name Visualizer Module

A collection of functions to generate various visual representations of text/names
in SVG format. Each function creates a different type of visualization:

1. Binary Stripe - Binary bar code representation
2. Morse Code Band - Dots and dashes visualization
3. Circuit Trace Silhouette - Circuit board-like pattern
4. Dot Grid Steganography - Grid with highlighted letters
5. Semaphore Flags - Flag position visualization
6. A1Z26 Numeric Stripe - Numeric representation of letters
7. Code128 Barcode - Standard barcode format
8. Waveform Stripe - Waveform visualization
9. Chevron Stripe - Chevron pattern visualization
10. Braille Stripe - Braille representation

Each visualization function takes text input and generates an SVG file.
"""

from .visualizers import (
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

__all__ = [
    'generate_binary_stripe',
    'generate_morse_code_band',
    'generate_circuit_trace_silhouette',
    'generate_dot_grid_steganography',
    'generate_semaphore_flags',
    'generate_a1z26_stripe',
    'generate_code128_barcode',
    'generate_waveform_stripe',
    'generate_chevron_stripe',
    'generate_braille_stripe'
]

"""
Name Visualizer package for generating various visual representations of text.
"""

__version__ = "0.1.0" 