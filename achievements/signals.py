from django.dispatch import Signal

# An achievement has been registered :
achievement_registered = Signal(providing_args=["achievement_class"])
# A user has unlocked an achievement.
achievement_unlocked = Signal(providing_args=["user", "achievement"])
