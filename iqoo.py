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
    def get_contents(self, min_good_count='', min_good_rate='', min_view_count=''):
        # 動画ののクオリティの基準を再設定する。
        self.set_movie_evaluation_attr(
            min_good_count, min_good_rate, min_view_count)

        links = self.get_links()

        contents = []
        for link in links:
            page_link = link['page_link']
            print(page_link)
            self.driver.get(page_link)

            try:
                im_link = self.get_im_link(link)
                title = self.driver.find_element_by_css_selector('h1').text
                good = int(self.driver.find_element_by_id('btn_good').text)
                bad = int(self.driver.find_element_by_id('btn_bad').text)
                tags = [tag.text for tag in self.driver.find_elements_by_css_selector(
                    'article footer li a')]
                good_rate = self.get_good_rate(good, bad)

                # 高評価が10以上かつ高評価率が0.8以上
                if self.validation_content(good_count=good, good_rate=good_rate):
                    contents.append(
                        [im_link, title, page_link, good, '{:.0%}'.format(good_rate), '・'.join(tags)])
            except Exception as e:
                print('要素の取得に失敗')
                print(str(e))
                continue

        self.driver.quit()

        return contents
