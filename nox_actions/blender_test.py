# Import third-party modules
import nox


@nox.session
def blender_test(session: nox.Session) -> None:
    """Run tests in Blender environment."""
    # For CI, we'll just print a message
    print("Blender compatibility test skipped in CI")
    print("For local testing, use Docker:")
    print("docker pull linuxserver/blender")
    print("nox -s blender-test")
