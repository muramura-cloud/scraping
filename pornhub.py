from googletrans.models import Translated
from av import Av
from selenium.webdriver.common.by import By
from googletrans import Translator

translator = Translator()


class Pornhub(Av):
    def get_translated_text(self, text):
        try:
            translated = translator.translate(text, dest='ja').text
        except Exception as e:
            print('翻訳に失敗しました。')
            return text

        return translated

    # 特定のurlが指定されていたら、そこのページのリンクを収集する
    def get_links(self, url=''):
        if url != '':
            self.driver.get(url)

        # 特定のurlが指定が指定された場合、そこのページの要素に'pcVideoListItem'というセレクタが必ず存在するとは言えないつまりエラーが起こる可能性があります。
        items = self.driver.find_elements_by_class_name('pcVideoListItem')
        links = []
        for item in items:
            a_tag = item.find_element(By.TAG_NAME, 'a')
            img_tag = item.find_element(By.TAG_NAME, 'img')
            links.append({
                'page_link': a_tag.get_attribute('href'),
                'im_link': img_tag.get_attribute('src')
            })

        return links

    # Avコンテンツを取得
    def get_contents(self):
        # 急上昇のページのリンクを取得
        soaring_movie_link = self.driver.find_element_by_css_selector(
            'h1 a').get_attribute('href')
        # 動画のリンクを収集
        links = self.get_links(soaring_movie_link)
        print(links)

        # 質の高い動画を抽出
        contents = super().get_contents(links)

        # ブラウザを閉じる
        self.driver.quit()

        return contents
