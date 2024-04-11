from turtle import Turtle


class EnemyManager(Turtle):

    def __init__(self, screen_size: tuple[int, int]):
        super().__init__()
        self.all_blocks: list[Turtle] = []
        self.all_rows: dict[str, list[Turtle]] = {}
        self.block_num: int = 0
        self.create_enemies(screen_size)

    def create_enemies(self, screen_size: tuple[int, int]) -> None:
        """Creates enemies"""
        block_len = None
        max_height = screen_size[1]-80
        max_width = screen_size[0]-20
        for num in range(60, 91):
            if max_width % num == 0:
                block_len = num
        if not block_len:
            block_len = 90
        for row_num in range(0, 5):
            self.all_blocks = []
            block = -max_width
            for _ in range(int((max_width*2)/block_len)):
                new_block = Turtle('arrow')
                new_block.shapesize(stretch_wid=2, stretch_len=2)
                new_block.penup()
                new_block.color('white')
                new_block.goto(block + block_len/2, max_height - row_num*60)
                new_block.right(90)
                new_block.shapesize(stretch_wid=2, stretch_len=4)
                block = block + block_len
                self.all_blocks.append(new_block)
            self.all_rows[new_block.ycor()] = self.all_blocks
            self.block_num += len(self.all_blocks)
