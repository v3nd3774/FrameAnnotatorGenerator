import os
import pytz
import nltk
from datetime import datetime
from jinja2 import Environment, select_autoescape
TEMPLATE = """
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <fullTextAnnotation xsi:schemaLocation="../schema/fullText.xsd" xmlns="http://framenet.icsi.berkeley.edu" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <header>
        <corpus description="Generated User Input" name="Generated User Input" ID="0">
          <document description="Generated User Input" name="Generated User Input" ID="0"/>
        </corpus>
      </header>
      {%- for sentence in sentence_tuples %}
      <sentence corpID="0" docID="0" sentNo="{{sentence[0]}}" paragNo="1" aPos="0" ID="{{sentence[0]}}">
        <text>{{sentence[1]}}</text>
        <annotationSet cDate="{{now}}" status="UNANN" ID="{{sentence[0]}}">
          <layer rank="1" name="PENN"/>
          <layer rank="1" name="NER"/>
          <layer rank="1" name="WSL"/>
        </annotationSet>
      </sentence>
      {%- endfor %}
    </fullTextAnnotation>
""".strip()
template = Environment(autoescape=select_autoescape(["xml"])).from_string(TEMPLATE)
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")
class FrameAnnotatorGenerator(object):
    @classmethod
    def convert(cls, input_text):
        """Converts input text into XML input for FrameAnnotator"""
        sentences = nltk.sent_tokenize(input_text)
        sentence_tuples = [(idx + 1, sent) for idx, sent in enumerate(sentences)]
        template_vars = {"sentence_tuples":sentence_tuples,
                         "now":datetime.now(pytz.utc).strftime("%m/%d/%Y %H:%M:%S %Z %a")}
        return template.render(**template_vars)
