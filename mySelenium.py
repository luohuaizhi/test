# -*- encoding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

UNAME = "luohuaizhi"
PASSWORD = "******"

def main():
    """
    1.登录到github
    2.打开个人中心
    3.获取所有工程的git仓库
    """
    driver = webdriver.Chrome()
    # TODO 1
    driver.get("https://github.com/login")
    assert "GitHub" in driver.title
    u_ele = driver.find_element_by_name("login")
    u_ele.send_keys(UNAME)
    # e_ele = driver.find_element_by_name("user[email]")
    # e_ele.send_keys("luohuaizhi1484@163.com")
    p_ele = driver.find_element_by_name("password")
    p_ele.send_keys(PASSWORD)
    login_ele = driver.find_element_by_css_selector("input[type=submit]")
    login_ele.click()
    # TODO 2
    driver.find_element_by_css_selector("img[alt='@"+UNAME+"']").click()
    # 点击下拉菜单
    driver.find_element_by_link_text("Your profile").click()
    # 点击个人信息
    # TODO 3
    repo_list = driver.find_elements_by_class_name("pinned-repo-item")
    for rep in repo_list:
        print rep.find_element_by_tag_name("a").get_attribute("href")
    print driver.page_source


if __name__ == '__main__':
    main()