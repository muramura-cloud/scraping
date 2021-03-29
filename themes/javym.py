from av import Av
from functions import is_empty
import sys



class Javym(Av):
    def get_link(self, url='', base_element=None):
        if url != '':
            self.driver.get(url)

        link = {
            'page_link': self.get_item('page_link', base_element),
            'im_link': self.format_im_link(self.get_item('im_link', base_element)),
        }

        return link

    # 詳細ページに行く必要がなかったから、独自にコンテンツを取得する。
    def get_contents(self):
        contents = []

        articles = self.get_elements('tag', 'article')
        for article in articles:
            try:
                evaluation_items = self.get_evaluation_items(article)
                if (not self.evaluate(evaluation_items)):
                    print('基準を満たしていない。')
                    continue

                need_items = self.get_need_items(article)
                link = self.get_link('', article)
                print(link['page_link'])
                if (is_empty(need_items) or is_empty(link)):
                    print('必要項目が取得出来ていません。')
                    continue

                contents = self.append_contents(
                    contents, link, need_items, evaluation_items)
            except Exception as e:
                print('シート入力コンテンツの取得に失敗')
                print(str(e))
                continue

        # ブラウザを閉じる
        self.driver.quit()

        return contents
