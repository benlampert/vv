from django.contrib import admin
from evaluations.models import Evaluations, Section, Question, VendorEvaluation, Answer, MT_VendorAnswers
# Register your models here.

#admin.site.register(Evaluations)
admin.site.register(Section)
admin.site.register(Question)
#admin.site.register(VendorEvaluation)
#admin.site.register(Answer)
admin.site.register(MT_VendorAnswers)

