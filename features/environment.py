import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from libraries.screenshot_actions import ScreenshotActions

FAILURE_STATUSES = {"failed", "error", "hook_error", "cleanup_error"}


def before_all(context):
    project_root = Path(__file__).resolve().parent.parent
    config_path = project_root / "config" / "environemnt.json"
    with config_path.open("r", encoding="utf-8") as config_file:
        browser_config = json.load(config_file)

    context.project_root = project_root
    context.execution_started = time.monotonic()
    context.execution_summary = {
        "application": browser_config["url"],
        "browser": browser_config["browser"],
        "total_scenarios": 0,
        "passed": 0,
        "failed": 0,
        "skipped": 0,
        "execution_time": "0s",
        "failure_screenshots": [],
        "screenshot_errors": [],
    }


def before_scenario(context, scenario):
    context.failure_screenshot = None


def after_step(context, step):
    status = getattr(step.status, "name", str(step.status)).lower()
    if status not in FAILURE_STATUSES or context.failure_screenshot:
        return

    try:
        context.failure_screenshot = ScreenshotActions.capture_failure_screenshot(
            getattr(context, "page", None),
            f"{context.scenario.name}_{step.name}",
        )
    except Exception as error:
        context.execution_summary["screenshot_errors"].append(str(error))


def after_scenario(context, scenario):
    summary = context.execution_summary
    summary["total_scenarios"] += 1
    status = getattr(scenario.status, "name", str(scenario.status)).lower()

    if status == "passed":
        summary["passed"] += 1
    elif status in FAILURE_STATUSES:
        summary["failed"] += 1
        screenshot_path = context.failure_screenshot
        if not screenshot_path:
            try:
                screenshot_path = ScreenshotActions.capture_failure_screenshot(
                    getattr(context, "page", None),
                    scenario.name,
                )
            except Exception as error:
                summary["screenshot_errors"].append(str(error))
        if screenshot_path:
            summary["failure_screenshots"].append(screenshot_path)
    else:
        summary["skipped"] += 1


def after_all(context):
    elapsed_seconds = int(time.monotonic() - context.execution_started)
    minutes, seconds = divmod(elapsed_seconds, 60)
    context.execution_summary["execution_time"] = (
        f"{minutes}m {seconds}s" if minutes else f"{seconds}s"
    )

    summary_path = (
        context.project_root / "reports" / "latest" / "execution_summary.json"
    )
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    with summary_path.open("w", encoding="utf-8") as summary_file:
        json.dump(context.execution_summary, summary_file, indent=4)
        summary_file.write("\n")