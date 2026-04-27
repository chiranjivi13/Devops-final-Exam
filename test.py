import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_web_app():
    # Setup Chrome options for headless mode (important for CI/CD)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Determine the absolute path to the index.html file
        # In CI, we will serve this via a local server or directly using file:// protocol.
        # For simplicity in testing locally, we'll open the local HTML file directly if no URL is provided.
        test_url = os.environ.get("TEST_URL")
        if not test_url:
            file_path = os.path.abspath("index.html")
            test_url = f"file:///{file_path}"
        
        print(f"Testing URL: {test_url}")
        driver.get(test_url)

        # 1. Verify Page Title
        assert "DevOps Demo App" in driver.title, f"Expected title not found. Got: {driver.title}"
        print("✓ Page Title verified.")

        # 2. Find and click the button
        button = driver.find_element(By.ID, "action-btn")
        button.click()
        print("✓ Button clicked.")

        # 3. Verify that the success message appears
        # The class 'hidden' is removed by our JS logic upon clicking.
        # Wait until the element is visible (opacity > 0)
        status_msg = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "status-msg"))
        )
        
        assert status_msg.text == "Button clicked successfully!", "Status message text mismatch"
        print("✓ Success message is visible and correct.")
        
        print("All tests passed successfully!")

    except Exception as e:
        print(f"Test failed: {e}")
        exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_web_app()
