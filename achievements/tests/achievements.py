from django.test import TestCase   
    
class AchievementClassesCheckTest(TestCase):

    def test_check_achievement_class(self):
        class AchievementDef(object):
            name = "Username achivement"
            key = "username"
            description = "Handles when a user changes its username"
            bonus = 15.0
            def evaluate(self):
                return True
        
        self.assertEqual([], check_achievement_class(AchievementDef))
                                                                                 

        def test_check_missing_attributes(self):
            class AchievementDef(object):
                name = "Username achivement"
                description = "Handles when a user changes its username"
                bonus = 15.0
                def evaluate(self):
                    return True

            self.assertEqual([('key', False)], check_achievement_class(AchievementDef))
                                                                             
        
        def test_check_achievement_class(self):
            class AchievementDef(object):
                name = "Username achivement"
                key = "username"
                bonus = 15.0
                def evaluate(self):
                    return True

            self.assertEqual([('description', False)], check_achievement_class(AchievementDef))