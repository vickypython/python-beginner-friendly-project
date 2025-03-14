from django.db import models
class Publication(models.Model):
    title=models.CharField(max_length=30)
    class Meta:
        ordering=["title"]
        def __str__(self):
           
           return self.title

class Article(models.Model):
    headline=models.CharField(max_length=50)
    publications=models.ManyToManyField(Publication)
    reporter=models.OneToOneField()
    class Meta:
        ordering=["headline"]

        def __str__(self):
            return self.headline

p1=Publication(title='learnign django the hard way')
p1.save()
p2=Publication(title='learnign python the hard way')
p2.save()
a1=Article(headline="chapter one")
a1.save()
a1.publications.add(p1)
print(a1)
class Simplemiddleware():
    def __init__(self,get_response):
        self.get_response=get_response
        #code for configureation
    def __call__(self,request):
        #code before view are called
        response=self.get_response(request)
        #code after view are code ofr request and response
        return response
