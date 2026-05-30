def ft_count_harvest_recursive() -> None:
    days = int(input('How many days left until harvest ? '))

    def helpharvest(i):
        if i == days:
            print('Day ', i)
            print('Harvest time!')
            return
        else:
            print('Day ', i)
            helpharvest(i + 1)
    helpharvest(1)
