**MS Team Autoconnect meeting!!!**
A Python script to automate joining Microsoft Teams meetings.

**Key Features:**

1. Automatic meeting joiner
2. Auto-mute microphone and disable camera before joining
3. Configurable automatic login
   
**Script Requirements:**

- Python 3.x
- selenium and webdriver libraries
- Microsoft Teams desktop application
- Chromedriver.exe
- Used Web Elements (Xpath)

**How to Use this Repo?**
1.Install chromedriver extension and check its version with Google Chrome browser (Should be compatible)(Starting 8 digit should be same then it only be compatible)
Chrome Version 129.0.6668.58 (Browser)
Chromedriver version 129.0.6668.(Chromedriver)
2-create a new folder and Clone this Repo (https://github.com/Inaya791/MS-Team-AutoConnect-Meeting.git)
Command: git clone https://github.com/Inaya791/MS-Team-AutoConnect-Meeting.git
make sure after cloning your chromedriver extension should be within this folder.
3.Navigate to path cd MS-Team-AutoConnect-Meeting
4.Install the required python Libraries
Command: pip install -r requirement.txt
5.YAY! Finally you to hit the command in your CLI Terminal.
Command: python app.py

**The Challenge Triggered** (https://github.com/Inaya791/MS-Team-AutoConnect-Meeting/commit/5f3d3c3b80e0ee81edcc646aec6341006e12c4bc)
To handle the default popups from MS Teams Web Application.
Solutions:This piece of Code help m eout execute my Sccript well.
        # Extract the updated meeting link after joining
        updated_meeting_link = driver.current_url
        print(f"Extracted updated meeting link: {updated_meeting_link}")

        # Open the new meeting link in a new tab
        driver.execute_script("window.open('');")  # Open a new blank tab
        driver.switch_to.window(driver.window_handles[1])  # Switch to the new tab

        # Load the extracted meeting link in the new tab
        driver.get(updated_meeting_link)
        print(f"Opening the extracted meeting link in a new tab: {updated_meeting_link}")

**Thank you for ramping on my Github project!!!Will catch you soon for Coffee!!!**
