from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    tecnologias = models.TextField(help_text="Liste as tecnologias utilizadas separadas por vírgula.")
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome
