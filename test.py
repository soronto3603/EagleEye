def find_by_re(pattern,text):
    import re

    r=re.compile(pattern)
    results=r.findall(text)
    return results
class EagleEye:
    target_url="http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu4"
    target_area="EagleEye"

    def __init__(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys

        self.driver = webdriver.Firefox()

    def __del__(self):
        self.driver.close()

    def get_target(self,url=target_url,area=target_area):
        self.target_url=url
        self.target_area=area

    def debug_show_value(self):
        print(self.target_url,self.target_area)

    def get_target_source(self):
        self.driver.get(self.target_url)
        return self.driver.find_element_by_tag_name('html').get_attribute('innerHTML')


a=Eagle Eye()
a.debug_show_value()
html_source=a.get_target_source()

print(find_by_re('<div',html_source))
