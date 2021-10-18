import requests
from bs4 import BeautifulSoup
import re
import time

import os
import selenium
from selenium import webdriver
import time
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException

PATH= 'C:\webdrivers\chromedriver.exe'
#ChromeDriverManager().install()
driver= webdriver.Chrome(ChromeDriverManager().install())
inp=int(input('Please enter week number: '))
print('fetching results...')

url='https://overwatchleague.com/en-us/schedule?stage=regular_season&week=' + str(inp) + '/'
driver.get(url)
print(driver.title)
# print(driver.body)
# element= driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[3]/div[3]/div[1]/div[2]/div[2]/div/section/div[3]/div[1]/div/div[2]/div[1]/p')
# elements1=driver.find_elements_by_xpath('//*[@id="__next"]/div/div/div[3]/div[3]/div[1]/div[2]/div[2]/div/section/div[3]/div[1]/div/div[2]')
#both work using XPATH !!

# for element in elements1:
#     print(element.text)

containers=driver.find_elements_by_class_name('match-cardstyles__Middle-sc-1rgscfz-6')
for i,container in enumerate(containers):
    # print(container.text.strip())
    # team1= container.find_element_by_xpath('//*[@id="__next"]/div/div/div[3]/div[3]/div[1]/div[2]/div[2]/div/section/div[3]/div[1]/div/div[2]/div[1]/p')
    # score1=container.find_element_by_xpath('//*[@id="__next"]/div/div/div[3]/div[3]/div[1]/div[2]/div[2]/div/section/div[3]/div[1]/div/div[2]/div[2]/div/p[1]')
    # team2=container.find_element_by_xpath('//*[@id="__next"]/div/div/div[3]/div[3]/div[1]/div[2]/div[2]/div/section/div[3]/div[1]/div/div[2]').text[3]
    # score2=container.find_element_by_xpath('//*[@id="__next"]/div/div/div[3]/div[3]/div[1]/div[2]/div[2]/div/section/div[3]/div[1]/div/div[2]').text[4]
    # xpath is TOO specific. best is to use class!
    team1= container.find_element_by_class_name('match-cardstyles__MiddleText-sc-1rgscfz-12')
    score1= container.find_element_by_class_name('match-cardstyles__ScoreText-sc-1rgscfz-23')
    if not team1:
        break
    print(team1.text.replace(' ', ''))
    # print(score1.text.replace(' ','').strip())
# <div class="match-cardstyles__Middle-sc-1rgscfz-6 GRdHe"><div class="match-cardstyles__FlexCentered-sc-1rgscfz-13 match-cardstyles__ContainerTeam-sc-1rgscfz-24 kAeBio"><p class="match-cardstyles__MiddleText-sc-1rgscfz-12 hueupq">DAL</p><div class="match-cardstyles__Logo-sc-1rgscfz-3 bHHCvO imagestyles__ImageStyled-sc-1a2dybj-0 jXQkVy" role="img" src="https://bnetcmsus-a.akamaihd.net/cms/page_media/NO44N7DDJAPF1508792362936.png"></div></div><div class="match-cardstyles__ContainerScore-sc-1rgscfz-16 dlFDqa"><div class="match-cardstyles__ScoreTextContainer-sc-1rgscfz-17 vutet"><p color="#333333" font-weight="bold" class="match-cardstyles__ScoreText-sc-1rgscfz-23 gOtrSB">3</p><p color="#333333" class="match-cardstyles__ScoreText-sc-1rgscfz-23 fKHwTE">-</p><p color="#333333" font-weight="" class="match-cardstyles__ScoreText-sc-1rgscfz-23 jRejaZ">1</p></div></div><div class="match-cardstyles__FlexCentered-sc-1rgscfz-13 match-cardstyles__ContainerTeam-sc-1rgscfz-24 gdAfxi"><div class="match-cardstyles__Logo-sc-1rgscfz-3 bHHCvO imagestyles__ImageStyled-sc-1a2dybj-0 hjdSjK" role="img" src="https://bnetcmsus-a.akamaihd.net/cms/page_media/3AEMOZZL76PF1508792362892.PNG"></div><p class="match-cardstyles__MiddleText-sc-1rgscfz-12 cLYgmY">GLA</p></div></div>
# <div class="match-cardstyles__Middle-sc-1rgscfz-6 GRdHe"><div class="match-cardstyles__FlexCentered-sc-1rgscfz-13 match-cardstyles__ContainerTeam-sc-1rgscfz-24 kAeBio"><p class="match-cardstyles__MiddleText-sc-1rgscfz-12 hueupq">HOU</p><div class="match-cardstyles__Logo-sc-1rgscfz-3 bHHCvO imagestyles__ImageStyled-sc-1a2dybj-0 hMfnCU" role="img" src="https://bnetcmsus-a.akamaihd.net/cms/gallery/2YF5VLIMGZVA1546557680222.png"></div></div><div class="match-cardstyles__ContainerScore-sc-1rgscfz-16 dlFDqa"><div class="match-cardstyles__ScoreTextContainer-sc-1rgscfz-17 vutet"><p color="#333333" font-weight="bold" class="match-cardstyles__ScoreText-sc-1rgscfz-23 gOtrSB">3</p><p color="#333333" class="match-cardstyles__ScoreText-sc-1rgscfz-23 fKHwTE">-</p><p color="#333333" font-weight="" class="match-cardstyles__ScoreText-sc-1rgscfz-23 jRejaZ">2</p></div></div><div class="match-cardstyles__FlexCentered-sc-1rgscfz-13 match-cardstyles__ContainerTeam-sc-1rgscfz-24 gdAfxi"><div class="match-cardstyles__Logo-sc-1rgscfz-3 bHHCvO imagestyles__ImageStyled-sc-1a2dybj-0 jXQkVy" role="img" src="https://bnetcmsus-a.akamaihd.net/cms/page_media/NO44N7DDJAPF1508792362936.png"></div><p class="match-cardstyles__MiddleText-sc-1rgscfz-12 cLYgmY">DAL</p></div></div>

    # <p color="#333333" font-weight="bold" class="match-cardstyles__ScoreText-sc-1rgscfz-23 gOtrSB">3</p>
    # <p color="#333333" font-weight="" class="match-cardstyles__ScoreText-sc-1rgscfz-23 jRejaZ">1</p>
    # <p class="match-cardstyles__MiddleText-sc-1rgscfz-12 hueupq">SEO</p>
    # <p class="match-cardstyles__MiddleText-sc-1rgscfz-12 hueupq">GLA</p>

# elements2=driver.find_elements_by_xpath('//p[contains(@class, "match-cardstyles__Middle-sc")]')
# print(elements2)

# elements3=driver.find_elements_by_class_name('match-cardstyles__MiddleText-sc-1rgscfz-12 cLYgmY')
# for element in elements3:
#     print(element.text)

# print('ELEMENTS HERE: ', elements1)

# driver.execute_script("(arguments[0]).click;",element)

# //*[@id="__next"]/div/div/div[3]/div[3]/div[1]/div[2]/div[2]/div/section/div[3]/div[1]/div/div[2]

time.sleep(10)
driver.quit()


# <div class="match-cardstyles__Middle-sc-1rgscfz-6 GRdHe"><div class="match-cardstyles__FlexCentered-sc-1rgscfz-13 match-cardstyles__ContainerTeam-sc-1rgscfz-24 kAeBio"><p class="match-cardstyles__MiddleText-sc-1rgscfz-12 hueupq">GLA</p><div class="match-cardstyles__Logo-sc-1rgscfz-3 bHHCvO imagestyles__ImageStyled-sc-1a2dybj-0 hjdSjK" role="img" src="https://bnetcmsus-a.akamaihd.net/cms/page_media/3AEMOZZL76PF1508792362892.PNG"></div></div><div class="match-cardstyles__ContainerScore-sc-1rgscfz-16 dlFDqa"><div class="match-cardstyles__ScoreTextContainer-sc-1rgscfz-17 vutet"><p color="#333333" font-weight="" class="match-cardstyles__ScoreText-sc-1rgscfz-23 jRejaZ">1</p><p color="#333333" class="match-cardstyles__ScoreText-sc-1rgscfz-23 fKHwTE">-</p><p color="#333333" font-weight="bold" class="match-cardstyles__ScoreText-sc-1rgscfz-23 gOtrSB">3</p></div></div><div class="match-cardstyles__FlexCentered-sc-1rgscfz-13 match-cardstyles__ContainerTeam-sc-1rgscfz-24 gdAfxi"><div class="match-cardstyles__Logo-sc-1rgscfz-3 bHHCvO imagestyles__ImageStyled-sc-1a2dybj-0 gjWKci" role="img" src="https://images.blz-contentstack.com/v3/assets/blt321317473c90505c/blte679a761205b5d5f/5e1763e38691147ecf07e0f6/OWL_SFShock_Icon_1C_SILVER-01.png"></div><p class="match-cardstyles__MiddleText-sc-1rgscfz-12 cLYgmY">SFS</p></div></div>
# r=requests.get(url).text
# # r.raise_for_status()
# soup=BeautifulSoup(r, 'lxml')
# print(soup.title)

# # attrs= {'meta content'}
# tests=soup.find_all('div', class_='indexstyles__PageContainer-pu1n5t-1 cvzdyC')
# print(tests)
# /html/body/div[1]/div


#refers to left side
# /html/body/div[1]/div/div/div[3]/div[3]/div[1]/div[2]/div[2]/div/section/div[3]/div[1]/div/div[2]/div[1]/p
# <p class="match-cardstyles__MiddleText-sc-1rgscfz-12 hueupq">HOU</p>
# <p class="match-cardstyles__MiddleText-sc-1rgscfz-12 hueupq">GLA</p>

#refers to right side
# <p class="match-cardstyles__MiddleText-sc-1rgscfz-12 cLYgmY">GZC</p>
# <p class="match-cardstyles__MiddleText-sc-1rgscfz-12 cLYgmY">SHD</p>

#refers to center box with team and score info
# <div class="match-cardstyles__Middle-sc-1rgscfz-6 GRdHe"><div class="match-cardstyles__FlexCentered-sc-1rgscfz-13 match-cardstyles__ContainerTeam-sc-1rgscfz-24 kAeBio"><p class="match-cardstyles__MiddleText-sc-1rgscfz-12 hueupq">LDN</p><div class="match-cardstyles__Logo-sc-1rgscfz-3 bHHCvO imagestyles__ImageStyled-sc-1a2dybj-0 dbBiXd" role="img" src="https://bnetcmsus-a.akamaihd.net/cms/page_media/NW461AQIYQMK1508792363133.png"></div></div><div class="match-cardstyles__ContainerScore-sc-1rgscfz-16 dlFDqa"><div class="match-cardstyles__ScoreTextContainer-sc-1rgscfz-17 vutet"><p color="#333333" font-weight="" class="match-cardstyles__ScoreText-sc-1rgscfz-23 jRejaZ">0</p><p color="#333333" class="match-cardstyles__ScoreText-sc-1rgscfz-23 fKHwTE">-</p><p color="#333333" font-weight="bold" class="match-cardstyles__ScoreText-sc-1rgscfz-23 gOtrSB">3</p></div></div><div class="match-cardstyles__FlexCentered-sc-1rgscfz-13 match-cardstyles__ContainerTeam-sc-1rgscfz-24 gdAfxi"><div class="match-cardstyles__Logo-sc-1rgscfz-3 bHHCvO imagestyles__ImageStyled-sc-1a2dybj-0 jXQkVy" role="img" src="https://bnetcmsus-a.akamaihd.net/cms/page_media/NO44N7DDJAPF1508792362936.png"></div><p class="match-cardstyles__MiddleText-sc-1rgscfz-12 cLYgmY">DAL</p></div></div>