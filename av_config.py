av_config = {
    'nukisuto': {
        'theme_name': '抜きスト',
        'base_url': 'https://www.nukistream.com/',
        'items': {
            'links': {
                'page_link': {
                    'name': 'リンク',
                    'required': True,
                    'target': 'tag',
                    'value': '.article_content h3 a',
                    'attr': 'href',
                },
                'im_link': {
                    'name': 'サムネイル',
                    'required': True,
                    'target': 'tag',
                    'value': 'article img',
                    'attr': 'src',
                },
            },
            'evaluation_items': {
                'good_count': {
                    'name': '高評価数',
                    'required': True,
                    'min': 10,
                    'target': 'id',
                    'value': 'btn_good',
                    'attr': 'text',
                },
                'bad_count': {
                    'name': '低評価数',
                    'required': False,
                    'target': 'id',
                    'value': 'btn_bad',
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
                    'required': True,
                    'target': 'tag',
                    'value': 'h1',
                    'attr': 'text',
                },
                'tags': {
                    'name': 'タグ',
                    'required': True,
                    'target': 'tag',
                    'value': 'article footer li a',
                    'attr': 'text',
                },
            },
        },
    },
    'iqoo': {
        'theme_name': 'iQoo',
        'base_url': 'https://iqoo.me/',
        'items': {
            'links': {
                'page_link': {
                    'name': '遷移先リンク',
                    'required': True,
                    'target': 'tag',
                    'value': '.article_content h3 a',
                    'attr': 'href',
                },
                'im_link': {
                    'name': 'サムネイル画像リンク',
                    'required': True,
                    'target': 'tag',
                    'value': 'article img',
                    'attr': 'src',
                },
            },
            'evaluation_items': {
                'good_count': {
                    'name': '高評価数',
                    'required': True,
                    'min': 10,
                    'target': 'id',
                    'value': 'btn_good',
                    'attr': 'text',
                },
                'bad_count': {
                    'name': '低評価数',
                    'required': False,
                    'target': 'id',
                    'value': 'btn_bad',
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
                    'required': True,
                    'target': 'tag',
                    'value': 'h1',
                    'attr': 'text',
                },
                'tags': {
                    'name': 'タグ',
                    'required': True,
                    'target': 'tag',
                    'value': 'article footer li a',
                    'attr': 'text',
                },
            },
        }
    },
    'sugirl': {
        'theme_name': 'シュガール',
        'base_url': 'https://sugirl.info/',
        'items': {
            'links': {
                'page_link': {
                    'name': 'リンク',
                    'required': True,
                    'target': 'tag',
                    'value': 'article a',
                    'attr': 'href',
                },
                'im_link': {
                    'name': 'サムネイル',
                    'required': True,
                    'target': 'tag',
                    'value': 'article figure img',
                    'attr': 'src',
                },
            },
            'evaluation_items': {
                'view_count': {
                    'name': '再生数',
                    'required': False,
                    'min': 10000,
                    'target': 'class',
                    'value': 'views',
                    'attr': 'text',
                },
                'elapsed_days_count': {
                    'name': '経過日数',
                    'required': False,
                    'max': 3,
                    'target': 'tag',
                    'value': 'article header time',
                    'attr': 'text',
                },
            },
            'need_items': {
                'title': {
                    'name': 'タイトル',
                    'required': True,
                    'target': 'tag',
                    'value': 'h1',
                    'attr': 'text',
                },
                'tags': {
                    'name': 'タグ',
                    'required': True,
                    'target': 'tag',
                    'value': '.tagList li a',
                    'attr': 'text',
                },
            },
        }
    },
    'javym': {
        'theme_name': 'ジャビま',
        'base_url': 'https://javym.net/',
        'items': {
            'links': {
                'page_link': {
                    'name': 'リンク',
                    'required': True,
                    'target': 'tag',
                    'value': 'article h2 a',
                    'attr': 'href',
                },
                'im_link': {
                    'name': 'サムネイル',
                    'required': True,
                    'target': 'tag',
                    'value': 'article img',
                    'attr': 'src',
                },
            },
            'evaluation_items': {
                'good_count': {
                    'name': '高評価数',
                    'required': True,
                    'min': 30,
                    'target': 'tag',
                    'value': 'article figure strong',
                    'attr': 'text',
                },
            },
            'need_items': {
                'title': {
                    'name': 'タイトル',
                    'required': True,
                    'target': 'tag',
                    'value': 'h2',
                    'attr': 'text',
                },
                'tags': {
                    'name': 'タグ',
                    'required': True,
                    'target': 'class',
                    'value': '.tagList',
                    'attr': 'text',
                },
            },
        },
    },
    'pornhub': {
        'theme_name': 'Pornhub',
        'base_url': 'https://jp.pornhub.com/',
        'items': {
            'links': {
                'page_link': {
                    'name': 'リンク',
                    'required': True,
                    'target': 'tag',
                    'value': '.pcVideoListItem a',
                    'attr': 'href',
                },
                'im_link': {
                    'name': 'サムネイル',
                    'required': True,
                    'target': 'tag',
                    'value': '.pcVideoListItem .phimage a img',
                    'attr': 'data-thumb_url',
                },
            },
            'evaluation_items': {
                'good_count': {
                    'name': '高評価数',
                    'required': True,
                    'min': 100,
                    'target': 'tag',
                    'value': '.votesUp',
                    'attr': 'data-rating',
                },
                'bad_count': {
                    'name': '低評価数',
                    'required': False,
                    'max': 30,
                    'target': 'tag',
                    'value': '.votesDown',
                    'attr': 'data-rating',
                },
                'view_count': {
                    'name': '再生数',
                    'required': False,
                    'min': 10000,
                    'target': 'tag',
                    'value': '.count',
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
                    'required': True,
                    'target': 'tag',
                    'value': 'h1',
                    'attr': 'text',
                },
                'tags': {
                    'name': 'タグ',
                    'required': True,
                    'target': 'class',
                    'value': '.categoriesWrapper .item',
                    'attr': 'text',
                },
            },
        },
    },
}
