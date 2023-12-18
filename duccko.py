from typing import Self
import pyxel

class App:

    def __init__(self):

        #フィールドの大きさ
        pyxel.init(120, 80)

        pyxel.load('kamo.pyxres')
        #鴨関連
        self.duck = Duck()
        self.duck
        #壁関連
        self.wall=[Wall(), Wall(), Wall(), Wall(), Wall(), Wall()]

        self.enemy = Enemy()

        self.gameoverflag = False

        pyxel.run(self.update, self.draw)


    def update(self):
        self.duck.move()
        self.enemy.move()


    def draw(self):
        pyxel.cls(7)
        pyxel.bltm(0, 0, 0, 0, 0, 120, 80, 0)
        self.duck.draw()

        self.enemy.draw()

        for i in self.wall:
            i.draw()

        
        

class Wall():

    def __init__(self):
        self.x = pyxel.rndi(8, 104)
        self.y = pyxel.rndi(8, 64)

    def draw(self):
        pyxel.blt(self.x, self.y , 0, 0, 8, 8, 8, 0)
        


class Duck:

    def __init__(self):
    #鴨の初期設定
        #スタート地点右下
        self.x= 112
        self.y= 72
        self.dir = 1
        pyxel.load('kamo.pyxres')
        
    def move(self):
        #矢印キーの操作
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2
            self.dir = 0
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
            self.dir = 1
        elif pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2
    
    def draw(self):
        #鴨の描画
        if self.dir == 1:
            pyxel.blt(self.x, self.y, 0, 0, 0, 8, 8, 0)

        if self.dir == 0:
            pyxel.blt(self.x, self.y, 0, 8, 8, 8, 8, 0)


class Enemy:
    def __init__(self):
        self.x= 0
        self.y= 0
        self.vx= pyxel.rndi(-2,2)
        self.vy= pyxel.rndi(-2,2)
    def move(self):
        self.x += self.vx
        self.y += self.vy
        pass
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 8, 0, 8, 8, 0)

App()