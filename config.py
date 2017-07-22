class Config:
    def __init__(self):
        self.file = {
                'data': 'whiteboard.p',
                'text': 'whiteboard.txt'}

    def get_file(self, item):
        return self.file[item]
