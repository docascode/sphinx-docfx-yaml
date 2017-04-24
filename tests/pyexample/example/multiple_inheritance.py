class Subject(object):

    def __init__(self):
        self.observers = []
        super(Subject, self).__init__()

    def register(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.notify()


class ArbitraryWidget(object):

    def __init__(self):
        # 'methalop' is what Ali G suggests as an alternative for the word
        # 'bread' to Noam Chomsky
        self.methalop = 5
        super(ArbitraryWidget, self).__init__()

    def do_something(self):
        self.methalop += 1


class ObservableArbitraryWidget(ArbitraryWidget, Subject):

    def __init__(self):
        super(ObservableArbitraryWidget, self).__init__()


