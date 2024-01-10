# mypy {name file python}

x: int = 2
y: float = 4.4
z: bool = True
k: None = None
l: str = "Hello"
m: list = [2,4,6]

def my_function(x: int,y: int) -> int:
    return x**y

my_function(2,10)

def my_function2(x: int,y: int) -> None:
    print(f"{x} + {y} = {x+y}")
    
my_function2(2,6)

x2 = [[2,3,4],[5,4,3],[9,8,1]]

x3: list[list[int]] = [[2,3,4],[5,4,3],[9,8,1]]

x5 = {"A":"a"}

x6: dict[str,str] = {"A":"a"}

x7: list[list[int]] = [[2,3,4],[5,6,7]]
y2: list[list[int]] = [[1,4,8],[3,6,1,3,4]]
z2: list[list[int]] = [[6,4,1,2,3],[0,5,1,1,0]]

Type1 = list[list[int]]

x8: Type1 = [[1,4,8],[3,6,1,3,4]]

from typing import Optional, Any, Sequence, Callable

def my_function3(x: Optional[int] = 2):
    pass

def my_function4(x: Any):
    return "Nothing"

def my_function5(x: Sequence):
    pass

def myfunction6(x:int, y:float) -> str:
    return "hello"


def myfunction7(func: Callable[[int, float], str]) -> None:
    pass