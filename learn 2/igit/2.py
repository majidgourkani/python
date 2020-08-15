class first:
    def name(self): return self._doAction('name')

    def _doAction(self , x):
        if x in self.test:
            return self.test[x]
        else:
            return "the {} dont have {}".format(self._res(), x)

    def _res(self):
        return self.__class__.__name__.lower()


class majid(first):
    test = dict(
    name = "majidGourkani"
    )

class milad(first):
    test = dict(
    fname = "miladGourkani"
    )

def getName(ns):
    print(ns.name())

def main():
    mg = majid()
    lg = milad()

    print("majid calss name:")
    getName(mg)
    print("milad calss name:")
    getName(lg)

if __name__ == "__main__": main()
