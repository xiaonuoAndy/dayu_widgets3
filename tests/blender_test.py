#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test dayu_widgets in Blender environment.
This script is meant to be run by Blender's Python interpreter.
"""

# Import built-in modules
import os
import sys
import unittest

# Add the parent directory to sys.path to import dayu_widgets
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import third-party modules
try:
    import bpy
    from bpy.types import Panel
except ImportError:
    print("Blender Python API not available. This script must be run within Blender.")
    sys.exit(1)

# Import local modules
from dayu_widgets.button import MButton
from dayu_widgets.label import MLabel
from dayu_widgets.divider import MDivider
from dayu_widgets.line_edit import MLineEdit


class BlenderWidgetTestCase(unittest.TestCase):
    """Test case for dayu_widgets in Blender."""
    
    def test_button(self):
        """Test MButton in Blender."""
        button = MButton("Test Button")
        self.assertEqual(button.text(), "Test Button")
        
    def test_label(self):
        """Test MLabel in Blender."""
        label = MLabel("Test Label")
        self.assertEqual(label.text(), "Test Label")
        
    def test_line_edit(self):
        """Test MLineEdit in Blender."""
        line_edit = MLineEdit()
        line_edit.setText("Test")
        self.assertEqual(line_edit.text(), "Test")


def run_tests():
    """Run the tests."""
    suite = unittest.TestLoader().loadTestsFromTestCase(BlenderWidgetTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    
if __name__ == "__main__":
    # When running as a script from Blender's text editor
    run_tests()
