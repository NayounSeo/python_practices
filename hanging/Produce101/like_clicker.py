'''
ASSUMPTION : 네이버 로그인☆이 되어있다 
GOAL : 
최민기 직캠 영상 페이지에 접속 후
- 전체 댓글을 누르고
- 1page 댓글에서 좋아요를 눌렀는지 아닌지 판단한 후
- 누르지 않았다면 누른다

처음은 뷰숲 이번은 셀레늄이니 다음은 스크래피 
'''
from selenium import webdriver
import time

url = "http://tv.naver.com/v/1747159/list/132312"

def main():
  binry = "C:\chromedriver_2.29.exe"
  chrome_driver = webdriver.Chrome(binry)
  chrome_driver.get(url)

  # TODO : 로그인... 로그인은 중요한 거였어..
  # 네이버 로그인 예제를 갖다 씁시다... 한글 있었어..

  time.sleep(3) # TH Yedarm

  # chrome_driver.find_element_by_id("id")
  # chrome_driver.find_elements_by_class_name("id")
  # chrome_driver.find_element_by_xpath("xpath")
  # chrome_driver.find_elements_by_css_selector("")
  see_all = chrome_driver.find_element_by_xpath(
                    '//*[@id="cbox_module"]/div/div[5]/div[1]/div/ul/li[2]/a')
  see_all.click() # 전체 댓글 클릭

  time.sleep(3)

  # 1page 댓글들
  comments = chrome_driver.find_elements_by_css_selector(
      '#cbox_module > div > div.u_cbox_content_wrap > ul > li.u_cbox_comment')
  for c in comments:
    c.find_elements_by_css_selector('div.u_cbox_comment_box > div > div.u_cbox_tool > div > a.u_cbox_btn_recomm')
    print(c)
    c.click()

  # chrome_driver.quit()

if __name__ == "__main__":
  main()