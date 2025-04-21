# Import built-in modules
import os
import sys
from pathlib import Path

# Import third-party modules
import nox


@nox.session
def blender_test(session: nox.Session) -> None:
    """Run tests in Blender environment."""
    # Get the project root directory
    root_dir = Path(__file__).parent.parent.absolute()
    
    # Install dependencies
    session.install("pytest>=7.0.0", "pytest-cov>=4.1.0")
    
    # Install the package with PySide6 (Blender 3.x+ uses PySide6)
    session.install("-e", ".[pyside6]")
    
    # Set environment variables
    env = {
        "QT_API": "pyside6",
        "PYTHONPATH": str(root_dir),
        "CI": "1"
    }
    
    # On Linux, we need to install Blender
    if sys.platform.startswith("linux"):
        # Install Blender (this is for Ubuntu)
        session.run("sudo", "apt-get", "update", external=True)
        session.run("sudo", "apt-get", "install", "-y", "blender", external=True)
    elif sys.platform == "darwin":  # macOS
        # Install Blender using Homebrew
        session.run("brew", "install", "blender", external=True)
    elif sys.platform == "win32":  # Windows
        # On Windows, we would need to download and install Blender manually
        # This is more complex and might require a separate script
        session.skip("Blender tests not supported on Windows in CI yet")
        return
    
    # Run the Blender tests
    session.run(
        "blender", "--background", "--python", "tests/run_blender_tests.py",
        env=env,
        external=True
    )
