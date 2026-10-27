import json
from pathlib import Path


def navigate_to_url(page):
    config_path = Path(__file__).resolve().parent.parent / "config" / "environemnt.json"
    with config_path.open("r", encoding="utf-8") as f:
        url = json.load(f)["url"]
    page.goto(url)