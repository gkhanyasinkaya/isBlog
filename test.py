from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import warnings
from ntlk import parserNormal,parserTagged,normalPoint,taggedPoint,totalPoint
from error404 import error404found

warnings.filterwarnings("ignore", category=DeprecationWarning)

driver_path = r"C:/Users/gokli/Desktop/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

#opening data file
file_data = open("output.txt", "r")
dataText = file_data.read()

#link = "https://www.donanimhaber.com/"
#link = "https://www.gittigidiyor.com/"
#link = "https://www.mynet.com/"

#https://www.wix.com/blog/2020/12/types-of-websites/#viewer-d5va4
#https://www.sitebuilderreport.com/inspiration/blog-examples
#https://zyro.com/blog/portfolio-website-examples/


link = "https://www.amazon.com/"
link = "https://www.ebay.com/"
link = "https://www.oliviabosserteducation.com/"
link = "https://www.trendyol.com/"
link = "https://www.seanhalpin.design/"
link = "https://www.donanimhaber.com/"
link = "https://www.johngreenbooks.com/"
link = "https://www.onemag.us/one-online"
link = "https://www.creativeretailawards.com/"
link = "https://www.wikipedia.org/"




driver.get(link)
total = 0
## Link check ##

if "blog" in link:
    print("[+60] Site has 'blog' in URL")
    total += 60

##
if ".tumblr.com" in link:                                         # %83 of the blog sites are from tumblr.com.
    print("[+90] Site made with tumblr.com")                      # ½94 of the all tumblr sites are blog.
    total += 90

if ".blogspot.com" in link:                                       # %80 of the blogspot.com sites are
    print("[+60] Site made with blogger.com")                     # powered by wordpress.com.
    total += 60
##
flagWordPress = True
if ".wordpress.com" in link:
    flagWordPress = False
    print("[+5] Site made with wordpress.com")
    total += 5

if ".wixsite.com" in link:
    print("[+5] Site made with wix.com")
    total += 5

try:
    src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@src,'assets.squarespace.com')]")))
    print("[+5] Site made with squarespace.com")
    total += 5
except:
    pass

## Shopping cart check ##
def shoppingCartCheck():
    try:
        src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@id,'cart')]")))
        print("[-80] Site has Shopping Cart System.")
        return (-80)
    except:
        try:
            src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'shopping-icon')]")))
            print("[-80] Site has Shopping Cart System.")
            return (-80)
        except:
            try:
                src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'basket')]")))
                print("[-80] Site has Shopping Cart System.")
                return (-80)
            except:
                try:
                    src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@aria-label,'shopping')]")))
                    print("[-80] Site has Shopping Cart System.")
                    return (-80)
                except:
                    try:
                        src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'shopping-cart')]")))
                        print("[-80] Site has Shopping Cart System.")
                        return(-80)
                    except:
                        try:
                            src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@data-hook,'cart-icon')]")))
                            print("[-80] Site has Shopping Cart System.")
                            return (-80)
                        except:
                            pass
    return(0)


#### Description Analysis with  ntlk.py

dataListNormal = parserNormal(dataText)
dataListTagged = parserTagged(dataText)
def descAnalysis(dataListNormal,dataListTagged):
    try:
        desc = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//*[@name='description']"))).get_attribute("content")
        p0=0
        if "blog" in desc:
            print("[+60] Site has 'blog' in site's description.")
            p0=60
        inputTextNormal = parserNormal(desc)
        inputTextTagged = parserTagged(desc)
        p1 = normalPoint(inputTextNormal,dataListNormal)
        p2 = taggedPoint(inputTextTagged,dataListTagged)
        pTotal = totalPoint(p1,p2)
        print("[+"+str(pTotal)+"] Site has common words in site's description compare to blog sites.")
        return (pTotal+p0)

    except:
        pass
    return (0)

### Blog posting schema check
def schemaCheck():
    try:
        src_content = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@itemtype,'schema.org/BlogPosting')]")))
        print("[+10] Site has blog posting schema.")
        return (10)
    except:
        pass
    return(0)

## wp-content check
def wpContentCheck(flagWordPress):
    if flagWordPress:
        try:
            href_content = WebDriverWait(driver, 1).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@href,'wp-content')]")))
            print("[+5] Site made with wordpress.com")
            return (5)
        except:
            try:
                src_content = WebDriverWait(driver, 1).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@src,'wp-content')]")))
                print("[+5] Site made with wordpress.com")
                return (5)
            except:
                pass
    return (0)

## Wikipages
def wikiCheck(link):
    if "wiki" in link:
        print("[-60] Site is a wiki page")
        return (-60)
    else:
        try:
            desc = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//*[@name='description']"))).get_attribute("content")
            if "wiki" in desc:
                print("[-60] Site is a wiki page")
                return (-60)
        except:
            linkWiki = link + "wiki"
            if error404found(driver, linkWiki):
                print("[-40] Site has a /wiki page")
                return (-40)
            else:
                pass
    return (0)
## Forums
def forumCheck(link):
    if "forum" in link:
        print("[-40] Site has 'forum' in URL")
        return (-40)
    else:
        if "www" in link:
            linkArray = link.split("https://www.")
            linkAdded = "https://" + "forum." + linkArray[1]
        else:
            linkArray = link.split("https://")
            linkAdded = "https://" + "forum." + linkArray[1]

        if error404found(driver,linkAdded):
            print("[-40] Site has  forum.site.com page")
            return (-40)
        else:
            link = link + "forum"
            if error404found(driver,link):
                print("[-40] Site has  /forum page")
                return (-40)
    return (0)


## /about /blog blog.link.com
def blogCheck(link):
    if "www" in link:
        linkArray = link.split("https://www.")
        linkAdded = "https://"+ "blog." + linkArray[1]
    else:
        linkArray = link.split("https://")
        linkAdded = "https://" + "blog." + linkArray[1]

    if error404found(driver,linkAdded):
        print("[+80] Site has blog.site.com page")
        return (80)
    else:
        linkBlog = link + "blog"
        if error404found(driver,linkBlog):
            print("[+80] Site has /blog page")
            return (80)
        else:
            linkAbout = link + "about"
            if error404found(driver, linkAbout):
                try:
                    src_content = WebDriverWait(driver, 1).until(
                        EC.presence_of_all_elements_located((By.XPATH, "//*[text()='blog']")))
                    print("[+60] Site has blogging references in it's /about page")
                    return (60)
                except:
                    try:
                        src_content = WebDriverWait(driver, 1).until(
                            EC.presence_of_all_elements_located((By.XPATH, "//*[text()='blogging']")))
                        print("[+60] Site has blogging references in it's /about page")
                        return (60)
                    except:
                        pass
    return (0)


## /about charity,event,reward /event /events
def eventCheck(link):
    linkEvent = link + "event"
    if error404found(driver,linkEvent):
        print("[-60] Site has /event page")
        return (-60)
    else:
        linkEvent = linkEvent + "s"
        if error404found(driver,linkEvent):
            print("[-60] Site has /events page")
            return (-60)
    linkAbout = link + "about"
    if error404found(driver, linkAbout):
        try:
            src_content = WebDriverWait(driver, 1).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[text()='annual event']")))
            print("[-60] Site has event planing references in it's /about page")
            return (-60)
        except:
            try:
                src_content = WebDriverWait(driver, 1).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//*[text()='charity']")))
                print("[-30] Site has event planing references in it's /about page")
                return (-30)
            except:
                try:
                    src_content = WebDriverWait(driver, 1).until(
                        EC.presence_of_all_elements_located((By.XPATH, "//*[text()='awards']")))
                    print("[-40] Site has awards & award shows references in it's /about page")
                    return (-40)
                except:
                    pass
    return (0)
## /product /shop /pricing /products
def bussinesCheck(link):
    linkProduct = link + "product"
    if error404found(driver, linkProduct):
        print("[-60] Site has /product page")
        return(-60)
    else:
        linkProduct = linkProduct + "s"
        if error404found(driver, linkProduct):
            print("[-60] Site has /products page")
            return (-60)
        else:
            linkShop = link + "shop"
            if error404found(driver, linkShop):
                print("[-40] Site has /shop page")
                return (-40)
            else:
                linkPricing = link + "pricing"
                if error404found(driver, linkPricing):
                    print("[-60] Site has /pricing page")
                    return (-60)
    return (0)


total = ( total
         +shoppingCartCheck()
         +descAnalysis(dataListNormal,dataListTagged)
         +schemaCheck()
         +wpContentCheck(flagWordPress)
         +wikiCheck(link)
         +blogCheck(link)
         +eventCheck(link)
         +bussinesCheck(link)
         +forumCheck(link))


print("Total Point:  "+str(total))
#errorController = bussinesCheck(link) + eventCheck(link) + blogCheck(link) + forumCheck(link)
#if errorController == -140:
#    "This Website may not be truly checked!"

if total<-50:
    print("This Website definitly not a blog.")
elif total<0 and total>=-50:
    print("This Website most likely not a blog.")
elif total>=0 and total < 25:
    print("This Website either doesn't have enough blog features or its main focus is not blog")
elif total >= 25 and total < 50:
    print("This Website most likely a blog.")
elif total>=50:
    print("This Website definitly a blog.")

