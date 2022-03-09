import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

baseURL = input("Enter link (or links saperated by spaces) from share button or from address bar: ")
url = baseURL.split()
url_list_length = len(url)

options = Options()
options.headless = True
s = Service('./chromedriver')
driver = webdriver.Chrome(service=s, options=options)

i = 0
while i < url_list_length:
    print("Connecting...")
    driver.get(url[i])
    video_url = driver.find_element(by=By.TAG_NAME, value="source").get_attribute("src")
    title = driver.find_element(by=By.CLASS_NAME, value="_eYtD2XCVieq6emjKBH3m").text
    video_title = str(title).replace(" ", "_")

    print("Downloading video...")
    os.system(f'ffmpeg -loglevel error -i "{video_url}" -bsf:a aac_adtstoasc -vcodec copy -c copy -crf 50 videos/{video_title}.mp4')

    print(f'Video "{video_title}" downloaded successfully.')

    def upload():
        answer = input('Do you want to upload this to youtube? Enter "yes" or "no": ')
        if answer == "yes":
            os.system(f"python3 youtube_api.py --file videos/{video_title}.mp4 --title {video_title} --description {video_title} --privacyStatus public")
            print("Uploaded")
        elif answer == "no":
            pass
        else:
            print("Please enter yes or no.")
            upload()

    upload()

    i = i + 1

print("All Done!")