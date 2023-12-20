from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Tarayıcımız "Microsoft Edge"
browser =webdriver.Edge()
browser.maximize_window()
# URL adresimiz
browser.get("https://www.trendyol.com/")
time.sleep(2)

# İlk çıkan reklamı kapatır.
reklam_kapat = browser.find_element(By.XPATH,"//*[@id='gender-popup-modal']/div/div/div[2]/div/div[2]/a/span[1]/img")
reklam_kapat.click()

# Arama yeri
arama_input =browser.find_element(By.XPATH,"//*[@id='sfx-discovery-search-suggestions']/div/div[1]/input")
input = arama_input.send_keys("ekran karti")
time.sleep(1)

ekran_karti = browser.find_element(By.XPATH,"//*[@id='sfx-discovery-search-suggestions']/div/div[2]/div/div/a[1]")
ekran_karti.click()

# Markalar
asus = browser.find_element(By.XPATH,"//*[@id='sticky-aggregations']/div/div[2]/div[3]/div/div/div[1]/div/a/div[1]")
asus.click()
time.sleep(1)

msi = browser.find_element(By.XPATH,"//*[@id='sticky-aggregations']/div/div[2]/div[3]/div/div/div[2]/div/a/div[1]")
msi.click()
time.sleep(1)

# Sepete ekleme
items = "//*[@id='search-app']/div/div[1]/div[2]/div[4]/div[1]/div/div[{}]/div[1]/div[2]/button/div[1]"

# Kaç tane ürün istiyorsak "16" yerine yazıyoruz
for i in range(1, 16):  
    kart = items.format(i)
    sepet = browser.find_element(By.XPATH, kart)
    sepet.click()
    
# Yukarı kaydırma
actions = ActionChains(browser)
actions.send_keys(Keys.HOME).perform()

# Sepet Bölümü
sepete_git = browser.find_element(By.XPATH,"//*[@id='account-navigation-container']/div/div[2]/a/p")
time.sleep(1)
sepete_git.click()

sepet_title = []
sepet_fiyat = []
sayac = 1

# Ürün Adı
sepet_item = browser.find_elements(By.CLASS_NAME,"pb-item")
for i in sepet_item:
    sepet_title.append(i.text)

# Ürün Fiyatı
sepet_item_fiyat = browser.find_elements(By.CLASS_NAME,"pb-basket-item-price")
for i in sepet_item_fiyat:
    sepet_fiyat.append(i.text)

# Text dosyasına yazma
with open("Trendyol_sepet.txt", "w", encoding="UTF-8") as file:
    for title, fiyat in zip(sepet_title, sepet_fiyat):
        file.write(str(sayac) + "\n" + title + "\n")
        file.write(fiyat + "\n")
        file.write("************************************\n")
        sayac += 1

time.sleep(5)
browser.quit()