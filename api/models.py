class News:
    def __init__(self, tit, des, img):
        self.tit = tit
        self.des = des
        self.img = img

news1 = News(
    "iPhone 16 Pro Max",
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
    "https://github.com/eminshikh/images/blob/main/iphone_16_pro_max.png?raw=true"
)

news2 = News(
    "AirPods Pro 3",
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
    "https://github.com/eminshikh/images/blob/main/Apple-AirPods-Pro-3.jpg?raw=true"
)

news3 = News(
    "Apple Watch Ultra 3",
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
    "https://github.com/eminshikh/images/blob/main/Apple-Watch-Ultra-3.jpg?raw=true"
)

news_list = [news1, news2, news3]