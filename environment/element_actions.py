# Element Actions 

class ElementActions:
    # Click Functionality
    def click(page, locator):
        try:
            page.locator(locator).click(timeout=5000)
            return True
        except Exception as e:
            raise Exception(f"Unable to click '{locator}': {e}")

    # Enter Text
    def enter_text(page, locator, text):
        try:
            page.locator(locator).fill(text)
            return True
        except Exception as e:
            raise Exception(
                f"Failed to enter text '{text}' in locator '{locator}'. Error: {str(e)}"
            )

    # Clear text 
    def clear_text(page, locator):
        try:
            page.locator(locator).fill("")
            return True
        except Exception as e:
            raise Exception(
                f"Failed to clear text from locator '{locator}'. Error: {e}"
            )

    # Double Click
    def double_click(page, locator):
        try:
            page.locator(locator).dblclick()
            return True
        except Exception as e:
            raise Exception(
                f"Failed to double click on locator '{locator}'. Error: {e}"
            )

    # Right Click
    def right_click(page, locator):
        try:
            page.locator(locator).click(button="right")
            return True
        except Exception as e:
            raise Exception(
                f"Failed to right click on locator '{locator}'. Error: {e}"
            )

    # Hover 
    def hover(page, locator):
        try:
            page.locator(locator).hover()
            return True
        except Exception as e:
            raise Exception(
                f"Failed to hover over locator '{locator}'. Error: {e}"
            )

    # Get Text
    def get_text(page, locator):
        try:
            text = page.locator(locator).text_content()
            return text.strip() if text else ""
        except Exception as e:
            raise Exception(
                f"Failed to get text from locator '{locator}'. Error: {e}"
            )