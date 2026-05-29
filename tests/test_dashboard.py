import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestDashboard:

    def test_login_redirect_ke_dashboard(self, driver):
        """
        TC-DASH-001: Setelah login berhasil,
        user harus berada di halaman dashboard (/secure).
        """
        login = LoginPage(driver)
        login.login("tomsmith", "SuperSecretPassword!")

        dashboard = DashboardPage(driver)
        assert dashboard.is_on_dashboard(), \
            "Setelah login berhasil, harus ada di halaman /secure"

    def test_logout_kembali_ke_login(self, driver):
        """
        TC-DASH-002 (TUGAS UTAMA): Setelah logout,
        user harus kembali ke halaman login (/login).
        """
        # Step 1: Login dulu
        login = LoginPage(driver)
        login.login("tomsmith", "SuperSecretPassword!")

        # Step 2: Verifikasi sudah di dashboard
        dashboard = DashboardPage(driver)
        assert dashboard.is_on_dashboard(), \
            "Harus di dashboard sebelum bisa logout"

        # Step 3: Logout
        dashboard.logout()
        # Step 4: Tunggu URL berpindah ke /login
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(driver, 10).until(EC.url_contains("login"))
        assert "login" in driver.current_url, \
            "Setelah logout, URL harus kembali ke /login"

    def test_flash_message_setelah_logout(self, driver):
        """
        TC-DASH-003: Setelah logout, muncul pesan
        konfirmasi bahwa user sudah logout.
        """
        login = LoginPage(driver)
        login.login("tomsmith", "SuperSecretPassword!")

        dashboard = DashboardPage(driver)
        dashboard.logout()

        # Tunggu sampai URL kembali ke /login dulu
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(driver, 10).until(EC.url_contains("login"))

        msg = login.get_flash_message()
        assert "logged out" in msg.lower(), \
            f"Pesan logout tidak sesuai: {msg}"