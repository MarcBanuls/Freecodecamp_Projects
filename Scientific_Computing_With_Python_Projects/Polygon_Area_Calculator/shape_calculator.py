class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        area = 0
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = 0
        perimeter = 2 * self.width + 2 * self.height
        return perimeter
    
    def get_diagonal(self):
        diagonal = 0
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        count_height = self.height
        picture = ""
        while count_height > 0:
            picture += ("*" * self.width) + "\n"
            count_height -= 1
        return picture
        
    def get_amount_inside(self, shape):
        original_area = self.get_area()
        new_area = shape.get_area()
        counter = 0
        while original_area >= new_area:
            original_area -= new_area
            counter += 1
        return counter
    
    def __str__(self):
        string = ""
        string += f"Rectangle(width={self.width}, height={self.height})"
        return string

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self,side, side)
        self.side = side
        
    def set_side(self, side):
        self.side = side
        
    # Method overriding to satisfy square class:
    def set_width(self, width):
        self.width = width
        self.height = width
        self.side = width
        
    def set_height(self, height):
        self.width = height
        self.height = height
        self.side = height
    
    def get_picture(self):
        picture = ""
        count_side = self.side
        while count_side > 0:
            picture += ("*" * self.side) + "\n"
            count_side -= 1
        return picture
        
    def __str__(self):
        string = ""
        string += f"Square(side={self.side})"
        return string
