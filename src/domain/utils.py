from datetime import datetime
from pytz import timezone


def kst_now():
    """Get the current time in KST."""
    return datetime.now(timezone("Asia/Seoul"))
