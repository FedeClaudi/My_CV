# CLI for printing the CV and saving to file
import typer
from cv.cv import CV

app = typer.Typer()


@app.command()
def main(html: str = "",):
    """
        Show my CV
    """
    mycv = CV()
    mycv.show()

    if html:
        mycv.to_html(html)


if __name__ == "__main__":
    app()
