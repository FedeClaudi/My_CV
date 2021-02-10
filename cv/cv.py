from rich.console import Console
from rich import print
from rich.terminal_theme import TerminalTheme

from cv import make


CV_THEME = TerminalTheme(
    (30, 30, 30),
    (220, 220, 220),
    [
        (255, 255, 255),
        (128, 0, 0),
        (0, 128, 0),
        (128, 128, 0),
        (0, 0, 128),
        (128, 0, 128),
        (0, 128, 128),
        (192, 192, 192),
    ],
    [
        (128, 128, 128),
        (255, 0, 0),
        (0, 255, 0),
        (255, 255, 0),
        (0, 0, 255),
        (255, 0, 255),
        (0, 255, 255),
        (255, 255, 255),
    ],
)


class CV:
    def __init__(self, WIDTH=150):
        """
            Class showing my CV, printing it to screen and saving to HTML
        """
        self.WIDTH = WIDTH

        # try to get projects info from github
        try:
            projs = make.projs(self.WIDTH - 12)
        except Exception:  # too many API requests
            print("Could not get github projects info, likely API problems")
            projs = ""

        self.contents = [
            make.bio(self.WIDTH),
            "\n",
            make.cv(self.WIDTH),
            make.pubs(self.WIDTH - 12),
            projs,
        ]

    def __rich_console__(self, *args, **kwargs):
        yield from self.contents

    def show(self):
        """
            Print the CV to console
        """
        print(self)

    def to_html(self, path):
        """
            Save the content to a HTML file
        """
        htmlconsole = Console(record=True)
        htmlconsole.print(self)
        htmlconsole.save_html(path, theme=CV_THEME)
