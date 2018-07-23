from django.db import models

# class Group(models.Model):
# 	established = models.DateTimeField(auto_now_add=True)
# 	name = models.CharField(max_length=50)
  

  
  
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

    
# q = Question(question_text="Does our proposed solution address the users need?")
# q.save()


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

# # c = Choice(choice_text="You can see yourself using this application")
# # c.save()
# # c = Choice(choice_text="You are likely to recommend this to a friend")
# # c.save()
# # c = Choice(choice_text="I am no longer bored when waiting")
# # c.save()

# attract_level_choice = (('ONE','ONE STAR'),('TWO','TWO STAR'),('THREE','THREE STAR'),('FOUR','FOUR STAR'),('FIVE','FICE STAR'),('ELSE','ELSE'))


class Map(models.Model):
  location = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date add')
  
  ONESTAR='ONE'
  TWOSTAR='TWO'
  THREESTAR='THREE'
  FOURSTAR='FOUR'
  FIVESTAR='FIVE'
  
#   attract_level_choice = (('ONE','ONE STAR'),('TWO','TWO STAR'),('THREE','THREE STAR'),('FOUR','FOUR STAR'),('FIVE','FICE STAR'),('ELSE','ELSE'))
  ATTRACT_LEVEL_CHOICE = (
    (ONESTAR,'⭐️'),
    (TWOSTAR,'⭐️⭐️'),
    (THREESTAR,'⭐️⭐️⭐️'),
    (FOURSTAR,'⭐️⭐️⭐️⭐️'),
    (FIVESTAR,'⭐️⭐️⭐️⭐️⭐️'),
  )
  
  attract_level_choice = models.CharField(
    max_length = 5,
    choices = ATTRACT_LEVEL_CHOICE,
    default = ONESTAR,
  )
  
  
  
#   attract_level = models.ChoiceField()
  comment = models.CharField(max_length=200)
  
  
  
  def __str__(self):
    return self.location
  
#   https://docs.djangoproject.com/en/2.0/ref/forms/fields/#built-in-field-classes