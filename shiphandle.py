class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __eq__(self, other):
        if type(self)==type(other):
            return self.x==other.x and self.y==other.y
        else:
            return ValueError("Cannot compare point to any other type of variable")
    def __copy__(self):
        return Point(self.x,self.y)
    def __str__(self):
        return f"{self.x} {self.y}"
    def __hash__(self):
        return (self.x**(10+len(str(self.y))+1)+self.y)%(10**9+7)

class Board:
    def __init__(self):
        self.__board__=[[0 for x in range(11)] for x in range(11)]
        self.hit_position=set()
        self.hit_to_ship_position=set()
    def Board_Piece_Here(self,x,y):
        try:
            self.__board__[x][y] = self.__board__[x][y]&2
        except:
            return False
        return True
    def Is_hit(self,x,y):
        return self.__board__[x][y]&1
    def Hit(self,x,y):
        try:
            self.__board__[x][y] = self.__board__[x][y]&1
            if self.__board__[x][y]&2:
                self.hit_to_ship_position.add(Point(x,y))
            self.hit_position.add(Point(x, y))
        except:
            return False
        return True
    def BoardPieceHere(self,point):
        if type(point)!=type(Point()):
            return False
        return self.Board_Piece_Here(point.x,point.y)
    def IsHit(self,point):
        if type(point)!=type(Point()):
            return False
        return self.Is_hit(point.x,point.y)
    def HitPointobj(self,point):
        if type(point)!=type(Point()):
            return False
        return self.Hit(point.x,point.y)
