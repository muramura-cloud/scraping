from selenium import webdriver


class Av:
    def __init__(self, url):
        self.url = url
        self.min_good_count = 10
        self.min_good_rate = 0.8
        self.min_view_count = 5000

        # インスタンス化したと同時にブラウザを開き、ベースページへと遷移する
        self.open_browser()
        self.driver.get(self.url)

    # webブラウザを開く
    def open_browser(self):
        # Chromeの起動オプションを設定する
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        # ブラウザの新規ウィンドウを開く
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=options.to_capabilities(),
            options=options,
        )

        self.driver = driver

    def get_good_rate(self, good, bad):
        good_rate = 0
        # 0除算を防ぐため
        if good > 0 or bad > 0:
            good_rate = round(good / (good + bad), 2)

        return good_rate

    def set_min_good_count(self, min_good_count):
        if isinstance(min_good_count, int):
            self.min_good_count = min_good_count

    def set_min_good_rate(self, min_good_rate):
        if isinstance(min_good_rate, int) or isinstance(min_good_rate, float):
            print('hello')
            self.min_good_rate = min_good_rate

    def set_min_view_count(self, min_view_count):
        if isinstance(min_view_count, int):
            self.min_view_count = min_view_count

    def set_movie_evaluation_attr(self, min_good_count, min_good_rate, min_view_count):
        self.set_min_good_count(min_good_count)
        self.set_min_good_rate(min_good_rate)
        self.set_min_view_count(min_view_count)

    def validation_content(self, good_count='', good_rate='', view_count=''):
        if good_count != '' and good_count < self.min_good_count:
            return False
        if good_rate != '' and good_rate < self.min_good_rate:
            return False
        if view_count != '' and view_count < self.min_view_count:
            return False

        return True
