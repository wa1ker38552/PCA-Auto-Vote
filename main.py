from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from threading import Thread
import random
import time

casted_votes = 0
crashes = 0
vote_url = 'https://www.votepca.com/vote/the-comedy-show/young-sheldon'

def vote(driver):
    global casted_votes
    email = f"{''.join([random.choice(s) for i in range(random.randint(5, 15))])}@{''.join([random.choice(s) for i in range(random.randint(5, 15))])}.com"
    driver.get(vote_url)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="vote-detail-cat12-H1"]/div/button').click()
    time.sleep(0.5)
    driver.execute_script('document.querySelector("#optin_terms").checked = 1;document.querySelector("#optin_terms").value = true')
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="TelescopeWidgetCategoryVoteModal"]/div/div/div/div/div/div/div/div/form[2]/button').click()
    driver.find_element(By.XPATH, '//*[@id="TelescopeWidgetCategoryVoteModal"]/div/div/div/div/div/div/div/div/form[2]/button').click()
    casted_votes += 1
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="thanks:cat12-Z9"]/button').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="TelescopeWidgetCategoryVote"]/div[1]/div/div/div/div/section[2]/div[2]/a').click()

def start_agent(driver, instance):
    global crashes
    driver.get(vote_url)
    time.sleep(agents)
    print(f'Loaded instance: {instance}')
    while True:
        try:
            # s = time.time()
            vote(driver)
            # e = time.time()
            '''if averages[str(instance)]:
                averages[str(instance)] += e-s
                averages[str(instance)] /= 2
                averages[str(instance)] = round(averages[str(instance)], 2)
            else:
                averages[str(instance)] = round(e - s, 2)'''
        except: crashes += 1

def print_votes():
    global casted_votes, crashes
    while True:
        print(f'votes: {casted_votes}; crashes: {crashes}')
        time.sleep(5)

s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
agents = 4

chrome_options = Options()
# chrome_options.add_argument("--headless=new")
drivers = [webdriver.Chrome(options=chrome_options) for i in range(agents)]

# averages = {}

for i, dr in enumerate(drivers):
    # averages[str(i)] = None
    Thread(target=lambda: start_agent(dr, i)).start()

Thread(target=print_votes).start()
