import numpy as np
from angle_interface import angle_interface as ai

'''
・制御入力を実機とやりとりする際に用いる
・生のnumpy配列を引数でやり取りしてどの角度形式が用いられているかわからず混乱することを避けるのが目的
'''

class Control:
    def __init__(self, radvec: np.ndarray) -> None:
        self.radvec = radvec

    '''
        input
    '''
    @classmethod
    def from_radvec(cls, radvec: np.ndarray):
        return cls(radvec)

    @classmethod
    def from_degvec(cls, degvec: np.ndarray):
        radvec = ai.degree2radian(degvec)
        return cls(radvec)

    @classmethod
    def from_resvec(cls, resvec: np.ndarray):
        radvec = ai.resolution2radian(resvec)
        return cls(radvec)

    '''
        output
    '''
    def as_radvec(self) -> np.ndarray:
        return self.radvec

    def as_degvec(self) -> np.ndarray:
        return ai.radian2degree(self.radvec)

    def as_resvec(self) -> np.ndarray:
        return ai.radian2resolution(self.radvec)


if __name__ == '__main__':
    # ------------ Example usage (input) ------------
    print("--------------------------------------")
    radvec = np.array([0, 3.1415, 6.28319], dtype=float)
    ctrl1 = Control.from_radvec(radvec)
    print(f"ctrl1.radvec = {ctrl1.radvec}")

    degvec = np.array([0, 180, 360], dtype=float)
    ctrl2 = Control.from_degvec(degvec)
    print(f"ctrl2.radvec = {ctrl2.radvec}")

    resvec = np.array([0, 2000, 4440], dtype=float)
    ctrl3 = Control.from_resvec(resvec)
    print(f"ctrl3.radvec = {ctrl3.radvec}")

    # ------------ Example usage (output) ------------
    print("--------------------------------------")
    print(f"ctrl1.as_resvec = {ctrl1.as_resvec()}")
    print(f"ctrl2.as_resvec = {ctrl2.as_resvec()}")
    print(f"ctrl3.as_radvec = {ctrl3.as_radvec()}")
    print(f"ctrl3.as_degvec = {ctrl3.as_degvec()}")
    print("--------------------------------------")
