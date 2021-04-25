from enum import Enum

class EXPOSABLE_EVENTS(Enum):
    MISSING_DATA_ALL = "missing_redis_data::all"
    MISSING_DATA_SINGLE = "missing_redis_data::single"
