from collections import UserList

class MagicList(UserList):

    def __init__(self):
        super().__init__(self)

    # set our code to accept key (i) and value (item) for indexing
    def __setitem__(self, i, item):
        if len(self.data) >= i:
            self.data.append(item)
        else:
            super().__setitem__(i, item)

    # set our code to read the data provided
    def __getitem__(self, i):
        if len(self.data) >= i:
            self.data.append(self)
        return super().__getitem__(i)


