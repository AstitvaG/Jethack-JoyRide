class Stats:
    _livesLeft=3
    coinsCollected=0
    enemiesKilled=0
    _isAlive=True
    def incrCoins(self):
        self.coinsCollected+=1
    def killEnemy(self):
        self.enemiesKilled+=1
    def killed(self):
        self._livesLeft-=1
        if(self._livesLeft<0):
            self._isAlive=False