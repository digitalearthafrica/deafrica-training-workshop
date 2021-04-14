# deafrica-training-workshop
Training material on how to use DE Africa data at https://training.digitalearthafrica.org/

English: [![Documentation Status](https://readthedocs.org/projects/digital-earth-africa-workshop/badge/?version=latest)](https://training.digitalearthafrica.org/en/latest/?badge=latest) | [RTD](https://readthedocs.org/projects/digital-earth-africa-workshop/)

French: [![Documentation Status](https://readthedocs.org/projects/atelier-digital-earth-africa/badge/?version=latest)](https://training.digitalearthafrica.org/fr/latest/?badge=latest) | [RTD](https://readthedocs.org/projects/atelier-digital-earth-africa/) | [POEditor](https://poeditor.com/projects/po_edit?id_language=50&id=392089)


## To edit docs on the sandbox
(replace `<branch_name>` with the name of your new branch that relates to your change)
```
mkdir dev
cd dev
git clone https://github.com/digitalearthafrica/deafrica-training-workshop.git
cd deafrica-training-workshop
git checkout -b <branch_name>
```
You can now make your changes by adding, editing or deleting notebooks
* 

When you are ready to commit your files, you can use the Git panel.
From the menu bar, select the **Git** -> **Git Interface** (or click the git button on the left panel, a diamond with a branch on it)
* Click the + next to _Changed_ files to move them  _Staged_
* Click the + next to _Untracked_ files to add them and move them  _Staged_
* Enter a commit message in the _Summary_ field at the bottom of the panel and click commit.
* After you have done the below instructions once, you can use the **Push committed changes** button (cloud with an up arrow) at the top of the panel

```
git config --global credential.helper store
git push --set-upstream origin <branch_name>
```
To start a pull request:
* You can now go to https://github.com/digitalearthafrica/deafrica-training-workshop
* There should be a notification box that says something like `<branch_name> recently pushed`. Click the button **Create Pull request**
* Put in a description of your changes
* Add some people to review your changes

> **Troubleshooting:** If you get the error message: 
`remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/digitalearthafrica/deafrica-training-workshop.git'`, 
follow the guide to [creating a personal access token here](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) (**only the "repo" tickbox/scope needs to be selected** in order to push).  
Once you have generated a token (a string of letters and numbers), save the token in a safe location (if you lose this you can regenerate it again). Now you can `git push` and when git asks for your user name and password in the sandbox, enter your GitHub username e.g. `BexDunn` and instead of entering your GitHub password, enter your token string e.g. `3i4htrou3fgffgyy45tysiduhg6779yho87rtiouhihrego7wery`

## To build docs locally
```
git clone https://github.com/digitalearthafrica/deafrica-training-workshop.git
cd deafrica-training-workshop/docs
conda create -c conda-forge -n deafrica-training-workshop pandoc
conda activate deafrica-training-workshop
pip install -r requirements.txt
make html
open _build/html/index.html
```

## To include `.rst` snippets in notebooks
* From the toolbar at the top of the notebook, change from **Markdown** to **Raw**
* On the left panel, click the **cogs icon** and change the **Raw NBConvert Format** to **ReStructured Text** 

## Notes
### Website generation
* For youtube embedding: `pip install ytsphinx`
* For ipynb conversion: you will need to install `pandoc`, either from `conda-forge` or with `apt-get`
* Hosted on ReadTheDocs
  * Project at: https://readthedocs.org/projects/digital-earth-africa-workshop/
* 	GitHub Actions:
  * Pull Request: make sure it builds, failing on warnings

### PDF generation without latex
* To install: `pip install rinohtype`
* To run from docs folder: `sphinx-build -b rinoh . _build/rinoh`
