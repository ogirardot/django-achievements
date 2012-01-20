
from django.conf import settings

from .models import Achievement
from .utils import check_achievement_plain


class AutoAchievementChecker(object):
  def process_response(self, request, response):
    if not getattr(request, 'user'):
      return response

    user = request.user
    try:
      methods = [i.lower() for i in settings.ACHIEVEMENT_MIDDLEWARE_REQUEST_METHODS]
    except:
      methods = []

    if request.method.lower() in methods and user and user.is_authenticated():
      for obj in Achievement.objects.all().order_by('bonus'):
        check_achievement_plain(self, user, obj.key)

    return response

