"""Music-specific enums
"""


from enum import Enum


class Vocals(Enum):
    """Types of vocals in rock 'n' roll.
    """

    LEAD_VOCALS = 1
    BACKGROUND_VOCALS = 2


class Instrument(Enum):
    """Typical instruments in rock 'n' roll.
    """

    LEAD_GUITAR = 1
    RHYTHM_GUITAR = 2
    BASS = 3
    DRUMS = 4
    PIANO = 5
