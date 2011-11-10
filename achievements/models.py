import importlib, inspect
from django.core.exceptions import ImproperlyConfigured   
from django.contrib.auth.models import User
from django.conf import settings 
from django.db import models        

from appconf import AppConf         

def check_achievement_class(cls):
    return [attribute for attribute in ['name', 'key', 'description', 'bonus', 'evaluate'] if not hasattr(cls, attribute)]      

def load_classes(classes=settings.ACHIEVEMENT_CLASSES, *args, **kwargs):  
	# if we're called during south migration ignore every app 
	# until we get notified that the achievements app 
	# was properly loaded
    if 'app' in kwargs and kwargs['app'] != 'achievements':
		return
    from achievements.engine import engine
    for achievement_module in classes:
        try:
            module = importlib.import_module(achievement_module)
            clses = [cls for name, cls in inspect.getmembers(module) if inspect.isclass(cls) and name.endswith('Achievement')]
            for cl in clses:
                errors = check_achievement_class(cl)
                if errors:
                    raise ImproperlyConfigured("Achievement class '%s' in '%s' has missing attributes : %s" %(cl.__name__, module.__name__, ",".join(errors)))
                else:
                    print "Registering achievement class %s..." % (cl)
                    engine.register_achievement(cl)
        except ImproperlyConfigured:
            raise
        except Exception, exc:
            raise ImproperlyConfigured("ACHIEVEMENT_CLASSES attribute must be set properly for them to be loaded into the engine : %s" % exc)   
    
                     

class Achievement(models.Model):
    """ These objects are what people are earning when contributing """  
    name = models.CharField(max_length=75)
    key = models.CharField(max_length=75, unique=True)
    description = models.TextField(null=True, blank=True)
    bonus = models.IntegerField(default=0)
    callback = models.TextField()  
    def __unicode__(self):
        return "Achievement(%s, %s)"% (self.name, self.bonus)  

class UserAchievement(models.Model):
    user = models.ForeignKey(User)
    achievement = models.ForeignKey(Achievement)     
    registered_at = models.DateTimeField(auto_now_add=True)  
                                
class AchievementEngineConf(AppConf): 
    """ Configuration class used by Django AppConf to ease the setup"""
    USE_CELERY = False
    CLASSES = []     
    
    class Meta:
        prefix = 'achievement'

    def configure_classes(self, value):
        pass  

# connect to the end of the syncdb command signal to reload achievements at that time.
if 'south' in settings.INSTALLED_APPS:
    from south.signals import post_migrate
    post_migrate.connect(load_classes)
else:
    from django.db.models.signals import post_syncdb
    post_syncdb.connect(load_classes)
