from dataclasses import dataclass


@dataclass
class LonelySlipper:
    color: str
    size: int
    days_alone: int
    hope: int

    def complain(self):
        print(f"{self.color} тапочок {self.size} розміру сумує без пари вже {self.days_alone} дн.")

    def search(self):
        self.hope -= 10
        print(f"{self.color} тапочок шукав пару під диваном, але знайшов лише пил. Надія: {self.hope}%")

    def meet_dog(self):
        print(f"{self.color} тапочок зустрів пса. Тепер він ще й мокрий.")

    def dream(self):
        print(f"{self.color} тапочок мріє, що пара чекає його в пральній машині.")


def main():
    slipper1 = LonelySlipper("Рожевий", 37, 3, 80)
    slipper2 = LonelySlipper("Коричневий", 44, 365, 30)
    slipper3 = LonelySlipper("Білий", 42, 12, 50)

    for slipper in (slipper1, slipper2, slipper3):
        slipper.complain()
        slipper.search()
        slipper.meet_dog()
        slipper.dream()
        print()


if __name__ == "__main__":
    main()