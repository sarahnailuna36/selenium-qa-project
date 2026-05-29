from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):

    URL = "https://the-internet.herokuapp.com/secure"

    # ── Locators ──────────────────────────────────────
    LOGOUT_BTN = (By.CSS_SELECTOR, "a[href='/logout']")
    FLASH_MSG  = (By.ID, "flash")
    HEADING    = (By.TAG_NAME, "h2")

    # ── Actions ───────────────────────────────────────
    def logout(self):
        """Klik tombol Logout."""
        self.logger.info("Melakukan logout")
        self.click(self.LOGOUT_BTN)

    # ── Assertion Helpers ─────────────────────────────
    def is_on_dashboard(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("secure")
                )
            return True
        except:
            return False

    def get_heading(self):
        """Ambil teks heading halaman (harusnya 'Secure Area')."""
        return self.get_text(self.HEADING)
