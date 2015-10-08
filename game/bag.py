class Bag:
    """Defines the bag, or the inventory of the player character, is possible to save 12 items in the bag"""
    def __init__(self):
            self.slots = {"slot" + str(i) : None for i in range(1,6)} # This is a dict comprehension

    def get_item(self, slot):
        if self.slots.has_key(slot): return self.slots[slot]
        return True

    def add_item(self, item, slot):
        if self.slots.has_key(slot): self.slots[slot] = item

    def remove_item(self, item, slot):
        if self.slots.has_key(slot): self.slots[slot] = None
