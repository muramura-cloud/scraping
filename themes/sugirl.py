from av import Av
import sys


class Sugirl(Av):
    def get_links(self, url=''):
        if url != '':
            self.driver.get(url)

        links = super().get_links()
        links = self.extract_links(links, 'video')

        return links

    # コンテンツを取得
    def get_contents(self):
        # 動画のリンクを取得
        links = self.get_links()

        # 質の高い動画を抽出
        contents = super().get_contents(links)

        # ブラウザを閉じる
        self.driver.quit()

        return contents
