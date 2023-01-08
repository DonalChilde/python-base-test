"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Python Base Test."""


if __name__ == "__main__":
    main(prog_name="python-base-test")  # pragma: no cover