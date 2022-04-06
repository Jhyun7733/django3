from django.db import models
from acc.models import User
# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="writer")
    content = models.TextField()
    likey = models.ManyToManyField(User, blank=True, related_name="likey")
    pubdate = models.DateTimeField()

    def __str__(self):
        return f"{self.subject} written by {self.writer}"
    # 마이그레이션 전까지 

    def summary(self):
        if len(self.content) > 50:
            return f"{self.content[:50]} ..."
        return self.content

    def hot(self):
        if self.likey.count() > 1:
            return True
        return False



class Reply(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    replyer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.board}_{self.replyer}"