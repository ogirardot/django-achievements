import importlib     
from achievements.models import Achievement, UserAchievement         
from achievements.signals import achievement_registered, achievement_unlocked

def get_user_score(user):      
    """ Compute the score of a given user taking into account their Achievement's bonuses"""
    return UserAchievement.objects.filter(user=user).aggregate(score=Sum('achievement__bonus'))     

def check_achievement_plain(sender, user, key, *args, **kwargs):
    obj = Achievement.objects.get(key=key)
    if evaluate_achievement_callback(user, obj, *args, **kwargs):
        (user_ach, created) = UserAchievement.objects.get_or_create(achievement=obj, user=user)
        if created:
            achievement_unlocked.send(sender=sender, user=user, achievement=obj, *args, **kwargs)
                                        
def evaluate_achievement_callback(user, obj, *args, **kwargs):
    """ 
    Evaluate callback of the achievement in order to determine if achievement has been
    unlocked by user.
    """            
    achievement = get_callback_object(obj.callback)
    # call the evaluate fonction :
    return achievement().evaluate(user, *args, **kwargs)
                                                   
def construct_callback(obj): 
    return "%s.%s" % (obj.__module__, obj.__name__)

def get_callback_object(ref):
    module = ".".join(ref.split(".")[:-1])
    class_name = ref.split(".")[-1]    
    m = importlib.import_module(module)
    return eval('m.%s' % class_name)
