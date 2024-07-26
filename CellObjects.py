class CellObject():
    def __init__(self, name, **kwargs):
        self.id:    int = 0  # Update this to update per object of type.
        self.name:  str = name
        self.colour:tuple
        self.style: int

class Prop(CellObject):
    def __init__(self):
        super();
        self.orientation: int = 0;
