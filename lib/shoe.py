#!/usr/bin/env python3


class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

        

    def cobble(self):
        print("The shoe is repaired.")
        self.condition = "New"
