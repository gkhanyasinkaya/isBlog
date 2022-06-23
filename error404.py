from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)


#driver_path = r"C:/Users/gokli/Desktop/chromedriver.exe"
#driver = webdriver.Chrome(executable_path=driver_path)

#link = "https://stackoverflow.com/"
#driver.get(link+"blog333")

def error404found(driver,link):
    try:
        driver.get(link)
        try:
            src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@id,'offline')]")))
        except:
            try:
                src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'error')]")))
            except:
                try:
                    src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'not-found')]")))
                except:
                    try:
                        src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'error-404')]")))
                    except:
                        try:
                            src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'error-contents')]")))
                        except:
                            try:
                                src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'400-page')]")))
                            except:
                                try:
                                    src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'error-400')]")))
                                except:
                                    try:
                                        src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH,"//*[contains(@class,'404')]")))
                                    except:
                                        try:
                                            src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH,"//*[text()='Page not found']")))
                                            #print("AAAAAAAAAAAA")
                                        except:
                                            try:
                                                src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[text()='page not found']")))
                                            except:
                                                try:
                                                    src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[text()='We couldn't find']")))
                                                except:
                                                    try:
                                                        src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[text()='We could not find']")))
                                                    except:
                                                        try:
                                                            src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'404-page')]")))
                                                        except:
                                                            try:
                                                                src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[text()='Not Found']")))
                                                            except:
                                                                try:
                                                                    src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'404img')]")))
                                                                except:
                                                                    try:
                                                                        src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[text()='404']")))
                                                                    except:
                                                                        try:
                                                                            src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH,  "//*[contains(@alt,'Sorry')]")))
                                                                        except:
                                                                            return (True)
    except:
        "This site is offline!"
    return (False)

#print(error404found(driver,link+"blog14545"))