# Import built-in modules
import os
import sys
from pathlib import Path

# Import third-party modules
import nox


@nox.session
def maya_test(session: nox.Session) -> None:
    """Run tests in Maya environment using Docker."""
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
    
    # Run the Maya tests using Docker
    # Note: This assumes the Docker image is available and the host has Docker installed
    session.run(
        "docker", "run", "--rm",
        "-v", f"{root_dir}:/dayu_widgets",
        "-w", "/dayu_widgets",
        "mottosso/maya:2022",
        "mayapy", "tests/run_maya_tests.py",
        env=env,
        external=True
    )
