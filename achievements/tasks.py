from achievements.utils import check_achievement_plain
from celery.task import task


@task
def check_achievement_task(sender, user, key, *args, **kwargs):
    check_achievement_plain(sender, user, key, *args, **kwargs)

