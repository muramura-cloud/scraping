from functions import is_empty

evaluation_items = {
    'good_count': {
        'name': '高評価数',
                'value': 10,
                'target': 'id',
                'target_value': 'btn_good',
                'attr': 'text',
    },
    'bad_coungat': {
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

print(obj1)
