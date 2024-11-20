class VaccineError(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)