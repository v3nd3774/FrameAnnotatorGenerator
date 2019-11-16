import os
import pdb
from xmldiff import main
from generator import FrameAnnotatorGenerator
def test_sentence_conversion():
    sentence_base = f"{os.path.dirname(os.path.realpath(__file__))}/data/sentence_"
    input_path = f"{sentence_base}input.txt"
    target_path = f"{sentence_base}target.xml"
    with open(input_path, "r") as f:
        sentence = f.read()
    with open(target_path, "rb") as f:
        target = f.read()
    actual_out = FrameAnnotatorGenerator.convert(sentence).encode("UTF-8")
    actions_to_fix_differences = main.diff_texts(actual_out, target)
    # Assert that only changes that need to happen are to the timestamp
    assert (len(actions_to_fix_differences) ==
            len([action for action in actions_to_fix_differences if action.name == "cDate"]))
