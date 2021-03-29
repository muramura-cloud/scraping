from av import Av


class Iqoo(Av):
    # サイトのトップページから動画の詳細リンクを収集する
    def get_links(self, url=''):
        if url != '':
            self.driver.get(url)

        links = []
        for article in self.driver.find_elements_by_css_selector('article'):
            page_link = article.find_element_by_css_selector(
                'a').get_attribute('href')
            im_link = article.find_element_by_css_selector(
                'img').get_attribute('src')
            if self.url in page_link:
                links.append({
                    "page_link": page_link,
                    "im_link": im_link,
                })

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
