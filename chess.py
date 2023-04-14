class Figura:
    color: str = "white"
# место на доске
    x: int = 0
    y: int = 0

    def __init__(self, x1: int, y1: int, color_temp: str):
        self.set_color(color_temp)
        if self._check_border(x1, y1):
            self.x = x1
            self.y = y1
        elif color_temp == "white":
            self.x = 0
            self.y = 0
        elif color_temp == "black":
            self.x = 7
            self.y = 7

    def set_color(self, color_: str):
        if color_ == "white":
            self.color = color_
        else:
            self.color = "black"

    def change_color(self):
        if self.color == "white":
            self.color = "black"
        elif self.color == "black":
            self.color = "white"
        else:
            return False

    def _check_border(self, x1: int, y1: int) -> bool:
        if 0 <= x1 <= 7 and 0 <= y1 <= 7:
            return True

    def change_position(self, x1, y1):
        if self._check_border(x1, y1) and self.check_move(x1, y1):
            x = x1
            y = y1

    def check_move(self, x1, y1) -> bool:
        raise NotImplemented


class Pawns(Figura):

    def check_move(self, x2, y2):
        if self._check_border(x2, y2):
            if self.color == "white":
                if x2 - self.x == 1 and y2 == self.y:
                    return True
            elif self.color == "black" and y2 == self.y:
                if self.x - x2 == 1:
                    return True
        else:
            return False


class Knight(Figura):

    def check_move(self, x2, y2):
        move1 = abs(x2 - self.x)
        move2 = abs(y2 - self.y)
        if self._check_border(x2, y2):
            if move1 == 1 and move2 == 2 or move1 == 2 and move2 == 1:
                return True


class King(Figura):

    def check_move(self, x2, y2):
        if self._check_border(x2, y2):
            move1 = abs(x2 - self.x)
            move2 = abs(y2 - self.y)
            if self._check_border(x2, y2):
                if move1 == 1 and move2 == 1 or move1 == 0 and move2 == 1 or move1 == 1 and move2 == 0:
                    return True


class Bishop(Figura):

    def check_move(self, x2, y2):
        if self._check_border(x2, y2):
            move1 = abs(x2 - self.x)
            move2 = abs(y2 - self.y)
            if self._check_border(x2, y2):
                if move1 == move2:
                    return True


class Rook(Figura):

    def check_move(self, x2, y2):
        if self._check_border(x2, y2):
            move1 = abs(x2 - self.x)
            move2 = abs(y2 - self.y)
            if self._check_border(x2, y2):
                if move1 == 0 and move2 > 0 or move1 > 0 and move2 == 0:
                    return True


class Queen(Figura):

    def check_move(self, x2, y2):
        if self._check_border(x2, y2):
            move1 = abs(x2 - self.x)
            move2 = abs(y2 - self.y)
            if self._check_border(x2, y2):
                if move1 == 0 and move2 > 0 or move1 > 0 and move2 == 0 or move1 == move2:
                    return True


def check_list(list_: list, m, p):
    new_list = []
    for i in list_:
        if isinstance(i, Figura):
            if i.check_move(m, p):
                new_list.append(i)
                return(new_list)
