from contextlib import contextmanager
from av import Av
from selenium.webdriver.common.by import By
import sys


class Nukisuto(Av):
    # 抽出したリンクでベースページと関係ないものは削除
    def extract_links(self, links):
        del_indexes = []
        for index, link in enumerate(links):
            if (self.theme['base_url'] not in link['page_link']):
                del_indexes.append(index)
        del links[del_indexes[0]:del_indexes[-1]+1]

        return links

    def get_links(self, url=''):
        if url != '':
            self.driver.get(url)

        links = super().get_links()
        links = self.extract_links(links)

        return links

    def get_contents(self):

        # 動画のリンクを取得
        links = self.get_links()

        # 質の高い動画を抽出
        contents = super().get_contents(links)

        # ブラウザを閉じる
        self.driver.quit()

        return contents
