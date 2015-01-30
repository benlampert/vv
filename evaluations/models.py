from django.db import models
from vendors.models import Vendor
# Create your models here.
class Section(models.Model):
    section_name = models.CharField(max_length=100)
    section_order = models.IntegerField()
    
    class Meta:
        ordering = ["section_order"]
    
    def __str__(self):
        return "[%s] %s" % (self.section_order, self.section_name or "")


class Evaluations(models.Model):
    eval_name = models.CharField(max_length=100, default="New Evaluation")
    added_sections = models.ManyToManyField(Section)
    
    def __str__(self):
        return self.eval_name
    
    class Meta:
        verbose_name_plural = "Evaluations"
        verbose_name = "Evaluation"

    
class Question(models.Model):
    eval_question_name= models.CharField(max_length=300)
    eval_section = models.ForeignKey(Section, related_name="questions")
    for_marketing = models.BooleanField('For Marketing', default=0)
    question_order = models.IntegerField()

    class Meta:
        ordering = ["question_order"]
        unique_together = [[ "eval_section", "question_order"]]
  
    def __str__(self):
        return "%s" % (self.eval_question_name)

class VendorEvaluation(models.Model):
    vendor = models.ForeignKey(Vendor, related_name="evaluation")
    evaluation = models.ForeignKey(Evaluations, related_name="vendors_evaluation")
    #created = models.DateTimeField('Date Created', default=timezone.now())
    
    def __str__(self):
        return "%s : %s" % (self.vendor, self.evaluation)
        
    class Meta:
        ordering = ["vendor"]

class Answer(models.Model):
    answer = models.FloatField(default=0.0)
    question = models.ForeignKey(Question, related_name="questions")
    vendor_evaluation = models.ForeignKey(VendorEvaluation, related_name="vendor_eval")

    def __str__(self):
        return "%s : %s : %s" % (self.vendor_evaluation, self.question, self.answer)

class MT_VendorAnswers(models.Model):
    answer = models.FloatField(default=0.0)
    question = models.ForeignKey(Question, related_name="question")
    vendor = models.ForeignKey(Vendor, related_name="vendor")

    def __str__(self):
        return "%s : %s : %s" % (self.vendor, self.question, self.answer) 
        
    class Meta:
        verbose_name_plural = "Vendor Eval Answers"
        verbose_name = "Vendor Eval Answer"