# Screenshot Actions

# Screeshot Actions
class ScreenshotActios:
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
    
    # Screeshot Full Page
    