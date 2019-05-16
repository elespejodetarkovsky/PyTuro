from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects")
    link = models.URLField(null=True, blank=True)  # <=====
    linkImg = models.URLField(null= True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]
        
    def __str__(self):
        return self.title
    
class Cursos(models.Model):
    codi_curs = models.CharField(max_length=200, )
    nom = models.CharField(max_length=200, null = False)
    estat = models.IntegerField()
    data_inici = models.DateField()
    data_fi = models.DateField()
    hores = models.IntegerField()
    
    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ["-nom"]
        
    def __str__(self):
        return self.codi_curs
    
class Inscripciones(models.Model):
    codi_curs = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    orden = models.IntegerField()
    nom = models.CharField(max_length=200, null = False)
    apellido = models.CharField(max_length=200, null = False)
    dni =  models.CharField(max_length=20, null = False)
    telefono =  models.CharField(max_length=20, null = True)
    correo = models.CharField(max_length=200, null = True)
    sexo = models.CharField(max_length=20, null = False)
    edad = models.IntegerField()
    
    class Meta:
        ordering = ["-codi_curs"]
        
    def __str__(self):
        return self.nom