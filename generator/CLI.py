import click
from generator import FrameAnnotatorGenerator

@click.command()
@click.option('--source', '-s')
@click.option('--target', '-t')
def main(source, target):
    print("Reading input...")
    with open(source, "r") as f:
        paragraph = f.read()
    print("Converting...")
    actual_out = FrameAnnotatorGenerator.convert(paragraph)
    with open(target, "w") as f:
        f.write(actual_out)
    print("Done, enjoy! :)")
if __name__ == "__main__":
    main()
