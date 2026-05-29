import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
  
@pytest.fixture(scope='function') 
def driver(): 
    """Fixture: buat driver baru setiap test, tutup setelah selesai""" 
    options = webdriver.ChromeOptions() 
    options.add_argument('--start-maximized') 
    # options.add_argument('--headless')  # aktifkan di CI/CD 
    d = webdriver.Chrome( 
        service=Service(ChromeDriverManager().install()), 
        options=options 
    ) 
    yield d  # <-- test berjalan di sini 
    d.quit() # <-- teardown otomatis setelah test 
  
@pytest.fixture(scope='function') 
def login_page(driver): 
    from pages.login_page import LoginPage 
    return LoginPage(driver) 