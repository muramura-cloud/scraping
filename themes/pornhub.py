from googletrans.models import Translated
from av import Av
from selenium.webdriver.common.by import By
from googletrans import Translator
import sys

translator = Translator()


class Pornhub(Av):
    def get_translated_text(self, text):
        try:
            translated = translator.translate(text, dest='ja').text
        except Exception as e:
            print('翻訳に失敗しました。')
            return text

        return translated

    def translate_need_item_in_contents(self, item_name, contents):
        if (item_name in self.theme['items']['need_items']):
            for index, content in enumerate(contents):
                contents[index][item_name] = self.get_translated_text(
                    content[item_name])

        return contents

    def get_links(self, url=''):
        if url != '':
            self.driver.get(url)

        links = super().get_links()
        links = self.extract_links(links, 'view_video')

        return links

    def get_contents(self):
        # 急上昇のページのリンクを取得
        soaring_movie_link = self.driver.find_element_by_css_selector(
            'h1 a').get_attribute('href')
        # 動画のリンクを収集
        links = self.get_links(soaring_movie_link)

        # 質の高い動画を抽出
        contents = super().get_contents(links)

        # 指定したneed_itemを日本語に翻訳する。
        contents = self.translate_need_item_in_contents('title', contents)

        # ブラウザを閉じる
        self.driver.quit()

        return contents
