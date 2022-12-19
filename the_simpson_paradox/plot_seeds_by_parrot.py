from typing import Any
import matplotlib.pyplot as plt
from data_models.day_foraging import DayForaging
from data_models.day import Day
from data_models.parrot import Parrot
from data_models.seed_type import SeedType

# Seed foraging data for three parrots
serialized_data: dict[str, dict[str, Any]] = {
    "You": {
        "Monday": {"Seed Type": "Sunflower", "Number of Seeds": 12},
        "Tuesday": {"Seed Type": "Millet", "Number of Seeds": 5},
    },
    "Polly": {
        "Monday": {"Seed Type": "Millet", "Number of Seeds": 15},
        "Tuesday": {"Seed Type": "Sunflower", "Number of Seeds": 10},
    },
    "Peter": {
        "Monday": {"Seed Type": "Millet", "Number of Seeds": 5},
        "Tuesday": {"Seed Type": "Millet", "Number of Seeds": 17},
    },
}

deserialized_data: dict[Parrot, dict[Day, DayForaging]] = {
    Parrot(parrot): {
        Day(day): DayForaging.parse_obj(day_dictionary)
        for day, day_dictionary in day_dict.items()
    }
    for parrot, day_dict in serialized_data.items()
}


def seeds_by_type(
    data: dict[Parrot, dict[Day, DayForaging]]
) -> dict[SeedType, dict[Parrot, int]]:
    """
    # Function to calculate number of seeds found by seed type
    """
    seeds: dict[SeedType, dict[Parrot, int]] = {}
    for parrot, parrot_dictionary in data.items():
        for day in parrot_dictionary.values():
            day: DayForaging
            seed_type: SeedType = day.seed_type
            seeds[seed_type] = seeds.get(seed_type, {})
            seeds[seed_type][parrot] = seeds[seed_type].get(parrot, 0)
            seeds[seed_type][parrot] += day.number_of_seeds
    return seeds


# Calculate number of seeds found by seed type
seeds: dict[SeedType, dict[Parrot, int]] = seeds_by_type(deserialized_data)

max_y: int = 40

# Create figure and subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Plot bar charts for each seed type
for i, (seed_type, parrots) in enumerate(seeds.items()):
    axs[i].set_title(f"Number of {seed_type} Seeds Found")
    axs[i].set_xlabel("Parrot Name")
    axs[i].set_ylabel("Number of Seeds")
    axs[i].bar(parrots.keys(), parrots.values())
    axs[i].set_ylim([0, 20])
    axs[i].set_yticks(range(0, max_y, 5))

# Calculate total number of seeds found by each parrot
totals: dict[Parrot, int] = {}
for parrot, days in deserialized_data.items():
    totals[parrot] = sum([day.number_of_seeds for day in days.values()])

# Plot bar chart for total seeds found
axs[2].set_title("Total Number of Seeds Found")
axs[2].set_xlabel("Parrot Name")
axs[2].set_ylabel("Number of Seeds")
axs[2].bar(totals.keys(), totals.values())
axs[2].set_ylim([0, 30])
axs[2].set_yticks(range(0, max_y, 5))

plt.show()
