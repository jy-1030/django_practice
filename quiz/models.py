from django.db import models


# Create your models here.
# 寫資料儲存的model

class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    """
    on_delete=models.CASCADE -> 當Question被刪除 Choice也會同步刪除
    Charfiled表示該欄位為字串格式

    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    score = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text


