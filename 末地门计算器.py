import math
import sympy
#x-->z, y---->-x
#y-y0-kx+kx0 =0
class Angleway2():
    def __init__(self, PaX, PaZ, Aa, PbX, PbZ, Ab):
        self.PaX = PaX
        self.PaZ = PaZ
        self.PbX = PbX
        self.PbZ = PbZ
        self.Ka = math.tan(math.radians(float(Aa)))
        self.Kb = math.tan(math.radians(float(Ab)))
    def calc(self):
        self.x0a = int(self.PaZ)
        self.y0a = -int(self.PaX)
        self.x0b = int(self.PbZ)
        self.y0b = -int(self.PbX)
        self.x = sympy.Symbol('x')
        self.y = sympy.Symbol('y')
        self.f1 = -(self.Ka)*self.x+self.y+(self.Ka)*(self.x0a) - (self.y0a)
        self.f2 = -(self.Kb)*self.x+self.y+(self.Kb) * (self.x0b) - (self.y0b)
        self.answer = sympy.solve([self.f1, self.f2], [self.x, self.y])
        print(self.answer)
        print("计算结果为(x,z):",(-int((self.answer[self.y])),int(self.answer[self.x])))
def Input():
            PaX = input("请输入点A坐标X:")
            PaZ = input("请输入点A坐标Z:")
            Aa = input("请输入点A投掷末影珍珠角度")
            PbX = input("请输入点B坐标X:")
            PbZ = input("请输入点B坐标Z:")
            Ab = input("请输入点B投掷末影珍珠角度")
            main = Angleway2(PaX, PaZ, Aa, PbX, PbZ, Ab)
            main.calc()

def Hello():
    print(
    """
    --------------------------------------------------
    末地门坐标计算程序
    github:https://github.com/Friskwml/EnderCalc/
    bilibili:Frisk_wml
                                ----Friskwml 2022/1/27
    --------------------------------------------------
    """)

Hello()
Input()
while True:
    input()