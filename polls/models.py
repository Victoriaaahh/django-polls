# from django.db import models


# class Usuario(models.Model):
#     idQuestionário = models.IntegerField(primary_key=True, unique=True)
#     Nome = models.CharField(max_length=45)
#     Nickname = models.CharField(max_length=45, unique=True)
#     Avatar = models.CharField(max_length=45, null=True)

#     def __str__(self):
#         return self.Nome


# class Quiz(models.Model):
#     idQuiz = models.IntegerField(primary_key=True, auto_created=True)
#     Titulo = models.CharField(max_length=45)
#     Descrição = models.CharField(max_length=45, null=True)
#     Data_criacao = models.CharField(max_length=45)
#     Usuario_idQuestionário = models.ForeignKey(
#         Usuario, on_delete=models.CASCADE, related_name='quizzes')

#     def __str__(self):
#         return self.Titulo


# class Hashtag(models.Model):
#     idHashtag = models.IntegerField(primary_key=True)
#     tag = models.CharField(max_length=45, null=True)

#     def __str__(self):
#         return self.tag


# class Hashtag_has_Quiz(models.Model):
#     Hashtag_idHashtag = models.ForeignKey(
#         Hashtag, on_delete=models.CASCADE)
#     Quiz_idQuiz = models.ForeignKey(
#         Quiz, on_delete=models.CASCADE, related_name='hashtags')

#     def __str__(self):
#         return f"Hashtag: {self.Hashtag_idHashtag}, Quiz: {self.Quiz_idQuiz}"

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)