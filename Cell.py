class Cell:
    def __init__(self, cellType):
        self.cellType = cellType
        self.apple = "\u1f34e"

    def __repr__(self):
        if self.cellType == "Empty":
            return "⬜"
        if self.cellType == "Wall":
            return "⬛"
        if self.cellType.split(" ")[0] == "Body":
            return "▣"
        if self.cellType == "Apple":
            return "☑"

    def __str__(self):
        if self.cellType == "Empty":
            return "⬜"
        if self.cellType == "Wall":
            return "⬛"
        if self.cellType.split(" ")[0] == "Body":
            return "▣"
        if self.cellType == "Apple":
            return "☑"

    def is_hard(self):
        if self.cellType == "Wall" or self.cellType.split(" ")[0] == "Body":
            return True
        return False

