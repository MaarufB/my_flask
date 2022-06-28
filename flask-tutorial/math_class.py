from threading import Thread
from queue import Queue

class Math:
    def __init__(self):
        self.q = Queue()

    async def sum(self, first, second):
        return first + second

    async def loop(self, end):
        arr = list()

        count = 0
        while count <= end:
            # print(f'Counting start from: {count}')
            arr.append(f'Counting start from: {count}')
            count += 1

        # for i in range(len(arr)):
        #     print(f'{i}')

        return arr


    async def start(self):
        pass