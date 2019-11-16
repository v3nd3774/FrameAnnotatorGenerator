import os
from datetime import datetime
from nltk import tokenize
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(loader=PackageLoader(f"{os.path.dirname(os.path.realpath("__file__"))}/templates"),
                  autoescape=select_autoescape(["xml"]))
template = env.get_template("FrameAnnotatorInput.xml")
class FrameAnnotatorGenerator(object):
    def __init__(self, input_text):
        """Converts input text into XML input for FrameAnnotator"""
        sentences = nltk.sent_tokenize(input_text)
        template_vars = {"sentence_tuples":enumerate(sentences),
                         "now":datetime.now().strftime("%m/%d/%Y %H:%M:%S %Z %a")}
        return template.render(sentences_tuples=enumerate(sentences))
