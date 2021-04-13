import sys
from selenium import webdriver
from config.av_config import av_config
from functions import is_empty
from functions import is_empty_obj
from functions import to_int
from functions import get_elapsed_day_count

# 引数に所々セットされている「base_element」は探索の起点となる。
# セットしない場合は、ベースページがからの要素の探索となる。


class Av:
    def __init__(self, theme):
        self.driver = {}
        self.theme = {}
        if(self.set_av_config(theme)):
            self.open_browser()
            self.driver.get(self.theme['base_url'])
        else:
            print('テーマ設定に失敗しました。')

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

        if(not self.theme):
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
            print('要素及びその値の抽出に必要なデータが取得できません。指定されたアイテムが設定ファイルに存在しません。')
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
            if (is_empty(count)):
                print(evaluation_item['name']+'が取得できていない。')
                return False

            if ('min' in evaluation_item and (to_int(count) < evaluation_item['min'])):
                print(evaluation_item['name']+'が' +
                      str(evaluation_item['min'])+'未満')
                return False

            if ('max' in evaluation_item and (to_int(count) > evaluation_item['max'])):
                print(evaluation_item['name']+'が' +
                      str(evaluation_item['max'])+'以上')
                return False

            return True
        except Exception as e:
            print('カウントのバリデーションに失敗')
            print(sys._getframe().f_code.co_name)
            print(e.args)

    # これはdate(0000.?.??)がどういう形式で取得されるのかによるな。
    def validate_elapsed_days_count(self, evaluation_item, date):
        try:
            elapsed_day_count = get_elapsed_day_count(date)

            if (is_empty(elapsed_day_count)):
                print(evaluation_item['name']+'が取得できていない。')
                return False

            if ('min' in evaluation_item and (elapsed_day_count < evaluation_item['min'])):
                print(evaluation_item['name']+'が' +
                      str(evaluation_item['min'])+'日未満')
                return False

            if ('max' in evaluation_item and (elapsed_day_count > evaluation_item['max'])):
                print(evaluation_item['name']+'が' +
                      str(evaluation_item['max'])+'日以上')
                return False

            return True
        except Exception as e:
            print('経過日数のバリデーションに失敗')
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

    def get_evaluation_items(self, base_element=None):
        evaluation_items = {}

        evaluation_items_config = self.theme['items']['evaluation_items']
        for item_name in evaluation_items_config:
            if (item_name == 'good_rate'):
                if ('good_count' not in evaluation_items_config or 'bad_count' not in evaluation_items_config):
                    print('高評価数と低評価数を取得する際の設定情報がありません。評価率を取得するにはそれら二つが必要です。')

                    return {}

                good_count = self.get_item('good_count', base_element)
                bad_count = self.get_item('bad_count', base_element)
                evaluation_items['good_rate'] = self.get_rate(
                    good_count, bad_count)
            else:
                evaluation_items[item_name] = self.get_item(
                    item_name, base_element)

        return evaluation_items

    def format_im_link(self, link):
        return '=IMAGE("' + link + '")'

    def get_page_link(self, link):
        if 'page_link' in link and link['page_link'] in link.values():
            return link['page_link']

        return ''

    def merge_page_im_links(self, page_links, im_links):
        links = []
        links_len = min(len(page_links), len(im_links))

        for index in range(links_len):
            links.append({
                'page_link': page_links[index],
                'im_link': self.format_im_link(im_links[index]),
            })

        return links

    def extract_links(self, links, need_word):
        for link in list(links):
            if (need_word not in link['page_link']):
                links.remove(link)

        return links

    def get_links(self, base_element=None):
        links = []

        if ('links' not in self.theme['items']):
            print('リンクを取得する際に必要な情報を設定してください。')
            return links

        links_conf = self.theme['items']['links']
        try:
            for link_name in links_conf:
                if (link_name == 'page_link'):
                    page_links = self.get_items('page_link', base_element)
                if (link_name == 'im_link'):
                    im_links = self.get_items('im_link', base_element)

            links = self.merge_page_im_links(page_links, im_links)
        except Exception as e:
            print('動画リンクとサムネイル画像のリンクが正しく取得できていません。')
            print(sys._getframe().f_code.co_name)
            print(str(e))

        return links

    def get_element(self, target, value, base_element=None):
        element = {}

        driver = self.driver
        if (not is_empty(base_element)):
            driver = base_element

        try:
            if target == 'id':
                element = driver.find_element_by_id(value)
            elif target == 'class':
                element = driver.find_element_by_class_name(value)
            elif target == 'tag':
                element = driver.find_element_by_css_selector(value)
        except Exception as e:
            print('ターゲットとなる要素の取得に失敗')
            print(str(e))

        return element

    def get_elements(self, target, value, base_element=None):
        elements = []

        driver = self.driver
        if (not is_empty(base_element)):
            driver = base_element

        try:
            if target == 'class':
                elements = driver.find_elements_by_css_selector(value)
            elif target == 'tag':
                elements = driver.find_elements_by_css_selector(value)
        except Exception as e:
            print('ターゲットとなる要素の取得に失敗')
            print(str(e))

        return elements

    def get_element_value(self, element, attr):
        value = ''
        try:
            if attr == 'text':
                value = element.text
            else:
                value = element.get_attribute(attr)
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

    def get_item(self, item_name, base_element=None):
        item = ''

        info = self.get_info_for_getting_item(item_name)

        if (is_empty_obj(info)):
            print('要素及びその値の抽出に必要なデータが取得されていません。指定されたアイテムが設定ファイルに存在しません。')
            return item

        try:
            element = self.get_element(
                info['target'], info['value'], base_element)
            item = self.get_element_value(element, info['attr'])
        except Exception as e:
            print('アイテムの取得に失敗')
            print(str(e))

        return item

    def get_items(self, item_name, base_element=None):
        items = []

        info = self.get_info_for_getting_item(item_name)

        if (is_empty_obj(info)):
            print('要素及びその値の抽出に必要なデータの取得されていません。おそらく、指定されたアイテムが設定ファイルに存在しません。')
            return items

        try:
            elements = self.get_elements(
                info['target'], info['value'], base_element)
            items = self.get_element_values(elements, info['attr'])
        except Exception as e:
            print('アイテム群の取得に失敗')
            print(str(e))

        return items

    def get_need_items(self, base_element=None):
        items = {}

        if ('need_items' not in self.theme['items']):
            print('シートに記載する必要な項目を設定してください。')
            return items

        need_items = self.theme['items']['need_items']
        for need_item_name in need_items:
            if (need_item_name == 'title'):
                items['title'] = self.get_item('title', base_element)
            if (need_item_name == 'tags'):
                items['tags'] = '・'.join(self.get_items('tags', base_element))

        return items

    def evaluate(self, evaluation_items):
        evaluation_config = self.theme['items']['evaluation_items']

        for evaluation_item_name in evaluation_items:
            if (evaluation_item_name == 'elapsed_days_count'):
                if (not self.validate_elapsed_days_count(evaluation_config[evaluation_item_name], evaluation_items[evaluation_item_name])):
                    return False
            elif ('count' in evaluation_item_name):
                if (not self.validate_count(evaluation_config[evaluation_item_name], evaluation_items[evaluation_item_name])):
                    return False
            elif ('rate' in evaluation_item_name):
                if (not self.validate_rate(evaluation_config[evaluation_item_name], evaluation_items[evaluation_item_name])):
                    return False

        print('基準クリア')
        return True

    def append_contents(self, contents, link, need_items, evaluated_contents):
        append_content = {}
        # 必ず必要なページリンクとサムネイル画像のリンク
        append_content.update(link)

        # 動画の質を判断する際の評価項目
        evaluated_contents = self.extract_contents_for_writing(
            evaluated_contents)
        append_content.update(evaluated_contents)

        # タイトルやタグなどの必要項目
        append_content.update(need_items)

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
                evaluation_items = self.get_evaluation_items()
                if (not self.evaluate(evaluation_items)):
                    print('基準を満たしていない。')
                    continue

                need_items = self.get_need_items()
                if (is_empty(need_items)):
                    print('必要項目が取得出来ていません。')
                    continue

                contents = self.append_contents(
                    contents, link, need_items, evaluation_items)
            except Exception as e:
                print('シート入力コンテンツの取得に失敗')
                print(str(e))
                continue

        return contents
