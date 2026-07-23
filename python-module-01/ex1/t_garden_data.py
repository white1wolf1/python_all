# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   t_garden_data.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: asobolev <asobolev@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/03 15:34:29 by asobolev           #+#    #+#             #
#   Updated: 2026/06/03 16:52:59 by asobolev          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm,", end="")
        print(f" {self.days} days old")


def main() -> None:
    plant1: Plant = Plant("Rose", 25, 30)
    plant2: Plant = Plant("Sunflower", 80, 45)
    plant3: Plant = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    main()
