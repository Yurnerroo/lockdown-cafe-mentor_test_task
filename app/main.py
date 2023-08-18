from app.cafe import Cafe
from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError,
)

EVERYONE_VACCINATED_MSG = "All friends should be vaccinated"


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    friends_without_masks: int = 0

    for friend in friends:
        try:
            cafe.visit_cafe(visitor=friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return EVERYONE_VACCINATED_MSG
        except NotWearingMaskError:
            friends_without_masks += 1

    if friends_without_masks:
        return f"Friends should buy {friends_without_masks} masks"
    else:
        return f"Friends can go to {cafe.name}"
