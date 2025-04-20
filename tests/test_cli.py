"""
Tests for the command-line interface of name_visualizer.
"""

import os
import tempfile
import unittest
import pytest
from unittest.mock import patch
from name_visualizer.cli import main

class TestCLI(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_text = "HELLO"
        
    @pytest.mark.integration
    @pytest.mark.slow
    def test_cli_basic(self):
        """Test basic CLI functionality."""
        test_args = [
            "name-visualizer",
            "--text", self.test_text,
            "--output-dir", self.temp_dir
        ]
        
        with patch('sys.argv', test_args):
            main()
            
        # Check that all expected files were created
        expected_files = [
            "binary_stripe.svg",
            "morse_code_band.svg",
            "circuit_trace_silhouette.svg",
            "dot_grid_steganography.svg",
            "semaphore_flags.svg",
            "a1z26_stripe.svg",
            "code128_barcode.svg",
            "waveform_stripe.svg",
            "chevron_stripe.svg",
            "braille_stripe.svg",
            # Dark mode versions
            "binary_stripe_dark.svg",
            "morse_code_band_dark.svg",
            "circuit_trace_silhouette_dark.svg",
            "dot_grid_steganography_dark.svg",
            "semaphore_flags_dark.svg",
            "a1z26_stripe_dark.svg",
            "code128_barcode_dark.svg",
            "waveform_stripe_dark.svg",
            "chevron_stripe_dark.svg",
            "braille_stripe_dark.svg"
        ]
        
        for file in expected_files:
            file_path = os.path.join(self.temp_dir, file)
            self.assertTrue(os.path.exists(file_path), f"File {file} was not created")
            self.assertGreater(os.path.getsize(file_path), 0, f"File {file} is empty")
            
    @pytest.mark.integration
    @pytest.mark.slow
    def test_cli_dark_mode(self):
        """Test CLI with dark mode."""
        test_args = [
            "name-visualizer",
            "--text", self.test_text,
            "--output-dir", self.temp_dir,
            "--dark"
        ]
        
        with patch('sys.argv', test_args):
            main()
            
        # Check that dark mode files were created
        dark_files = [f for f in os.listdir(self.temp_dir) if f.endswith('_dark.svg')]
        self.assertTrue(len(dark_files) > 0, "No dark mode files were created")
        
    @pytest.mark.integration
    @pytest.mark.slow
    def test_cli_light_mode(self):
        """Test CLI with light mode."""
        test_args = [
            "name-visualizer",
            "--text", self.test_text,
            "--output-dir", self.temp_dir,
            "--light"
        ]
        
        with patch('sys.argv', test_args):
            main()
            
        # Check that light mode files were created
        light_files = [f for f in os.listdir(self.temp_dir) if f.endswith('.svg') and not f.endswith('_dark.svg')]
        self.assertTrue(len(light_files) > 0, "No light mode files were created")
        
    def tearDown(self):
        """Clean up test fixtures."""
        for file in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file))
        os.rmdir(self.temp_dir)

if __name__ == '__main__':
    unittest.main() 