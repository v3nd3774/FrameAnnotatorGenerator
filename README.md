[![Build Status](https://travis-ci.org/v3nd3774/FrameAnnotatorGenerator.svg?branch=master)](https://travis-ci.org/v3nd3774/FrameAnnotatorGenerator)

# FrameAnnotatorGenerator
Repository to store generator for input XML files for [IDIRLab FrameAnnotator](https://idir.uta.edu/frameannotator/).
The full paper for FrameAnnotator is [here](https://rc.library.uta.edu/uta-ir/bitstream/handle/10106/28142/ROY-THESIS-2019.pdf?sequence=1&isAllowed=y).

# How to uninstall?

```
pip uninstall frame-annotator-generator-v3nd3774
```

# How to install?

WIP [on Test PyPi](https://test.pypi.org/project/frame-annotator-generator-v3nd3774/) right now. To install:

```
pip install -i https://test.pypi.org/simple/ frame-annotator-generator-v3nd3774
```

# How do I use it?

First, you'll need a text file that contains sentences, the file extension doesn't matter as long as it
is a plaintext file that contains sentences. Something like this would work:

#### `test.txt`
```
I'm Anderson Cooper moderating tonight's debate, along with CNN's Erin Burnett and New York Times national editor Mark Lacey. We are in Ohio tonight, because it's one of the most critical battleground states. Ohio has backed all but two presidential winners in every election since 1896.

BURNETT: The top 12 Democratic presidential candidates are at their positions behind the podiums. This is a record number of candidates for a presidential primary debate, so to accommodate the large group, there are no opening statements tonight.
```

Then, once installed, simply call the FrameAnnotatorGenerator `fig` like this from the commandline to convert the above text file:

```
fig --source test.txt --target test.xml
```

After the utility runs, there should be a new file at the `target` path with the converted contents.
When run on the above example this is the output:
#### `test.xml`
```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <fullTextAnnotation xsi:schemaLocation="../schema/fullText.xsd" xmlns="http://framenet.icsi.berkeley.edu" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <header>
        <corpus description="Generated User Input" name="Generated User Input" ID="0">
          <document description="Generated User Input" name="Generated User Input" ID="0"/>
        </corpus>
      </header>
      <sentence corpID="0" docID="0" sentNo="1" paragNo="1" aPos="0" ID="1">
        <text>I&#39;m Anderson Cooper moderating tonight&#39;s debate, along with CNN&#39;s Erin Burnett and New York Times national editor Mark Lacey.</text>
        <annotationSet cDate="11/17/2019 04:15:54 UTC Sun" status="UNANN" ID="1">
          <layer rank="1" name="PENN"/>
          <layer rank="1" name="NER"/>
          <layer rank="1" name="WSL"/>
        </annotationSet>
      </sentence>
      <sentence corpID="0" docID="0" sentNo="2" paragNo="1" aPos="0" ID="2">
        <text>We are in Ohio tonight, because it&#39;s one of the most critical battleground states.</text>
        <annotationSet cDate="11/17/2019 04:15:54 UTC Sun" status="UNANN" ID="2">
          <layer rank="1" name="PENN"/>
          <layer rank="1" name="NER"/>
          <layer rank="1" name="WSL"/>
        </annotationSet>
      </sentence>
      <sentence corpID="0" docID="0" sentNo="3" paragNo="1" aPos="0" ID="3">
        <text>Ohio has backed all but two presidential winners in every election since 1896.</text>
        <annotationSet cDate="11/17/2019 04:15:54 UTC Sun" status="UNANN" ID="3">
          <layer rank="1" name="PENN"/>
          <layer rank="1" name="NER"/>
          <layer rank="1" name="WSL"/>
        </annotationSet>
      </sentence>
      <sentence corpID="0" docID="0" sentNo="4" paragNo="1" aPos="0" ID="4">
        <text>BURNETT: The top 12 Democratic presidential candidates are at their positions behind the podiums.</text>
        <annotationSet cDate="11/17/2019 04:15:54 UTC Sun" status="UNANN" ID="4">
          <layer rank="1" name="PENN"/>
          <layer rank="1" name="NER"/>
          <layer rank="1" name="WSL"/>
        </annotationSet>
      </sentence>
      <sentence corpID="0" docID="0" sentNo="5" paragNo="1" aPos="0" ID="5">
        <text>This is a record number of candidates for a presidential primary debate, so to accommodate the large group, there are no opening statements tonight.</text>
        <annotationSet cDate="11/17/2019 04:15:54 UTC Sun" status="UNANN" ID="5">
          <layer rank="1" name="PENN"/>
          <layer rank="1" name="NER"/>
          <layer rank="1" name="WSL"/>
        </annotationSet>
      </sentence>
    </fullTextAnnotation>

```
