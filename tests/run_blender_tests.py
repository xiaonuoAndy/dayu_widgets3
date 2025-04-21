#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Runner script for Blender tests.
This script is meant to be run from the command line with blender --background --python.
"""

# Import built-in modules
import os
import sys
import unittest

# Add the parent directory to sys.path to import dayu_widgets
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import Blender Python API
try:
    import bpy
except ImportError:
    print("Blender Python API not available. This script must be run with blender --background --python.")
    sys.exit(1)

# Now import the test module
from tests import blender_test

if __name__ == "__main__":
    # Run the tests
    blender_test.run_tests()
    
    # Exit Blender when done
    sys.exit(0)
