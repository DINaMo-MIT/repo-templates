# repo-templates
Templates for codes

## Tools Installation
Several tools configured to allow source code to be formatted and checked
* [pre-commit](https://pre-commit.com) automatically checks for various issues prior to committing to the git repository and does some basic code linting.
* [black](https://black.readthedocs.io/en/stable/) formats your python code so that you don't have to think about it.
* [flake8](https://flake8.pycqa.org) checks your python code for errors.
* [pytest](https://docs.pytest.org/) for unit testing and code coverage checks


Notes:

* `black` and `flake8` can be used in VS Code (manually or automatically) and are also used in `pre-commit` (with other hooks). Settings have been created to be consistent for both cases.
* Create a conda environment, install the requirements, and set your VS Code python interpreter **before** editing files in VS Code. Otherwise VS Code will ask you to install `black`, `flake8` etc into your base python environment.

Then create the environment and install pre-commit using:
```
conda activate myCondaEnv
conda install -c conda-forge pre_commit black
conda install -c anaconda flake8 pytest
pre-commit install
```

### Pre-commit hooks

The following pre-commit hooks have been configured in `.pre-commit-config.yaml`:

* `check-yaml`: checks and fixes format of yaml files
* `check-json5`: checks and fixes format of json files
* `end-of-file-fixer`: ensures consistency
* `trailing-whitespace`: ensures consistency
* `check-added-large-files`: ensures large files do not accidentally get committed
* `check-git-config-email`: ensures that MERL email addresses are used for commits
* `black`: code formatter
* `isort`: sorts imports
* `pyupgrade`: can upgrade code to new python versions (commented for now)
* `flake8`: code checker

When developing, `flake8` can sometimes be annoying as it will pick up on errors that you may not care about in the moment. By default, we have set it to output warnings only (not errors), but you should consider changing this. See `.pre-commit-config.yaml` for details.

You can manually run `pre-commit` using (works on all files in git or staged for a git commit):
```bash
pre-commit run --all-files
```

It will also run each time you commit your files (and stop the commit if it finds a problem - see below).
