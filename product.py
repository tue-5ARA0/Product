# Example from Sandi Metz: https://youtu.be/8bZh5LMaSmE
class Product:

    def __init__(self, days_remaining, quality):
        self.days_remaining = days_remaining
        self.quality = quality



    # RED
    # No code

    # GREEN
    # def tick(self):
    #     if self.quality != 0:  # Product is not rotten
    #         if self.days_remaining > 0:  # Fresh product
    #             self.quality -= 1
    #         else:  # Product is past due
    #             self.quality -= 2
    #
    #     self.days_remaining -= 1
    #
    #     return self

    # REFACTOR
    # def tick(self):
    #     self.days_remaining -= 1
    #
    #     # Product is rotten
    #     if self.quality == 0:
    #         return self
    #
    #     # Decrease quality
    #     self.quality -= 1
    #     if self.days_remaining <= 0:  # Product is past due
    #         self.quality -= 1
    #
    #     return self
