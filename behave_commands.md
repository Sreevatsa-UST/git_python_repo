# Behave Test Commands

Run these commands from the repository root in Bash. Behave discovers feature files under `features/` and step definitions under `features/steps/`.

## Run Tests

Run the complete suite:

```bash
behave
```

Run every feature in the feature folder:

```bash
behave features/
```

Run one feature file:

```bash
behave features/landing.feature
behave features/search.feature
behave features/smoke_test.feature
behave features/ui_validation.feature
```

## Run One Scenario

Select by scenario name:

```bash
behave features/landing.feature --name "Verify Download Page navigation"
```

Or select by the line where the scenario starts:

```bash
behave features/landing.feature:5
```

`--name` uses a regular expression. Match the scenario name closely to avoid selecting other scenarios.

## Run a Scenario Outline

Run every Examples row for the menu outline:

```bash
behave features/landing.feature --name "Verify menu navigation"
```

Run one generated Examples row. Replace `@1.1` with the row number shown in Behave's output:

```bash
behave features/landing.feature --name "Verify menu navigation -- @1.1"
```

## Run by Tag

Run all smoke-tagged scenarios:

```bash
behave --tags='@Smoke'
```

Run functional scenarios in the landing feature:

```bash
behave features/landing.feature --tags='@Functional'
```

Combine tags with AND or OR:

```bash
behave --tags='@Regression and @Search'
behave --tags='@Smoke or @Functional'
```

Exclude a tag:

```bash
behave --tags='not @Negative'
```

## Diagnose a Feature

Parse the feature and check step binding without launching the browser:

```bash
behave --dry-run features/search.feature
```

Show step output while running:

```bash
behave --no-capture --format=pretty features/search.feature
```

Use a tag or `--name` together with `--no-capture` to debug only the target scenario.

## If `behave` Is Not on PATH

Run Behave through the Python interpreter where it is installed:

```bash
python -m behave features/search.feature
```

The Python environment used for the command must have Behave, Playwright, and the required browser installed.