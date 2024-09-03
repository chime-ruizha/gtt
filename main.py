from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class GitTUI(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    TITLE = "Visual Git"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = GitTUI()
    app.run()


# If there are multiple actions one can take, this is the first screen
class ActionTUI:
    def __init__(self):
        pass


# If the user wants to amend files to commit, this is the screen
class AmendTUI:
    def __init__(self):
        pass


# If the user wants to commit, this is the screen
class CommitTUI:
    def __init__(self):
        pass


# File picker UI
class FileTUI:
    def __init__(self):
        pass


# Kicked off if there is a conflict
class ConflictTUI:
    def __init__(self):
        pass


# Used to diff two files
class DiffTUI:
    def __init__(self):
        pass
