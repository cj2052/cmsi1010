class Person:
    def __init__(self, name, mom=None, dad=None, born=None, died=None):
        self.name = name
        self.mom = mom
        self.dad = dad
        self.born = born
        self.died = died

    def life_span(self):
            return f"{self.born or '?'}-{self.died or '?'}"
    
    def __repr__(self):
        """Return a string representation of the person."""
        info = f"{self.name} ({self.life_span()})"
        info += f", Mom: {self.mom.name if self.mom else 'Unknown'}"
        info += f", Dad: {self.dad.name if self.dad else 'Unknown'}"
        return info
    
    def print_family_tree(self, prefix="", level=0):
        """Print the family tree starting from this person."""
        indent = "    " * level
        print(f"{prefix}{self.name} ({self.life_span()})")
        if self.mom:
            self.mom.print_family_tree(f"{indent}mom: ", level + 1)
        if self.dad:
            self.dad.print_family_tree(f"{indent}dad: ", level + 1)


