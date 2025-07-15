[![codecov](https://codecov.io/gh/DrWheelicus/encoderize/graph/badge.svg?token=QPQMGU1G01)](https://codecov.io/gh/DrWheelicus/encoderize) [![PyPI](https://badge.fury.io/py/encoderize.svg)](https://badge.fury.io/py/encoderize) [![Downloads](https://pepy.tech/badge/encoderize)](https://pepy.tech/project/encoderize)

<h1 align="center">
Encoderize
</h1>

<p align="center">
A Python package for generating various visual representations of text in SVG format.
</p>

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

Generates SVG visualizations of text using 10 distinct encoding methods:

1. **Binary Stripe**: Binary bar code representation
2. **Morse Code Band**: Dots and dashes visualization
3. **Circuit Trace Silhouette**: Circuit board-like pattern (5x7 grid per character)
4. **Dot Grid Steganography**: Grid with highlighted letters
5. **Semaphore Flags**: Flag position visualization
6. **A1Z26 Numeric Stripe**: Numeric representation of letters (A=1, Z=26)
7. **Code128 Barcode**: Standard Code128 barcode format
8. **Waveform Stripe**: Waveform visualization based on character ASCII values
9. **Chevron Stripe**: Chevron pattern based on binary representation
10. **Braille Stripe**: Visual representation of Braille characters

## Usage

```bash
encoderize --text "HELLO" --output-dir output
```

**Options:**

* `--text`, `-t`: Text to visualize (required)
* `--output-dir`, `-o`: Output directory (default: 'output')
* `--dark`: Generate dark mode versions (white on black)
* `--light`: Generate light mode versions (black on white)

If neither `--dark` nor `--light` is specified, both versions will be generated.

## Example Visualizations

*WIP*

## Output Structure

For input text like `"HELLO"`, the output structure will be:

```
output/
└── HELLO/
    ├── light/
    │   ├── binary_stripe_HELLO.svg
    │   ├── morse_code_band_HELLO.svg
    │   ├── circuit_trace_silhouette_HELLO.svg
    │   ├── dot_grid_steganography_HELLO.svg
    │   ├── semaphore_flags_HELLO.svg
    │   ├── a1z26_stripe_HELLO.svg
    │   ├── code128_barcode_HELLO.svg
    │   ├── waveform_stripe_HELLO.svg
    │   ├── chevron_stripe_HELLO.svg
    │   └── braille_stripe_HELLO.svg
    └── dark/
        ├── binary_stripe_HELLO.svg
        ├── morse_code_band_HELLO.svg
        └── ... (and so on for all 10 types)
```

## Customization

Each visualization function in `encoderize/visualizers.py` accepts optional parameters to customize the appearance (e.g., colors, sizes, spacing, dimensions).

See the function docstrings within `encoderize/visualizers.py` for detailed parameter information.

## Development

Install development dependencies:
```bash
pip install -e ".[dev]"
```

Run tests:
```bash
pytest
```

Run linters (e.g., flake8, black):
```bash
# Example using flake8
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
# Example using black
black . --check
```

## Requirements

* Python 3.8 or higher
* `svgwrite`
* `treepoem` (and its dependency Ghostscript for barcode generation)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to report bugs, suggest features, and submit pull requests.

## Contact

For questions or feedback, please contact Hayden MacIntyre at [haydenpmac@gmail.com](mailto:haydenpmac@gmail.com).

## Contributors

<a href="https://github.com/DrWheelicus/encoderize/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=DrWheelicus/encoderize" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
