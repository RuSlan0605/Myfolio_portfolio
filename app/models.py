from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone

# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

class FinishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()\
        .filter(status=Post.Status.FINISHED)

class Post(models.Model):

    class Status(models.TextChoices):
        FINISHED = 'FSHD', 'FINISHED'
        UNFINISHED = 'UFSHD', 'UNFINISHED'

    title = models.CharField(max_length=250)
    slug = models.SlugField()
    image = models.ImageField(upload_to='images/post', blank=True, null=True)
    descrip  = models.TextField()
    data = models.DateField(auto_now=timezone.now())
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.UNFINISHED)

    objects = models.Manager()
    finished = FinishedManager()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Роли'
        verbose_name = 'Роль'

class ActiveMembManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()\
        .filter(status=Members.Status.ACTIVE_MEMB)
    
class Members(models.Model):

    class Status(models.TextChoices):
        ACTIVE_MEMB = 'AMB', 'ACTIVE_MEMBER'
        INACTIVE_MEMB = 'INMB', 'INACTIVE_MEMBER'

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    slug = models.SlugField()
    email = models.EmailField()
    image = models.ImageField(upload_to='images/members', blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    insta_link = models.URLField(max_length=100, blank=True, null=True)
    git_link = models.URLField(max_length=100, blank=True, null=True)
    tg_link = models.URLField(max_length=100, blank=True, null=True)
    port_link = models.URLField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.INACTIVE_MEMB)

    objects = models.Manager()
    active = ActiveMembManager()

    class Meta:
        verbose_name_plural = 'Мемберы'
        verbose_name = 'Мембер'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'




