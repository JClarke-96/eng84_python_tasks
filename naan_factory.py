class NaanFactory:
    def make_dough(self, item1, item2):
        if item1 == "water" and item2 == "flour":
            return "dough"
        else:
            return

    def bake_dough(self, item1):
        if item1 == "dough":
            return "naan"
        else:
            return

    def run_factory(self, item1, item2):
        item3 = self.make_dough(item1, item2)
        return self.bake_dough(item3)