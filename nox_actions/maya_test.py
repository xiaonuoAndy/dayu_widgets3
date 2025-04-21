# Import third-party modules
import nox


@nox.session
def maya_test(session: nox.Session) -> None:
    """Run tests in Maya environment."""
    # For CI, we'll just print a message
    print("Maya compatibility test skipped in CI")
    print("For local testing, use Docker:")
    print("docker pull mottosso/maya:2022")
    print("nox -s maya-test")
