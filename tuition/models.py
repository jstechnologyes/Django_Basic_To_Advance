from django.db import models
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

class PostManager(models.Manager):
    def sorted(self,tile):
        return self.order_by(tile)
    def less_than(self,size):
        return self.filter(salary__lt=size)

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    content=models.TextField()
    def __str__(self):
        return self.name

class Subject(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Class_in(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    CATEGORY={
        ('Teacher','Teacher'),
        ('Student','Student'),
    }
    MEDIUM={
        ('Bangla','Bangla'),
        ('English','English'),
        ('Korea','Korea'),
        ('Japanis','Japanis'),
        ('China','China'),

    }
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    id= models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    slug=models.CharField(max_length=100, default=title)
    email=models.EmailField()
    salary=models.FloatField()
    details=models.TextField()
    stats=models.BooleanField()
    category=models.CharField(max_length=100,choices=CATEGORY)
    created_ad=models.DateTimeField(default=now)
    image=models.ImageField(default='default.jpg',upload_to='tuition/images')
    medium=MultiSelectField(max_length=100,max_choices=5,choices=MEDIUM,default='Bangla')
    subject=models.ManyToManyField(Subject,related_name='subject')
    class_in=models.ManyToManyField(Class_in,related_name='class_in')
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    # def __str__(self):
    #     return self.title+ "by: "+self.user.username
    def get_subject_list(self):
        sub=self.subject.all()
        subjects=""
        for s in sub:
            subjects=subjects+ str(s.name)+ ","
        return subjects
    def get_class_list(self):
        sub=self.class_in.all()
        subjects=""
        for s in sub:
            subjects=subjects+ str(s.name)+ ","
        return subjects
    def ProperCase(self):
        return self.title.title()
    def details_short(self):
        details_words=self.details.split(' ')
        if len(details_words)>10:
            return  ' '.join(details_words[:10])+ "....."
        else:
            return self.details
    objects= models.Manager()
    items=PostManager()





