import os
import csv
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def load_register_csv():
    filepath = os.path.join(
        os.path.dirname(__file__), "..", "data", "register_data.csv"
    )
    filepath = os.path.normpath(filepath)
    rows = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append((
                row["username"],
                row["password"],
                row["expected"],
                row["description"],
            ))
    return rows


DATA = load_register_csv()


class TestRegisterDDT:

    @pytest.mark.parametrize(
        "username, password, expected, description",
        DATA,
        ids=[d[3] for d in DATA],
    )
    def test_register(self, driver, username, password, expected, description):
        driver.get("https://demoqa.com/register")
        wait = WebDriverWait(driver, 10)

        if username:
            field = wait.until(EC.presence_of_element_located((By.ID, "userName")))
            field.clear()
            field.send_keys(username)

        if password:
            field = wait.until(EC.presence_of_element_located((By.ID, "password")))
            field.clear()
            field.send_keys(password)

        btn = wait.until(EC.presence_of_element_located((By.ID, "register")))