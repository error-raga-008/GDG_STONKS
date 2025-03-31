import time
import csv
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
)

# Set up ChromeDriver (Ensure chromedriver.exe is in the specified folder)
chromedriver_path = "C:/Users/Rishi/Desktop/GDG HACKATHON/BERT AI/chromedriver.exe"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# CSV File Setup
output_file = "news_data.csv"
data = [["date", "title", "news_summary"]]  # Column headers

# Set up start and end dates
start_date = datetime.datetime(2010, 1, 1)
end_date = datetime.datetime(2024, 6, 1)
delta = datetime.timedelta(weeks=1)  # Fetch news in weekly intervals

while start_date < end_date:
    next_week = start_date + delta
    formatted_start = start_date.strftime("%d/%m/%Y")
    formatted_end = next_week.strftime("%d/%m/%Y")

    print(f"🔎 Fetching news from {formatted_start} to {formatted_end}...")

    # Google News Search URL with Date Filter
    search_url = (
        f"https://www.google.com/search?q=Adani+Power&tbm=nws&tbs=cdr:1,cd_min:{formatted_start},cd_max:{formatted_end}"
    )
    driver.get(search_url)

    # Wait until news articles appear (max 10 seconds)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.SoaBEf"))
        )
    except:
        print(f"❌ No news found for {formatted_start} to {formatted_end}")
        start_date = next_week
        continue

    # Scroll multiple times to load more articles
    for _ in range(3):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

    # Extract all news articles
    articles = driver.find_elements(By.CSS_SELECTOR, "div.SoaBEf")  # Main news container

    if not articles:
        print(f"❌ No news found for {formatted_start} to {formatted_end}")
    else:
        for article in articles:
            try:
                title_element = article.find_element(By.CSS_SELECTOR, "div.MBeuO")
                title = title_element.text

                summary_element = article.find_elements(By.CSS_SELECTOR, "div.GI74Re.nDgy9d")  # Summary text
                summary = summary_element[0].text if summary_element else "No summary available"

                data.append([formatted_start, title, summary])  # Removed link
            except Exception as e:
                print(f"⚠️ Error extracting news: {e}")

    start_date = next_week  # Move to next week

# Save to CSV file
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"✅ News data saved to {output_file}")

# Close browser
driver.quit()