class Post:
    def __init__(self, poster_name, poster_avatar, pic, content, view_count, likes_count, pk):
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.like_count = likes_count
        self.views_count = view_count
        self.pk = pk

    def __repr__(self):
        return f'{self.poster_name}, номер поста {self.pk}'
