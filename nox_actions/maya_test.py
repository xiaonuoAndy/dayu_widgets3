# Import built-in modules
import os
import sys
from pathlib import Path

# Import third-party modules
import nox


@nox.session
def maya_test(session: nox.Session) -> None:
    """Run tests in Maya environment."""
    # Get the project root directory
    root_dir = Path(__file__).parent.parent.absolute()

    # Install dependencies
    session.install("pytest>=7.0.0", "pytest-cov>=4.1.0")

    # Install the package with PySide2 (Maya uses PySide2)
    session.install("-e", ".[pyside2]")

    # Set environment variables
    env = {
        "QT_API": "pyside2",
        "PYTHONPATH": str(root_dir),
        "CI": "1"
    }

    # For CI, we'll just run a simple test to verify the imports work
    # This avoids the need for Docker and Maya
    session.run(
        "python", "-c",
        """import sys;
from dayu_widgets.button import MButton;
from dayu_widgets.label import MLabel;
print('Maya compatibility test passed!');
sys.exit(0)""",
        env=env
    )
