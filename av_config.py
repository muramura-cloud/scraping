# この設定をもとにget_contents()を叩けば良い。
# ある特定の関数を叩けば、簡単にこのファイルを生成あるいは変更できる仕組みがあるとさらに便利だな。
av_config = {
    'nukisuto': {
        'theme_name': '抜きスト',
        'base_url': 'https://www.nukistream.com/',
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
    },
    'iqoo': {
        'theme_name': 'iQoo',
        'base_url': 'https://iqoo.me/',
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
        },
    },
    'pornhub': {
        'theme_name': 'Pornhub',
        'base_url': 'https://jp.pornhub.com/',
        'evaluation_items': {
            'good_count': {
                'name': '高評価数',
                'required': True,
                'min': 100,
                'target': 'class',
                'target_value': 'votesUp',
                'attr': 'data-rating',
            },
            'bad_count': {
                'name': '低評価数',
                'required': False,
                'max': 30,
                'target': 'class',
                'target_value': 'votesDown',
                'attr': 'data-rating',
            },
            'view_count': {
                'name': '再生数',
                'required': False,
                'min': 10000,
                'target': 'class',
                'target_value': 'count',
                'attr': 'text',
            },
            'good_rate': {
                'name': '高評価率',
                'required': True,
                'min': 0.8,
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
                'target': 'class',
                'value': '.categoriesWrapper .item',
                'attr': 'text',
            },
        },
    },
}
