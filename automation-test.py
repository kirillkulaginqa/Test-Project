# automation-tests.py
from selenium import webdriver

# Инициализация браузера
browser = webdriver.Chrome()
browser.get('https://example.com')

# Проверка заголовка страницы
assert "Example Domain" in browser.title

browser.quit()
