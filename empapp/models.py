from django.db import models

class Role(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return(self.name)


class department(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=50)
    def __str__(self):
        return(self.name)



class employee(models.Model):
    firstname=models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dept=models.ForeignKey(department,on_delete=models.CASCADE)
    salary=models.IntegerField()
    bonus=models.IntegerField()
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField()
    hiredate=models.DateTimeField()
    def __str__(self):
        return " %s %s " %(self.firstname , self.lastname )




