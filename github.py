from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from credential import USERNAME, PASSWORD
import time
import os

class GitHub():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument(f"--user-data-dir={os.getcwd()}\profile")
        options.add_argument('--headless')  
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.browser = webdriver.Chrome(options=options)

   
    def login(self):
        self.browser.get("https://github.com/login")
        try:
            username = self.browser.find_element(By.NAME, 'login')
        except:
            print("Already login")
            return

        username.send_keys(USERNAME)

        password = self.browser.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)

        submit = self.browser.find_element(By.NAME, 'commit')
        submit.click()
        print("Login successful")


    def logout(self):
        self.browser.get("https://github.com/logout")
        logout = self.browser.find_element(By.XPATH, '//*[@id="js-pjax-container"]/div/form/input[2]')
        logout.click()
        print("Logout successful")


    def create(self, repo, flag=0):
        self.browser.get('https://github.com/new')

        try:
            repoName = self.browser.find_element(By.NAME, 'repository[name]')
        except:
            print("Login first")
            return

        repoName.send_keys(repo)

        if flag:
            privacy = self.browser.find_element(By.ID, "repository_visibility_private")
        else:
            privacy = self.browser.find_element(By.ID, "repository_visibility_public")

        privacy.click()

        readme = self.browser.find_element(By.ID, 'repository_auto_init')
        readme.click()

        privacy.submit()

        if self.browser.find_elements(By.ID, "code-tab"):
            print(f"{repo} created")
        else:
            print("repository with same already exist")
        

    def upload(self, repo, paths):
        self.browser.get(f"https://github.com/{USERNAME}/{repo}/upload/main")
        try:
            upload = self.browser.find_element(By.ID, 'upload-manifest-files-input')
        except:
            print("Login first")
            return
        
        for path in paths.split(" "):
            filename = path.split("\\")[-1]
            if os.path.isfile(path):
                upload.send_keys(path)
                print(f"Upload successful: {filename}")
                time.sleep(5)
            else:
                print(f"{filename} does not exist")
        
        submit = self.browser.find_element(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/form/button')
        submit.click()
        time.sleep(5)
        
            

            
    def list(self):
        self.browser.get(f"https://github.com/{USERNAME}?tab=repositories")
        repo_count = self.browser.find_element(By.XPATH, '//*[@id="js-pjax-container"]/div[1]/div/div/div[2]/div/nav/a[2]/span').text
        for i in range(int(repo_count)):
            repo_name = self.browser.find_element(By.XPATH, f'//*[@id="user-repositories-list"]/ul/li[{i+1}]/div[1]/div[1]/h3/a').text
            status = self.browser.find_element(By.XPATH, f'//*[@id="user-repositories-list"]/ul/li[{i+1}]/div[1]/div[1]/h3/span[2]').text
            print(f"{i+1}. {repo_name} ({status})")


    def readme(self, repo):
        self.browser.get(f"https://github.com/{USERNAME}/{repo}/blob/main/README.md")
        try:
            header = self.browser.find_element(By.XPATH, '//*[@id="readme"]/article/h1').text
        except:
            print("Invalid repository name")
            return

        print(header)
        if len(self.browser.find_elements(By.XPATH, '//*[@id="readme"]/article/p')):
            body = self.browser.find_element(By.XPATH, '//*[@id="readme"]/article/p').text
            print(body)
        

    def status(self, repo):
        self.browser.get(f"https://github.com/{USERNAME}/{repo}")
        try:
            stars = self.browser.find_element(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div/div[3]/div[2]/div/div[1]/div/div[4]/a/strong').text
        except:
            print("Invalid repository name")
            return
            
        watching = self.browser.find_element(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div/div[3]/div[2]/div/div[1]/div/div[5]/a/strong').text
        forks = self.browser.find_element(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div/div[3]/div[2]/div/div[1]/div/div[6]/a/strong').text
        print("Stars:", stars)
        print("Watching:", watching)
        print("Forks:", forks)


    def issues(self, repo):
        self.browser.get(f"https://github.com/{USERNAME}/{repo}/pulse")
        try:
            issues_count = self.browser.find_element(By.XPATH, '//*[@id="new-issues"]/span/span[1]').text
        except:
            if len(self.browser.find_elements(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div/div[2]/div[2]/ul/li[2]/ul/li[4]/span[1]')):
                print("No issues found.")
            else:
                print("Invalid repository name")
            return

        print(f"Total issues: {issues_count}")
        for i in range(int(issues_count)):
            issue_name = self.browser.find_element(By.XPATH, f'//*[@id="issues"]/ul[2]/li[{i+1}]/div/a').text
            issue_des = self.browser.find_element(By.XPATH, f'//*[@id="issues"]/ul[2]/li[{i+1}]/div/p').text
            print(issue_name + ":", issue_des)
        

    def pullrequests(self, repo):
        self.browser.get(f"https://github.com/{USERNAME}/{repo}/pulse")
        try:
            pullrequest_count = self.browser.find_element(By.XPATH, '//*[@id="proposed-pull-requests"]/span/span[1]').text
        except:
            if len(self.browser.find_elements(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div/div[2]/div[2]/ul/li[2]/ul/li[2]/span[1]')):
                print("No pullrequests found.")
            else:
                print("Invalid repository name")
            return

        print(f"Total pullrequests: {pullrequest_count}")
        for i in range(int(pullrequest_count)):
            pullrequest_name = self.browser.find_element(By.XPATH, f'//*[@id="pull-requests"]/ul/li[{i+1}]/div/a').text
            pullrequest_des = self.browser.find_element(By.XPATH, f'//*[@id="pull-requests"]/ul/li[{i+1}]/div/p').text
            print(pullrequest_name + ":", pullrequest_des)


    def fork(self, url):
        try:
            self.browser.get(url)
            if len(self.browser.find_elements(By.ID, "not-found-search")):
                print("Invalid URL")
                return
        except:
            print("Invalid URL")
            return

        try:
            fork = self.browser.find_element(By.XPATH, '//*[@id="repository-container-header"]/div[1]/ul/li[2]/form/button')    
        except:
            print("Login first")
            return

        fork.click()
        try:
            WebDriverWait(self.browser, 5).until_not(EC.visibility_of_element_located((By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div/h3')))
            print("Fork successful")
        except:
            return

    def close(self):
        self.browser.quit()
    

if __name__ == "__main__":
    git = GitHub()
    
    #git.login()
    #git.logout()
    #git.create('654654dafdfas646546', 1)
    #git.upload('name', r'C:\Users\lazzy\Desktop\GitHub\1.txt C:\Users\lazzy\Desktop\GitHub\2.txt C:\Users\lazzy\Desktop\GitHub\3.txt')
    #git.list()
    #git.readme('name')
    #git.status('name')
    #git.issues('namasdfasdfasdadfadfae')
    #git.pullrequests('namasdfasdfasdadfadfae')
    #git.fork("https://github.com/donnemartin/system-design-pridsfmer")
    #git.fork("httpsadfa")
    
    git.close()
