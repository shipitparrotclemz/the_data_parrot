from pydantic import BaseModel, Field

from data_models.seed_type import SeedType


class DayForaging(BaseModel):
    seed_type: SeedType = Field(alias="Seed Type")
    number_of_seeds: int = Field(alias="Number of Seeds")
