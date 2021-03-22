from av import Av
from selenium.webdriver.common.by import By


class Nukisuto(Av):
    # AVサイトのトップページから動画の詳細リンクを収集する
    def get_links(self):
        # linksをオブジェクトにすれば良いかも
        links = {
            'page_link': 'url',
            'im_link': 'url'}
        links = []
        # 「article」で取得してきた方が良いかも。サムネイルの画像も同時に取得できるから
        for a_tag in self.driver.find_elements_by_css_selector('.article_content h3 a'):
            link = a_tag.get_attribute('href')
            if self.url in link:
                links.append(link)

        return links

    def get_contents(self, min_good_count='', min_good_rate='', min_view_count=''):
        self.set_movie_evaluation_attr(
            min_good_count, min_good_rate, min_view_count)

        links = self.get_links()

        contents = []
        for link in links:
            print(link)
            self.driver.get(link)

            try:
                title = self.driver.find_element_by_css_selector('h1').text
                good = int(self.driver.find_element_by_id('btn_good').text)
                bad = int(self.driver.find_element_by_id('btn_bad').text)
                tags = [tag.text for tag in self.driver.find_elements_by_css_selector(
                    'article footer li a')]
                good_rate = self.get_good_rate(good, bad)

                # 高評価が10以上かつ高評価率が0.8以上
                if self.validation_content(good_count=good, good_rate=good_rate):
                    contents.append(
                        [title, link, good, '{:.0%}'.format(good_rate), '・'.join(tags)])
            except Exception as e:
                print('要素の取得に失敗')
                print(str(e))
                continue

        self.driver.quit()

        return contents
