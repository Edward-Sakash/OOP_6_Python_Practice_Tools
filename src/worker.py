"""from abc import ABC, abstractmethod
from tool import Laptop


# Complete the class Worker
class Worker:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"\n\n{self.name} starts working:")

    def take_break(self, minutes):
        print(f"\n\n{self.name} takes {minutes} minutes break:")


# Complete this class, so that it would work properly. Implement the missing methods
class Programmer(Worker):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def __str__(self):
        return f"{self.name} codes with {self.language}"

    def work(self):
        super().work()


# Complete the class Janitor.
# Janitor is a subclass of the class Worker
# work(): Janitor fixes pipes with "tool"
# take_break(): Janitor listens to music
class Janitor:
    def __init__(self, name, tool):
        super().__init__(name)
        self.tool = tool

    def __str__(self):
        return f"{self.name} uses {self.tool}"
        """
from abc import ABC, abstractmethod
from tool import Laptop


# Complete the class Worker
class Worker(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def take_break(self, minutes):
        pass


# Complete this class, so that it would work properly. Implement the missing methods
class Programmer(Worker):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def __str__(self):
        return f"{self.name} codes with {self.language}"

    def work(self):
        print(f"{self.name} is coding with {self.language}")

    def take_break(self, minutes):
        print(f"{self.name} takes a {minutes}-minute break")


# Complete the class Janitor.
# Janitor is a subclass of the class Worker
# work(): Janitor fixes pipes with "tool"
# take_break(): Janitor listens to music
class Janitor(Worker):
    def __init__(self, name, tool):
        super().__init__(name)
        self.tool = tool

    def __str__(self):
        return f"{self.name} uses {self.tool}"

    def work(self):
        print(f"{self.name} fixes pipes with {self.tool}")

    def take_break(self, minutes):
        print(f"{self.name} listens to music for {minutes} minutes")


# Test the classes
def main():
    programmer = Programmer("John", "Python")
    janitor = Janitor("Alice", "wrench")

    print(programmer)
    programmer.work()
    programmer.take_break(10)

    print(janitor)
    janitor.work()
    janitor.take_break(15)


if __name__ == "__main__":
    main()








