from django.conf import settings                                                
from achievements.models import Achievement, UserAchievement                    
from achievements.utils import construct_callback, check_achievement_plain
from achievements.signals import achievement_registered, achievement_unlocked
            
class AchievementEngine(object):
    def register_achievement(self, cls):  
        """ Register a new achievement into the engine and database"""    
        (obj, created) = Achievement.objects.get_or_create(key=cls.key,  defaults={
            'name' : cls.name,
            'description' : cls.description, 
            'bonus' : cls.bonus, 
            'callback': construct_callback(cls)})
        if not created:
            # update the object if key didn't change :
            obj.name = cls.name
            obj.description = cls.description
            obj.bonus = cls.bonus
            obj.callback = construct_callback(cls) 
            obj.save()
        achievement_registered.send(sender=self, achievement_class=cls)      
                   
    def check_achievement(self, user, key, *args, **kwargs):
        if user and user.is_authenticated(): 
            if settings.ACHIEVEMENT_USE_CELERY: 
                # do not try to import if celery is not defined
                from achievements.tasks import check_achievement_task
                check_achievement_task.delay(self, user, key, *args, **kwargs)
            else:     
                check_achievement_plain(self, user, key, *args, **kwargs)
        else:
            print "trying to check an achievement for an un-logged user"
                                                     
# create the engine    
engine = AchievementEngine()

        