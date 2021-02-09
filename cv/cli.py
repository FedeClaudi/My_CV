# CLI for printing the CV and saving to file
import typer
from cv.cv import CV


def main(html: str = typer.Option("", help="Path to a HTML fil"),):
    """
        Show my CV
    """
    mycv = CV()
    mycv.show()

    if html:
        mycv.to_html(html)


if __name__ == "__main__":
    typer.run(main)
