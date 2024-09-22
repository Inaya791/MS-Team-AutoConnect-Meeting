from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import traceback

# Configure Chrome options
chrome_options = Options()
# Uncomment this for headless mode if needed
# chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-notifications")  # Disable notifications
chrome_options.add_argument("--disable-popup-blocking")  # Disable pop-up blocking
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.notifications": 2
})

# Initialize ChromeDriver service
service = Service(executable_path='./chromedriver.exe')  # Path to your chromedriver (within the folder )

# Create WebDriver instance
driver = webdriver.Chrome(service=service, options=chrome_options)

def join_teams_meeting(meeting_link):
    try:
        # Open the Teams meeting link
        driver.get(meeting_link)
        print(f"Opening the meeting link: {meeting_link}")
        sleep(30)  # Wait for the page to load completely (adjust the time if necessary)
        #why this is  done because to overcome with MS team popups 
        # Extract the new meeting URL after joining (if the URL changes)
        updated_meeting_link = driver.current_url
        print(f"Extracted updated meeting link: {updated_meeting_link}")

        # You can use this link for any further automation or save it for later use
        print(f"Now using the updated meeting link to re-open the meeting...")

        # Re-open the meeting with the new link (or you can store it somewhere as needed)
        driver.get(updated_meeting_link)
        sleep(5)  # Wait for the page to load

        # Click on "Continue on this browser"
        try:
            continue_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[2]/button[1]/div/h3'))
            )
            continue_button.click()
            print("Clicked 'Continue on this browser'")
        except Exception as e:
            print("Failed to find or click 'Continue on this browser' button. Error:", e)

        # Click on "Continue without audio or video"
        try:
            no_audio_video_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div[2]/div/div[1]/div/button'))
            )
            no_audio_video_button.click()
            print("Clicked 'Continue without audio or video'")
        except Exception as e:
            print("Failed to find or click 'Continue without audio or video' button. Error:", e)

        # Enter bot name
        try:
            name_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[5]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/span/input'))
            )
            name_input.clear()
            name_input.send_keys("AIBot")  # Replace with your bot's name
        except Exception as e:
            print("Failed to find or input bot name. Error:", e)
        
        # Click on "Join now" button
        try:
            join_now_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[5]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/button[2]'))
            )
            join_now_button.click()
        except Exception as e:
            print("Failed to find or click 'Join now' button. Error:", e)

        # Wait for the meeting to fully load
        sleep(30)

    except Exception as e:
        print("Error in the meeting process.")
        traceback.print_exc()

    finally:
        driver.quit()

if __name__ == '__main__':
    # Replace with your actual Teams meeting link
    meeting_link = "https://teams.microsoft.com/l/meetup-join/" 
    join_teams_meeting(meeting_link)
