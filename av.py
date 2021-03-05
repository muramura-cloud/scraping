from selenium import webdriver


class Av:
    # ここにAVの設定を書けば良いのでは？
    # 抜きスト、iqoo→.article_content h3 a
    def __init__(self, url):
        self.url = url

    # webブラウザを開く
    def open_browser(self):
        # x. Chrome の起動オプションを設定する
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        # x. ブラウザの新規ウィンドウを開く
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=options.to_capabilities(),
            options=options,
        )

        self.driver = driver

    # AVサイトのトップページから動画の詳細リンクを収集する
    def get_links(self):
        links = []
        for a_tag in self.driver.find_elements_by_css_selector('.article_content h3 a'):
            link = a_tag.get_attribute('href')
            if self.url in link:
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
            good_rate = 0

            # 0除算を防ぐため
            if good > 0 or bad > 0:
                good_rate = round(good / (good + bad), 2)

            # 高評価が10以上かつ高評価率が0.8以上
            if good >= 10 and good_rate >= 0.8:
                contents.append([title, link, good, good_rate])

        self.driver.quit()

        return contents
