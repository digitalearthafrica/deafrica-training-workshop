# deafrica-training-workshop
Training material on how to use DE Africa data

Prototype at https://digitalearthafrica.github.io/notebooks-training/index.html

## Website generation
* For youtube embedding: `pip install ytsphinx`
* Contents of `_build` folder pushed to `gh-pages` branch

## PDF generation without latex
* To install: `pip install rinohtype`
* To run from docs folder: `sphinx-build -b rinoh . _build/rinoh`
