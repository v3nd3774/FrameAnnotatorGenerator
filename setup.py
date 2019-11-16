import setuptools
with open("README.md", "r") as f:
  long_description = f.read()
setuptools.setup(
  name="frame-annotator-generator-v3nd3774",
  version="0.0.1",
  author="Josue Caraballo",
  author_email="josue.caraballo@gmail.com",
  description="Generates input XMLs for IDIRLab FrameAnnotator web application.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/v3nd3774/FrameAnnotatorGenerator",
  packages=setuptools.find_packages(),
  entry_points={'console_scripts':["fig=generator:CLI.main"]},
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ]
)
