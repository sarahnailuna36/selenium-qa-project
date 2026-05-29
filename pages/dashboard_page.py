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
        """
        Cek apakah user sedang di halaman dashboard/secure.
        Cukup cek URL saja karena flash message bisa hilang.
        """
        return "secure" in self.get_current_url()

    def get_heading(self):
        """Ambil teks heading halaman (harusnya 'Secure Area')."""
        return self.get_text(self.HEADING)
