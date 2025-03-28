import random

gifts = {
    'friends': {
        'A': {
            'F':
                [
                    [
                        '驚喜型:個性化禮物：定制首飾，如名字項鍊或刻有特殊日期的手鐲。定制T恤或背包，印有她喜歡的圖案或引言。',
                        '驚喜型:科技產品：最新的智能手表或耳機，特別是如果她對科技感興趣的話。一款流行的手機遊戲或應用程式的禮品卡。',
                        '驚喜型:生日派對：設計一場生日派對，邀請她的同學與朋友一同參加。',
                        '驚喜型:製作小糕點、甜品發送到她的教室，讓她可以與同學一起慶生享用。'
                    ],
                    [
                        '實用型:個性化禮物：定制首飾，如名字項鍊或刻有特殊日期的手鐲。定制T恤或背包，印有她喜歡的圖案或引言。',
                        '實用型:DIY手工藝套件：一個全套的DIY珠寶製作套件或編織套件，讓她能創造自己的作品。',
                        '實用型:閱讀愛好者：一套她最愛作家的書籍。一本特別的筆記本，配上一套優質的筆，鼓勵她寫下自己的故事。'
                    ],
                    [
                        '設計型:體驗禮物：給她預定一堂特殊的藝術課程，如陶藝、繪畫或舞蹈。',
                        '設計型:個性化禮物：定制首飾，如名字項鍊或刻有特殊日期的手鐲。定制T恤或背包，印有她喜歡的圖案或引言。',
                        '設計型:DIY手工藝套件：一個全套的DIY珠寶製作套件或編織套件，讓她能創造自己的作品。'
                    ],
                    [
                        '豪華型:主題驚喜派對：組織一個以她最喜歡的主題（如迪士尼公主、流行歌星、或科幻主題）為核心的驚喜派對。',
                        '豪華型:體驗禮物：預定一次冒險體驗，如攀岩、馬術或皮划艇。',
                        '豪華型:科技產品：最新的智能手表或耳機，特別是如果她對科技感興趣的話。一款流行的手機遊戲或應用程式的禮品卡。'
                    ]
                ],
            'M':
                [
                    [
                        '驚喜型:運動用品：足球、籃球或其他他喜歡運動的用品。運動服裝或鞋子，例如運動鞋或球隊球衣。',
                        '驚喜型:科學和教育玩具：科學實驗套裝，如小型化學實驗或機器人製作套件。教育型電子遊戲或學習工具，促進學習興趣和技能發展。',
                        '驚喜型:戶外活動和冒險設備：戶外探險套裝，如望遠鏡、指南針和背包。滑板、溜冰鞋或自行車。',
                        '驚喜型:書籍和音樂：他感興趣的主題或作家的書籍。音樂儀器，如吉他、鍵盤或打擊樂器，特別是如果他對音樂有興趣。',

                    ],
                    [
                        '實用型:個性化禮物：定制首飾，如名字項鍊或刻有特殊日期的手鐲。定制T恤或背包，印有她喜歡的圖案或引言。',
                        '實用型:DIY手工藝套件：一個全套的DIY珠寶製作套件或編織套件，讓她能創造自己的作品。',
                        '實用型:閱讀愛好者：一套她最愛作家的書籍。一本特別的筆記本，配上一套優質的筆，鼓勵她寫下自己的故事。'
                    ],
                    [
                        '設計型:體驗禮物：給她預定一堂特殊的藝術課程，如陶藝、繪畫或舞蹈。',
                        '設計型:個性化禮物：定制首飾，如名字項鍊或刻有特殊日期的手鐲。定制T恤或背包，印有她喜歡的圖案或引言。',
                        '設計型:DIY手工藝套件：一個全套的DIY珠寶製作套件或編織套件，讓她能創造自己的作品。'
                    ],
                    [
                        '豪華型:主題驚喜派對：組織一個以她最喜歡的主題（如迪士尼公主、流行歌星、或科幻主題）為核心的驚喜派對。',
                        '豪華型:體驗禮物：預定一次冒險體驗，如攀岩、馬術或皮划艇。',
                        '豪華型:科技產品：最新的智能手表或耳機，特別是如果她對科技感興趣的話。一款流行的手機遊戲或應用程式的禮品卡。'
                    ]
                ]



        }
    }
}

choosed1 = random.choice(gifts['friends']['A']['F'])
choosed2 = random.choice(choosed1)
print(choosed2)
