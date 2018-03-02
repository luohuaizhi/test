# -*- encoding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

UNAME = "luohuaizhi"
PASSWORD = "*****"

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
    # TODO 3
    print driver.page_source


if __name__ == '__main__':
    main()