from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Items(models.Model):
	#默认表前缀为polls 其他module以此类推
	#有一点比rails on ruby还不习惯,php和rails on ruby都可以不用定义表结构就可以拿到数据
	#这里非要定义表结构吗?假如表模型已经构建,这个非常不舒服
	#提示Field name `name` is not valid for model `Items`. 定义了就正常,未解
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	def __str__(self):
		return self.name