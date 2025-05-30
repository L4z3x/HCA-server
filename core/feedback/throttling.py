from rest_framework.throttling import AnonRateThrottle


class CustomAnonThrottle(AnonRateThrottle):
    rate = "5/min"  # 5 per minute
