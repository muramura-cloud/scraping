from functions import is_empty
from functions import to_int

evaluation_items = {
    'good_count': {
        'name': '高評価数',
                'value': 10,
                'target': 'id',
                'target_value': 'btn_good',
                'attr': 'text',
    },
    'bad_count': {
        'name': '低評価数',
                'target': 'id',
                'target_value': 'btn_bad',
                'attr': 'text',
    },
    'good_rate': 0.8,
}


link = {
    'page_link': 'https://www.nukistream.com/video.php?id=747482',
    'im_link': 'https://img.nukistream.com/files/745599.jpg',
}

obj1 = {}

ob2 = {'page_link': '630', 'im_link': '77'}

obj1.update(ob2)

num = '30,809'

print(to_int(num))

print(obj1)
