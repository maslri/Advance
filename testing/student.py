class Student :
    
    raise_mark = 0.5

    def __init__(self, first_name, last_name, mark) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.mark = mark
    
    def mail(self) :
        return f"{self.first_name}.{self.last_name}@gmail.com"
    
    def full_name(self) :
        return f"{self.first_name} {self.last_name}"
    
    def inc_mark(self) :
        self.mark = float(self.mark + self.raise_mark)

    