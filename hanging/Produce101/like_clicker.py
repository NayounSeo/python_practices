'''
토끼단 화이팅

GOAL : 
최민기 직캠 영상 페이지에 접속 후
- 연속 재생 해제 / 전체 댓글을 누르고 / 팝업 플레이어 끄기
- 댓글에서 좋아요 버튼 상태 체크 후 클릭해주는 코드
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
  iD.send_keys('id')
  psswd = chrome_driver.find_element_by_xpath('//*[@id="pw"]')
  psswd.send_keys('password')
  login = chrome_driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

  # 댓글 누를 페이지에 접속
  chrome_driver.get(url_hit)
  time.sleep(4) # 인터넷 접속 환경에따라 변경

  # 연속 재생 끄기
  conti_player = chrome_driver.find_element_by_xpath('//*[@id="playlistArea"]/div[1]/div/div/a')
  conti_player.click(); conti_player.click()

  see_all = chrome_driver.find_element_by_xpath(
                    '//*[@id="cbox_module"]/div/div[5]/div[1]/div/ul/li[2]/a')
  see_all.click() # 전체 댓글 클릭

  time.sleep(1)
  # 팝업 비디오는 꺼주기
  popped_video = chrome_driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[1]/div[1]/a').click()

  page_no = 1
  a_tag_no = 3
  while (True): # 돌리고 싶은 페이지 양만큼 돌도록 수정. page_no < 100 처럼
    time.sleep(1)

    # page 댓글들
    comments = chrome_driver.find_elements_by_css_selector(
      '#cbox_module > div > div.u_cbox_content_wrap > ul > li.u_cbox_comment')

    for c in comments:
      # TODO : 닉네임을 이용해서 자신의 댓글은 패스하도록 하자
      try:
        like = c.find_elements_by_css_selector('div.u_cbox_comment_box > div > div.u_cbox_tool > div > a.u_cbox_btn_recomm')
      except:  # 경고창이 뜨는 경우
        time.sleep(1)
        alert = chrome_driver.switch_to_alert().accept()
        time.sleep(1.5)
        continue
      else:
        if ("u_cbox_btn_recomm_on" not in like[0].get_attribute("class")):
          try:
            like[0].click()
            time.sleep(1)
          except:
            continue

    if (a_tag_no > 7):
      a_tag_no = 3
    next_view = chrome_driver.find_element_by_xpath('//*[@id="cbox_module"]/div/div[7]/div/a[' + str(a_tag_no) + ']').click()

    a_tag_no += 1
    page_no += 1

  chrome_driver.quit()

if __name__ == "__main__":
  main()