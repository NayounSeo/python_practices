'''
GOAL : 
최민기 직캠 영상 페이지에 접속 후
- 전체 댓글을 누르고
- 1page 댓글에서 좋아요를 눌렀는지 아닌지 판단한 후
- 누르지 않았다면 누른다

처음은 뷰숲 이번은 셀레늄이니 다음은 스크래피 
'''
from selenium import webdriver
import time

url_login = "https://nid.naver.com/nidlogin.login"
url_hit = "http://tv.naver.com/v/1747159/list/132312"

def main():
  binry = "C:\chromedriver_2.29.exe"
  chrome_driver = webdriver.Chrome(binry)
  chrome_driver.get(url_login)

  # Naver Login
  iD = chrome_driver.find_element_by_xpath('//*[@id="id"]')
  # iD.send_keys('로그인할 아이디')
  psswd = chrome_driver.find_element_by_xpath('//*[@id="pw"]')
  # psswd.send_keys('로그인 비밀번호')
  login = chrome_driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

  # 댓글 누를 페이지에 접속
  chrome_driver.get(url_hit)
  time.sleep(3) # 인터넷 접속 환경에따라 변경

  see_all = chrome_driver.find_element_by_xpath(
                    '//*[@id="cbox_module"]/div/div[5]/div[1]/div/ul/li[2]/a')
  see_all.click() # 전체 댓글 클릭

  time.sleep(1)

  # 1page 댓글들
  comments = chrome_driver.find_elements_by_css_selector(
      '#cbox_module > div > div.u_cbox_content_wrap > ul > li.u_cbox_comment')

  # time.sleep(1)
  # 팝업 비디오는 꺼주기
  popped_video = chrome_driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[1]/div[1]/a').click()

  for c in comments:
    like = c.find_elements_by_css_selector('div.u_cbox_comment_box > div > div.u_cbox_tool > div > a.u_cbox_btn_recomm')
    if ("u_cbox_btn_recomm_on" not in like[0].get_attribute("class")):
      like[0].click()
      time.sleep(1) # 너무 빨라서 안눌리더라..^^

  chrome_driver.quit()

if __name__ == "__main__":
  main()