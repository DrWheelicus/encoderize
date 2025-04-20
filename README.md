# Name Encoding Visualizer

A Python tool that generates various visual encodings of text input (particularly names) into SVG files. The tool supports both light and dark mode outputs.

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

## Installation

1. Clone this repository
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Dependencies

- svgwrite: For SVG file generation
- pillow: For image processing
- treepoem: For barcode generation

## Usage

1. Run the script:

   ```bash
   python encoding-names.py
   ```

2. Enter the text you want to encode when prompted
3. The script will generate SVG files in two directories:
   - `output_[text]/light/`: Light mode versions
   - `output_[text]/dark/`: Dark mode versions

Each encoding will be saved as a separate SVG file with the format `[encoding_name]_[text].svg`

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

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or feedback, please contact me at [your email address].

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contributors

<a href="https://github.com/your-repo/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=your-repo" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
