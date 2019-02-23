from django.contrib import admin


# Register your models here.

from .models import StudyProgram
from .models import Professor
from .models import Committee
from .models import AssessmentResult
from. models import AUN

admin.site.register(StudyProgram)
admin.site.register(Professor)
admin.site.register(Committee)
admin.site.register(AssessmentResult)
admin.site.register(AUN)