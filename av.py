from selenium import webdriver


class Av:
    def __init__(self, url):
        self.url = url
        self.like_count = 10
        self.like_rate = 0.8
        self.view_count = 5000

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

    def set_like_count(self, like_count):
        self.like_count = like_count

    def set_like_rate(self, like_rate):
        self.like_rate = like_rate

    def set_view_count(self, view_count):
        self.view_count = view_count
