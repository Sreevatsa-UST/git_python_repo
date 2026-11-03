# Git UI Automation Framework

## Prerequisites

- Python 3.13 with `pip`
- Google Chrome installed locally. The current browser configuration launches Chrome using Playwright's `channel: chrome` setting.
- Git, if you are cloning or pushing the repository
- PowerShell or Git Bash on Windows
- VS Code is optional. The Cucumber/Gherkin extension is useful for feature-file navigation but is not required to run tests.

## Set Up the Environment

Open a terminal at the repository root, the directory containing `features/`.

### PowerShell

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install behave playwright
```

If PowerShell blocks activation, use the venv interpreter directly instead:

```powershell
.\.venv\Scripts\python.exe -m pip install behave playwright
.\.venv\Scripts\python.exe -m behave --version
```

### Git Bash

```bash
py -3.13 -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install behave playwright
```

The framework reads browser settings from `config/environemnt.json` and test data from `testdata/landing_testdata.json`. Keep these files available when running the tests. The browser setting is currently `chrome`, so Google Chrome must be installed; `playwright install chromium` is not needed for this configuration.

## Run Tests

Run the full Behave suite from the repository root:

```bash
python -m behave
```

Run a feature file:

```bash
python -m behave features/landing.feature
python -m behave features/search.feature
python -m behave features/smoke_test.feature
python -m behave features/ui_validation.feature
```

Run one scenario by name:

```bash
python -m behave features/landing.feature --name "Verify Download Page navigation"
```

Run scenarios by tag:

```bash
python -m behave --tags="@Smoke"
python -m behave features/landing.feature --tags="@Functional"
python -m behave --tags="@Regression and @Search"
```

Check feature parsing and step binding without launching a browser:

```bash
python -m behave --dry-run features/search.feature
```

For more scenario-selection and debugging examples, see [behave_commands.md](behave_commands.md).

## Repository Contents

The repository should include the source and test assets needed to reproduce a run: `environment/`, `features/`, `libraries/`, `object_repository/`, `testdata/`, and `config/`, along with documentation. This project does not currently have a dependency lock or requirements file; the install commands above install the direct Python dependencies.

Do not commit the virtual environment (`.venv/` or `venv/`), Python cache files (`__pycache__/`, `*.pyc`), local secrets, or generated test artifacts unless the team intentionally versions those artifacts. Add ignore rules for local-only files before pushing if the repository does not already have them.