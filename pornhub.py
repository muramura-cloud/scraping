from googletrans.models import Translated
from av import Av
from selenium.webdriver.common.by import By
from googletrans import Translator

translator = Translator()


class Pornhub(Av):
    def translated_text(self, text):
        try:
            translated = translator.translate(text, dest='ja').text
        except Exception as e:
            return text

        return translated

    # 特定のurlが指定されていたら、そこのページのリンクを収集する
    def get_links(self, url=''):
        if url != '':
            self.driver.get(url)

        items = self.driver.find_elements_by_class_name('pcVideoListItem')
        links = []
        for item in items:
            a_tag = item.find_element(By.TAG_NAME, 'a')
            link = a_tag.get_attribute('href')
            links.append(link)

        return links

    # Avコンテンツを取得
    def get_contents(self, min_good_count='', min_good_rate='', min_view_count=''):
        # 取得する動画の評価基準を調整
        self.set_movie_evaluation_attr(
            min_good_count, min_good_rate, min_view_count)

        # 急上昇のページのリンクを取得
        soaring_movie_link = self.driver.find_element_by_css_selector(
            'h1 a').get_attribute('href')

        links = self.get_links(soaring_movie_link)

        contents = []
        for link in links:
            print(link)
            self.driver.get(link)

            title = self.driver.find_element_by_css_selector('h1').text
            # 「Pornhub」の場合は英語のタイトルが多いからグーグル翻訳で日本語にする
            title = self.translated_text(title)
            good = int(self.driver.find_element_by_class_name(
                'votesUp').get_attribute('data-rating'))
            bad = int(self.driver.find_element_by_class_name(
                'votesDown').get_attribute('data-rating'))
            tags = [tag.text for tag in self.driver.find_elements_by_class_name(
                'categoriesWrapper')]
            good_rate = self.get_good_rate(good, bad)

            # 高評価が10以上かつ高評価率が0.8以上
            if self.validation_content(good_count=good, good_rate=good_rate):
                contents.append(
                    [title, link, good, '{:.0%}'.format(good_rate), '・'.join(tags)])

        self.driver.quit()

        return contents
