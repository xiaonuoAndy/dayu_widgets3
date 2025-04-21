#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Runner script for Maya tests.
This script is meant to be run from the command line with mayapy.
"""

# Import built-in modules
import os
import sys
import unittest

# Add the parent directory to sys.path to import dayu_widgets
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import Maya standalone to initialize Maya without UI
try:
    import maya.standalone
    maya.standalone.initialize()
except ImportError:
    print("Maya standalone not available. This script must be run with mayapy.")
    sys.exit(1)

# Now import the test module
from tests import maya_test

if __name__ == "__main__":
    # Run the tests
    maya_test.run_tests()
    
    # Uninitialize Maya when done
    maya.standalone.uninitialize()
