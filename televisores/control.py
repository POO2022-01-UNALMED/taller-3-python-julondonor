from televisores.tv import TV

class Control:
    def getTv(self):
        return self._tv
    def setTv(self, tv):
        self._tv = tv
    
    def enlazar(self, tv):
        self._tv = tv
        tv._control = self
    
    def turnOn(self):
        if isinstance(self._tv, TV):
            self._tv.turnOn()
    def turnOff(self):
        if isinstance(self._tv, TV):
            self._tv.turnOff()
    def canalUp(self):
        if isinstance(self._tv, TV):
            self._tv.canalUp()
    def canalDown(self):
        if isinstance(self._tv, TV):
            self._tv.canalDown()
    def volumenUp(self):
        if isinstance(self._tv, TV):
            self._tv.volumenUp()
    def volumenDown(self):
        if isinstance(self._tv, TV):
            self._tv.volumenDown()
    def setCanal(self, num):
        if isinstance(self._tv, TV):
            self._tv.setCanal(num)