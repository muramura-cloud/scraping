from av import Av


class Iqoo(Av):
    # AVサイトのトップページから動画の詳細リンクを収集する
    def get_links(self):
        links = []
        for a_tag in self.driver.find_elements_by_css_selector('.article_content h3 a'):
            link = a_tag.get_attribute('href')
            if self.url in link:
                links.append(link)

        return links

    # 高評価率を求める
    def get_good_rate(good, bad):
        good_rate = 0
        # 0除算を防ぐため
        if good > 0 or bad > 0:
            good_rate = round(good / (good + bad), 2)

        return good_rate

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
