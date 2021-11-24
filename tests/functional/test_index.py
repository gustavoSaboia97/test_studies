import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.it("Person set data ok")
def test_get_health_info() -> None:
    driver = webdriver.Chrome()
    driver.get('http://localhost:5000/index')
    element = driver.find_element(by=By.XPATH, value='/html/body/a')
    element.click()

    assert driver.current_url == 'https://www.americanas.com.br/'

    driver.quit()
