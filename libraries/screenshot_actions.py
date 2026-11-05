import re
from datetime import datetime
from pathlib import Path


class ScreenshotActions:

    @staticmethod
    def capture_failure_screenshot(page, scenario_name="scenario"):
        if page is None:
            raise RuntimeError("Cannot capture a failure screenshot: no page is available")
        if page.is_closed():
            raise RuntimeError("Cannot capture a failure screenshot: the page is closed")

        project_root = Path(__file__).resolve().parent.parent
        screenshots_dir = project_root / "reports" / "screenshots"
        screenshots_dir.mkdir(parents=True, exist_ok=True)

        safe_name = re.sub(r"[^A-Za-z0-9._-]+", "_", scenario_name).strip("._")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        screenshot_path = screenshots_dir / f"failure_{safe_name}_{timestamp}.png"
        page.screenshot(path=str(screenshot_path), full_page=True)

        return screenshot_path.relative_to(project_root).as_posix()

# Full Screenshot Actions
class FullScreenshotActions:
    def capture_screenshot(page, file_name):
        try:
            page.screenshot(
                path=file_name,
                full_page=True
            )
            return True
        except Exception as e:
            raise Exception(
                f"Failed to capture screenshot '{file_name}'. Error: {e}"
            )