class Post:
    def __init__(self, post_id, title, subtitle, body):
        self.id: int = post_id
        self.title: str = title
        self.subtitle: str = subtitle
        self.body: str = body
