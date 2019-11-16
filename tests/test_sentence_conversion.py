import os
from xmldiff import main
from generator import FrameAnnotatorGenerator
def test_sentence_conversion():
    sentence_base = f"{os.path.dirname(os.path.realpath("__file__"))}/data/sentence_"
    input_path = f"{sentence_base}input.txt"
    target_path = f"{sentence_base}target.xml"
    with open(sentence_path, "r") as f:
        sentence = f.read()
    with open(target_path, "r") as f:
        target = f.read()
    converted_tree = FrameAnnotatorGenerator(sentence)
    output = converted_tree.tostring(root, pretty_print=True)
    actions_to_fix_differences = main.diff_texts()
    assert (len(actions_to_fix_differences) == 0)
