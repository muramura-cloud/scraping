from logging import NOTSET
from functions import is_empty
from functions import is_empty_obj
from functions import to_int

items = {
    'links': {
        'page_link': {
            'name': '遷移先リンク',
            'target': 'tag',
            'value': '.article_content h3 a',
            'attr': 'href',
        },
        'im_link': {
            'name': 'サムネイル画像リンク',
            'target': 'tag',
            'value': '.article_content h3 a',
            'attr': 'src',
        },
    },
    'evaluation_items': {
        'good_count': {
            'name': '高評価数',
            'required': True,
            'min': 10,
            'target': 'id',
            'target_value': 'btn_good',
            'attr': 'text',
        },
        'bad_count': {
            'name': '低評価数',
            'required': False,
            'target': 'id',
            'target_value': 'btn_bad',
            'attr': 'text',
        },
        'good_rate': {
            'name': '高評価率',
            'required': True,
            'min': 0.85,
        },
    },
    'need_items': {
        'title': {
            'name': 'タイトル',
            'target': 'tag',
            'value': 'h1',
            'attr': 'text',
        },
        'tags': {
            'name': 'タグ',
            'target': 'tag',
            'value': 'article footer li a',
            'attr': 'text',
        },
    }
}

name = 'title'

# for (index, num) in enumerate(list1):
#     list3.append({
#         'page_link': list1[index],
#         'im_link': list2[index],
#     })
links = [
    {'page_link': 'https://www.nukistream.com/video.php?id=747495', 'im_link': None},
    {'page_link': 'https://javym.net/count/48616/', 'im_link': None},
    {'page_link': 'https://erry.one/video/34763/', 'im_link': None},
    {'page_link': 'https://sugirl.info/video/36810/', 'im_link': None},
    {'page_link': 'http://smanavi.net/app/func_pub/click.php?number=1282843834&dst=1228148229', 'im_link': None},
    {'page_link': 'http://smanavi.net/smanavitool/app/func/pr_click/pr_click.php?no=1282843834&id=1294&c=1', 'im_link': None}]

del_list_indexes = []
for index, link in enumerate(links):
    if ('https://www.nukistream.com/video.php' not in link['page_link']):
        del_list_indexes.append(index)

del links[del_list_indexes[0]:del_list_indexes[-1]]


print(links)
