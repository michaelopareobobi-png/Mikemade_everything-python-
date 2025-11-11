class a:

    def __init__(self):
        print('init-A')

    def lap(self):
        print('lap-A')


class b(a):
    def __init__(self):
        super().__init__()
        print('init-B')

    def tap(self):
        super().lap()
        print('tap-B')

f=b()
f.tap()