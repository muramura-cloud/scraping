from selenium import webdriver
from av_config import av_config
from functions import is_empty
from functions import is_empty_obj
from functions import to_int
import sys


class Av:
    def __init__(self, theme):
        self.driver = {}
        self.theme = {}
        if(self.set_av_config(theme)):
            # ブラウザを開く。
            self.open_browser()
            # ベースページを開いておく。。
            self.driver.get(self.theme['base_url'])
        else:
            print('テーマの設定に失敗しました。')

            pass

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

    def set_av_config(self, theme):
        for theme_name in av_config:
            if(theme_name == theme):
                self.theme = av_config[theme_name]

                return True

        if(self.theme == {}):
            print('指定されたテーマに対応していません。対応しているテーマは以下です。')
            print(list(av_config))

            return False

    def get_rate(self, count1, count2):
        rate = 0
        if (is_empty(count1) or is_empty(count2)):
            print('割合を取得する際に必要な二つの数値が取得できていない。')
            return rate

        try:
            if to_int(count1) > 0 or to_int(count2) > 0:
                rate = round(to_int(count1) /
                             (to_int(count1) + to_int(count2)), 2)

            return rate
        except Exception as e:
            print('割合の取得に失敗しました。')
            print(str(e))

    def get_info_for_getting_item(self, item_name):
        target = None
        value = None
        attr = None

        try:
            for items_name in self.theme['items']:
                if (item_name in self.theme['items'][items_name]):
                    target = self.theme['items'][items_name][item_name]['target']
                    value = self.theme['items'][items_name][item_name]['value']
                    attr = self.theme['items'][items_name][item_name]['attr']
        except Exception as e:
            print('要素及びその値の抽出に必要なデータが取得されていません。おそらく、指定されたアイテムが設定ファイルに存在しません。')
            print(sys._getframe().f_code.co_name)
            print(e)

        info = {
            'target': target,
            'value': value,
            'attr': attr}

        return info

    def extract_contents_for_writing(self, contents):
        for evaluated_item_name in list(contents):
            if (self.theme['items']['evaluation_items'][evaluated_item_name]['required'] == False):
                del contents[evaluated_item_name]

        return contents

    def validate_count(self, evaluation_item, count):
        try:
            if (count == ''):
                print(evaluation_item['name']+'が取得できていない。')
                return False

            if ('min' in evaluation_item and (to_int(count) < evaluation_item['min'])):
                print(evaluation_item['name']+'が' +
                      str(evaluation_item['min'])+'未満')
                return False

            if ('max' in evaluation_item and (to_int(count) < evaluation_item['max'])):
                print(evaluation_item['name']+'が' +
                      str(evaluation_item['max'])+'以上')
                return False

            return True
        except Exception as e:
            print('カウントのバリデーションに失敗')
            print(sys._getframe().f_code.co_name)
            print(e.args)

    def validate_rate(self, evaluation_item, rate):
        try:
            if ('min' in evaluation_item and rate < evaluation_item['min']):
                print(evaluation_item['name']+'が' +
                      str(evaluation_item['min'])+'未満')
                return False

            return True

        except Exception as e:
            print('割合のバリデーションに失敗')
            print(sys._getframe().f_code.co_name)
            print(str(e))

    def evaluate_contents(self):
        evaluation_items = self.theme['items']['evaluation_items']

        evaluated_contents = {}
        for evaluation_item_name in evaluation_items:
            if (evaluation_item_name == 'good_count'):
                good_count = self.get_item('good_count')
                if (self.validate_count(evaluation_items[evaluation_item_name], good_count)):
                    evaluated_contents['good_count'] = good_count
                else:
                    return {}

            if (evaluation_item_name == 'bad_count'):
                bad_count = self.get_item('bad_count')
                if (self.validate_count(evaluation_items[evaluation_item_name], bad_count)):
                    evaluated_contents['bad_count'] = bad_count
                else:
                    return {}

            if (evaluation_item_name == 'good_rate'):
                if ('good_count' not in evaluation_items or 'bad_count' not in evaluation_items):
                    print('高評価数と低評価数を取得する際の設定情報がありません。評価率を取得するにはそれら二つが必要です。')
                    return {}

                good_count = self.get_item('good_count')
                bad_count = self.get_item('bad_count')
                good_rate = self.get_rate(good_count, bad_count)
                if (self.validate_rate(evaluation_items[evaluation_item_name], good_rate)):
                    evaluated_contents['good_rate'] = good_rate
                else:
                    return {}

            if (evaluation_item_name == 'view_count'):
                view_count = self.get_item('view_count')
                if (self.validate_count(evaluation_items[evaluation_item_name], view_count)):
                    evaluated_contents['view_count'] = view_count
                else:
                    return {}

        print('基準クリア')
        return evaluated_contents

    def get_im_link(self, link):
        if 'im_link' in link and link['im_link'] in link.values():
            return '=IMAGE("' + link['im_link'] + '")'

        return 'サムネイル画像はありません。'

    def get_page_link(self, link):
        if 'page_link' in link and link['page_link'] in link.values():
            return link['page_link']

        return ''

    def get_links(self):
        links = []

        if ('links' not in self.theme['items']):
            print('リンクを取得する際に必要な情報を設定してください。')
            return links

        links_conf = self.theme['items']['links']
        for link_name in links_conf:
            if (link_name == 'page_link'):
                page_links = self.get_items('page_link')
            if (link_name == 'im_link'):
                im_links = self.get_items('im_link')

        # 動画リンクとサムネイル画像のリンクをセットにしたオブジェクトの形にする
        try:
            for (index, num) in enumerate(page_links):
                links.append({
                    'page_link': page_links[index],
                    'im_link': im_links[index],
                })
        except Exception as e:
            print('動画リンクとサムネイル画像のリンクが正しく取得できていません。')
            print(str(e))

        return links

    def get_element(self, target, value):
        element = {}
        try:
            if target == 'id':
                element = self.driver.find_element_by_id(value)
            elif target == 'class':
                element = self.driver.find_element_by_class_name(value)
            elif target == 'tag':
                element = self.driver.find_element_by_css_selector(value)
        except Exception as e:
            print('ターゲットとなる要素の取得に失敗')
            print(str(e))

        return element

    def get_elements(self, target, value):
        elements = []
        try:
            if target == 'class':
                elements = self.driver.find_elements_by_css_selector(value)
            elif target == 'tag':
                elements = self.driver.find_elements_by_css_selector(value)
                print(value)
                print(elements)
        except Exception as e:
            print('ターゲットとなる要素の取得に失敗')
            print(str(e))

        return elements

    def get_element_value(self, element, attr):
        value = ''
        try:
            if attr == 'text':
                value = element.text
            elif attr == 'data-rating':
                value = element.get_attribute('data-rating')
        except Exception as e:
            print('要素の値の取得に失敗')
            print(sys._getframe().f_code.co_name)
            print(str(e))

        return value

    def get_element_values(self, elements, attr):
        values = []
        try:
            if attr == 'text':
                values = [element.text for element in elements]
            else:
                values = [element.get_attribute(
                    attr) for element in elements]
        except Exception as e:
            print('要素群の値の取得に失敗')
            print(sys._getframe().f_code.co_name)
            print(str(e))

        return values

    def get_item(self, item_name):
        item = ''

        info = self.get_info_for_getting_item(item_name)

        if (is_empty_obj(info)):
            print('要素及びその値の抽出に必要なデータが取得されていません。指定されたアイテムが設定ファイルに存在しません。')
            return item

        try:
            element = self.get_element(info['target'], info['value'])
            item = self.get_element_value(element, info['attr'])
        except Exception as e:
            print('アイテムの取得に失敗')
            print(str(e))

        return item

    def get_items(self, item_name):
        items = []

        info = self.get_info_for_getting_item(item_name)

        if (is_empty_obj(info)):
            print('要素及びその値の抽出に必要なデータの取得されていません。おそらく、指定されたアイテムが設定ファイルに存在しません。')
            return items

        try:
            elements = self.get_elements(info['target'], info['value'])
            items = self.get_element_values(elements, info['attr'])
        except Exception as e:
            print('アイテム群の取得に失敗')
            print(str(e))

        return items

    # 取得したいデータ項目(evaluation_itemsとか、linksとか)だけを引数に入れれば取得できるようになるとなお便利
    def get_need_items(self):
        items = {}

        if ('need_items' not in self.theme['items']):
            print('シートに記載する必要な項目を設定してください。')
            return items

        need_items = self.theme['items']['need_items']
        for need_item_name in need_items:
            if (need_item_name == 'title'):
                items['title'] = self.get_item('title')
            if (need_item_name == 'tags'):
                items['tags'] = '・'.join(self.get_items('tags'))

        return items

    def append_contents(self, contents, link, need_items, evaluated_contents):
        append_content = {}
        # 必ず必要なページリンクとサムネイル画像のリンク
        append_content.update(link)

        # タイトルやタグなどの必要項目
        append_content.update(need_items)

        # 動画の質を判断する際の評価項目
        evaluated_contents = self.extract_contents_for_writing(
            evaluated_contents)
        append_content.update(evaluated_contents)

        contents.append(append_content)
        return contents

    def get_contents(self, links):
        contents = []
        for link in links:
            page_link = self.get_page_link(link)
            if (is_empty(page_link)):
                print('遷移先のページリンクが取得できていません。')
                continue

            print(page_link)
            self.driver.get(page_link)
            try:
                evaluated_contents = self.evaluate_contents()
                if (not is_empty(evaluated_contents)):
                    need_items = self.get_need_items()
                    if (is_empty(need_items)):
                        print('シートに記載する必要項目が取得出来ていません。')
                        continue

                    contents = self.append_contents(
                        contents, link, need_items, evaluated_contents)
            except Exception as e:
                print('シート入力コンテンツの取得に失敗')
                print(str(e))
                continue

        return contents
