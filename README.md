# deafrica-training-workshop
Training material on how to use DE Africa data

Prototype at https://digitalearthafrica.github.io/deafrica-training-workshop/

## To edit docs on the sandbox (replace `<branch_name>`)
```
mkdir dev
cd dev
git clone https://github.com/digitalearthafrica/deafrica-training-workshop.git
cd deafrica-training-workshop
git checkout -b <branch_name>
```
Make your changes
You can use the Git panel to commit files by selecting the menu **Git** -> **Git Interface**
* Click the + next to _Changed_ files to move them  _Staged_
* Click the + next to _Untracked_ files to add them and move them  _Staged_
* Enter a commit message in the _Summary_ field at the bottom of the panel and click commit.
* After you have done the below instructions once, you can use the **Push committed changes** button (cloud with an up arrow) at the top of the panel

```
git config --global credential.helper store
git push --set-upstream origin <branch_name>
```

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
* 	GitHub Actions:
  * Pull Request: make sure it builds
  * Commits to `master` branch: Builds docs, pushed to `gh-pages` branch for publishing to https://digitalearthafrica.github.io/deafrica-training-workshop/

### PDF generation without latex
* To install: `pip install rinohtype`
* To run from docs folder: `sphinx-build -b rinoh . _build/rinoh`
