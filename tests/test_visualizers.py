"""
Tests for the visualization functions in encoderize.
"""

import os
import tempfile
import unittest
import pytest
import svgwrite
from encoderize import (
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

class TestVisualizers(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.test_text = "TEST"
        self.temp_dir = tempfile.mkdtemp()
        
    @pytest.mark.unit
    @pytest.mark.slow
    def test_binary_stripe(self):
        """Test binary stripe generation."""
        filename = os.path.join(self.temp_dir, "binary.svg")
        generate_binary_stripe(self.test_text, filename)
        self.assertTrue(os.path.exists(filename))
        self.assertGreater(os.path.getsize(filename), 0)
        
    @pytest.mark.unit
    @pytest.mark.slow
    def test_morse_code_band(self):
        """Test Morse code band generation."""
        filename = os.path.join(self.temp_dir, "morse.svg")
        generate_morse_code_band(self.test_text, filename)
        self.assertTrue(os.path.exists(filename))
        self.assertGreater(os.path.getsize(filename), 0)
        
    @pytest.mark.unit
    @pytest.mark.slow
    def test_circuit_trace_pads_and_traces(self):
        """Test circuit trace visualization pad and trace drawing."""
        filename = os.path.join(self.temp_dir, "circuit_trace_silhouette.svg")
        generate_circuit_trace_silhouette(self.test_text, filename)
        
        # Read the generated SVG
        with open(filename, 'r') as f:
            svg_content = f.read()
            
        # Test that pads are drawn (circles)
        self.assertIn('<circle', svg_content, "No pads (circles) found in SVG")
        
        # Test that traces are drawn (lines)
        self.assertIn('<line', svg_content, "No traces (lines) found in SVG")
        
        # Test specific pad and trace counts for "TEST"
        # "TEST" in binary is 01010100 01000101 01010011 01010100
        # This should result in a specific number of pads and traces
        dwg = svgwrite.Drawing(filename)
        circle_count = svg_content.count('<circle')
        line_count = svg_content.count('<line')
        
        # For "TEST", we expect:
        # - At least 8 pads (one for each '1' in the first byte)
        # - At least 4 traces (connections between adjacent '1's)
        self.assertGreaterEqual(circle_count, 8, "Insufficient number of pads")
        self.assertGreaterEqual(line_count, 4, "Insufficient number of traces")
        
    @pytest.mark.unit
    @pytest.mark.slow
    def test_dot_grid(self):
        """Test dot grid steganography generation."""
        filename = os.path.join(self.temp_dir, "dotgrid.svg")
        generate_dot_grid_steganography(self.test_text, filename)
        self.assertTrue(os.path.exists(filename))
        self.assertGreater(os.path.getsize(filename), 0)
        
    @pytest.mark.unit
    @pytest.mark.slow
    def test_semaphore_flags(self):
        """Test semaphore flags generation."""
        filename = os.path.join(self.temp_dir, "semaphore.svg")
        generate_semaphore_flags(self.test_text, filename)
        self.assertTrue(os.path.exists(filename))
        self.assertGreater(os.path.getsize(filename), 0)
        
    @pytest.mark.unit
    @pytest.mark.slow
    def test_a1z26_stripe(self):
        """Test A1Z26 numeric stripe generation."""
        filename = os.path.join(self.temp_dir, "a1z26.svg")
        generate_a1z26_stripe(self.test_text, filename)
        self.assertTrue(os.path.exists(filename))
        self.assertGreater(os.path.getsize(filename), 0)
        
    @pytest.mark.unit
    @pytest.mark.slow
    def test_barcode(self):
        """Test barcode generation."""
        filename = os.path.join(self.temp_dir, "barcode.svg")
        generate_code128_barcode(self.test_text, filename)
        self.assertTrue(os.path.exists(filename))
        self.assertGreater(os.path.getsize(filename), 0)
        
    @pytest.mark.unit
    @pytest.mark.slow
    def test_waveform(self):
        """Test waveform stripe generation."""
        filename = os.path.join(self.temp_dir, "waveform.svg")
        generate_waveform_stripe(self.test_text, filename)
        self.assertTrue(os.path.exists(filename))
        self.assertGreater(os.path.getsize(filename), 0)
        
    @pytest.mark.unit
    @pytest.mark.slow
    def test_chevron(self):
        """Test chevron stripe generation."""
        filename = os.path.join(self.temp_dir, "chevron.svg")
        generate_chevron_stripe(self.test_text, filename)
        self.assertTrue(os.path.exists(filename))
        self.assertGreater(os.path.getsize(filename), 0)
        
    @pytest.mark.unit
    @pytest.mark.slow
    def test_braille(self):
        """Test Braille stripe generation."""
        filename = os.path.join(self.temp_dir, "braille.svg")
        generate_braille_stripe(self.test_text, filename)
        self.assertTrue(os.path.exists(filename))
        self.assertGreater(os.path.getsize(filename), 0)
        
    def tearDown(self):
        """Clean up test fixtures."""
        for file in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file))
        os.rmdir(self.temp_dir)

if __name__ == '__main__':
    unittest.main() 