from django.db import models

class ExamScore(models.Model):


	allsubject = (( 'Math','Math'),
				  ('Sci','Sci'),
				  ('Art','Art'),
				  ('Eng','Eng'),
				  ('Physics','Physics'),
				  ('Bio','Bio'))

	student_subject = models.CharField(max_length=200, choices=allsubject, default='01')
	student_name = models.CharField(max_length=200)
	score = models.IntegerField(default=0)


	def __str__(self):
		return self.student_name +'-'+ self.student_subject +'-'+ str(self.score)
