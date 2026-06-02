def ft_count_harvest_recursive() -> None:
    days = int(input('How many days left until harvest ? '))

    def HelpHarvest(i):
        if i == days:
            print('Day ', i)
            print('Harvest time!')
            return
        else:
            print('Day ', i)
            HelpHarvest(i + 1)
    HelpHarvest(1)
