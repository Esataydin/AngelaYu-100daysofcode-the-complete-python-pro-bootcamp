from turtle import Turtle
import random


COLORS: list[str] = ["red", "orange", "yellow", "green", "blue", "purple"]


class BlockManager(Turtle):

    def __init__(self, screen_size: tuple[int, int]):
        super().__init__()
        self.all_blocks: list[Turtle] = []
        self.all_rows: list[list[Turtle]] = []
        self.block_num: int = 0
        self.create_blocks(screen_size)

    def create_blocks(self, coords: tuple[int, int]) -> None:
        max_height = coords[1]/2
        max_width = coords[0]-20
        for row_num in range(0, 4):
            self.all_blocks = []
            block = -max_width
            while block in range(-max_width, max_width):
                if max_width-block > 80:
                    block_len = random.randint(70, 80)
                else:
                    block_len = max_width-block
                new_block = Turtle('square')
                new_block.shapesize(stretch_wid=1.5, stretch_len=block_len/16)
                new_block.penup()
                new_block.color(random.choice(COLORS))
                new_block.goto(block + block_len/3, max_height - row_num*32)
                block = block + block_len
                self.all_blocks.append(new_block)
            self.all_rows.insert(row_num, self.all_blocks)
            self.block_num += len(self.all_blocks)
