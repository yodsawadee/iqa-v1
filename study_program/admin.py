from django.contrib import admin


# Register your models here.

from .models import StudyProgram
from .models import Professor
from .models import Committee
from .models import AssessmentResult
from .models import AUN
from .models import AvailableTime
from .models import Issue
from .models import Comment

admin.site.register(StudyProgram)
admin.site.register(Professor)
admin.site.register(Committee)
admin.site.register(AssessmentResult)
admin.site.register(AUN)
admin.site.register(AvailableTime)
admin.site.register(Issue)
admin.site.register(Comment)