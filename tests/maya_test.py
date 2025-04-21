#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test dayu_widgets in Maya environment.
This script is meant to be run inside Maya's Python interpreter.
"""

# Import built-in modules
import os
import sys
import unittest

# Import third-party modules
from maya import cmds
from maya import OpenMayaUI as omui

try:
    from shiboken2 import wrapInstance
except ImportError:
    from shiboken import wrapInstance

try:
    from PySide2 import QtWidgets
    from PySide2 import QtCore
except ImportError:
    from PySide import QtGui as QtWidgets
    from PySide import QtCore

# Add the parent directory to sys.path to import dayu_widgets
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import local modules
from dayu_widgets.button import MButton
from dayu_widgets.label import MLabel
from dayu_widgets.divider import MDivider
from dayu_widgets.line_edit import MLineEdit


def maya_main_window():
    """Return Maya's main window as a QWidget."""
    main_window_ptr = omui.MQtUtil.mainWindow()
    if sys.version_info.major >= 3:
        return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
    else:
        return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class MayaWidgetTestCase(unittest.TestCase):
    """Test case for dayu_widgets in Maya."""

    def setUp(self):
        """Set up the test environment."""
        self.maya_window = maya_main_window()
        
    def test_button(self):
        """Test MButton in Maya."""
        button = MButton("Test Button")
        self.assertEqual(button.text(), "Test Button")
        
    def test_label(self):
        """Test MLabel in Maya."""
        label = MLabel("Test Label")
        self.assertEqual(label.text(), "Test Label")
        
    def test_line_edit(self):
        """Test MLineEdit in Maya."""
        line_edit = MLineEdit()
        line_edit.setText("Test")
        self.assertEqual(line_edit.text(), "Test")
        
    def test_widget_creation(self):
        """Test creating a widget with Maya main window as parent."""
        widget = QtWidgets.QWidget(self.maya_window)
        self.assertIsNotNone(widget)
        self.assertEqual(widget.parent(), self.maya_window)


def run_tests():
    """Run the tests."""
    suite = unittest.TestLoader().loadTestsFromTestCase(MayaWidgetTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    
if __name__ == "__main__":
    run_tests()
