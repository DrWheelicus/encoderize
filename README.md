# Encoderize

[![codecov](https://codecov.io/gh/DrWheelicus/encoderize/branch/main/graph/badge.svg)](https://codecov.io/gh/DrWheelicus/encoderize)
[![PyPI](https://badge.fury.io/py/encoderize.svg)](https://badge.fury.io/py/encoderize)
[![Downloads](https://pepy.tech/badge/encoderize)](https://pepy.tech/project/encoderize)

A Python package for generating various visual representations of text in SVG format.

## Installation

1. Install Ghostscript (required for barcode generation):
   - Windows: Download and install from [Ghostscript website](https://www.ghostscript.com/releases/gsdnld.html)
   - Linux: `sudo apt-get install ghostscript`
   - macOS: `brew install ghostscript`

2. Install the package:
```bash
pip install -e .
```

## Features

Generates SVG visualizations of text using various encoding methods:
- Binary Stripe
- Morse Code Band
- Circuit Trace Silhouette
- Dot Grid Steganography
- Semaphore Flags
- A1Z26 Numeric Stripe
- Code128 Barcode
- Waveform Stripe
- Chevron Stripe
- Braille Stripe

## Usage

```bash
encoderize --text "HELLO" --output-dir output
```

Options:
- `--text`, `-t`: Text to visualize (required)
- `--output-dir`, `-o`: Output directory (default: 'output')
- `--dark`: Generate dark mode versions
- `--light`: Generate light mode versions

## Development

Install development dependencies:
```bash
pip install -e ".[dev]"
```

Run tests:
```bash
pytest
```

## Available Visualizations

1. **Binary Stripe** - Binary bar code representation
2. **Morse Code Band** - Dots and dashes visualization
3. **Circuit Trace Silhouette** - Circuit board-like pattern
4. **Dot Grid Steganography** - Grid with highlighted letters
5. **Semaphore Flags** - Flag position visualization
6. **A1Z26 Numeric Stripe** - Numeric representation of letters
7. **Code128 Barcode** - Standard barcode format
8. **Waveform Stripe** - Waveform visualization
9. **Chevron Stripe** - Chevron pattern visualization
10. **Braille Stripe** - Braille representation

## Requirements

- Python 3.8 or higher
- svgwrite
- treepoem

## Output Structure

For input text "example", the output structure will be:

```
output/
└── example/
    ├── light/
    │   ├── binary_stripe_example.svg
    │   ├── morse_code_band_example.svg
    │   └── ...
    └── dark/
        ├── binary_stripe_example.svg
        ├── morse_code_band_example.svg
        └── ...
```

## Customization

Each visualization function accepts various parameters to customize the appearance:

- Colors
- Sizes
- Spacing
- Dimensions

See the function docstrings for detailed parameter information.

## License

MIT License

## Features

The tool generates 10 different visual encodings for any input text:

1. **Binary Pulse Stripe**: Converts text to binary and creates a visual stripe pattern
2. **Morse Code Band**: Creates a visual representation of Morse code
3. **Circuit Trace Silhouette**: Generates a 5x7 circuit-like pattern
4. **Steganographic Dot-Grid Pattern**: Creates a grid with highlighted dots representing letters
5. **Semaphore Flags**: Visual representation of semaphore flag positions
6. **A1Z26 Numeric Stripe**: Converts letters to their position in the alphabet
7. **Code128 Barcode**: Generates a standard barcode
8. **Waveform Stripe**: Creates a waveform pattern based on character values
9. **Chevron Stripe**: Binary-based chevron pattern
10. **Braille Stripe**: Visual representation of Braille characters

## Dependencies

- svgwrite: For SVG file generation
- pillow: For image processing
- treepoem: For barcode generation

## Output Structure

For input text "example", the output structure will be:

```
output_example/
├── light/
│   ├── binary_stripe_example.svg
│   ├── morse_code_band_example.svg
│   └── ...
└── dark/
    ├── binary_stripe_example.svg
    ├── morse_code_band_example.svg
    └── ...
```

## Customization

The script includes various parameters that can be modified to adjust the visual appearance of the encodings, such as:

- Colors
- Sizes
- Spacing
- Dimensions

To modify these parameters, edit the corresponding function parameters in `encoding-names.py`.

## Contact

For questions or feedback, please contact me at [haydenpmac@gmail.com](mailto:haydenpmac@gmail.com)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contributors

<a href="https://github.com/DrWheelicus/encoderize/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=DrWheelicus/encoderize" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
