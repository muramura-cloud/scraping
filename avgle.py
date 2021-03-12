from av import Av
from selenium.webdriver.common.by import By

# 「Avgle」っていうサイトめちゃくちゃ重たい。あまり使わない方が良いかも
class Avgle(Av):

    def get_links(self):
        links = []

        elements = avgle.driver.find_elements_by_xpath(
            '//*[@id="wrapper"]/div[1]/div[8]/div/div[1]/div')
        for element in elements:
            a_tag = element.find_element(By.TAG_NAME, 'a')
            link = a_tag.get_attribute('href')
            links.append(link)

        return links

    # Avコンテンツを取得
    def get_contents(self):
        self.open_browser()

        self.driver.get(self.url)

        links = self.get_links()

        contents = []
        for link in links:
            print(link)
            self.driver.get(link)

            title = self.driver.find_element_by_css_selector('h1').text
            good = int(self.driver.find_element_by_id('btn_good').text)
            bad = int(self.driver.find_element_by_id('btn_bad').text)
            tags = [tag.text for tag in self.driver.find_elements_by_css_selector(
                'article footer li a')]
            good_rate = self.get_good_rate(good, bad)

            # 高評価が10以上かつ高評価率が0.8以上
            if good >= self.like_count and good_rate >= self.like_rate:
                contents.append(
                    [title, link, good, '{:.0%}'.format(good_rate), '・'.join(tags)])

        self.driver.quit()

        return contents
