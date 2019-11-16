import os
from xmldiff import main
from generator import FrameAnnotatorGenerator
def test_paragraph_conversion():
    paragraph_base = f"{os.path.dirname(os.path.realpath("__file__"))}/data/paragraph_"
    input_path = f"{paragraph_base}input.txt"
    target_path = f"{paragraph_base}target.xml"
    with open(paragraph_path, "r") as f:
        paragraph = f.read()
    with open(target_path, "r") as f:
        target = f.read()
    converted_tree = FrameAnnotatorGenerator(paragraph)
    output = converted_tree.tostring(root, pretty_print=True)
    actions_to_fix_differences = main.diff_texts()
    assert (len(actions_to_fix_differences) == 0)
