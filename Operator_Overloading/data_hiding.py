class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        while True:
            # if not self._lives:
            if self._lives == 0:
                print("Game Over")
                break
            else:
                self._lives += -1
                return self._lives


p = Player("mujtaba", 3)
p.hit()
p.hit()
p.hit()
p.hit()
