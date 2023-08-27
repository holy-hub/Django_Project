from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UtilisateurManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class Utilisateur(AbstractBaseUser):
    ROLES_CHOICES = [
        ('etudiant', 'Étudiant'),
        ('enseignant', 'Enseignant'),
        ('administrateur', 'Administrateur'),
    ]
    sexe = [
        ('feminin', 'Feminin'),
        ('masculin', 'Masculin'),
    ]

    nom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=100,choices=sexe,default=None)
    password = models.CharField(max_length=100,default=1234)
    USERNAME_FIELD = 'numero_utilisateur'
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    numero_utilisateur = models.CharField(max_length=20,unique=True)
    role = models.CharField(max_length=20, choices=ROLES_CHOICES)
    objects = UtilisateurManager()

    def __str__(self):
        return f"{self.prenom} {self.nom}"

# Module de chargement/téléchargement
class Projet(models.Model):
    STATUT_CHOICES = [ ('en_cours', 'En cours'), ('soumis', 'Soumis'), ('corrigé', 'Corrigé'), ('traite', 'Traité'), ('archive', 'A0rchivé'), ]

    intitule = models.CharField(max_length=200)
    matiere = models.CharField(max_length=200)
    fichier_projet = models.FileField(upload_to='projets/')
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
    instructeur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    notes_avis = models.TextField(blank=True)

class Tache(models.Model):
    STATUT_CHOICES = [ ('en_cours', 'En cours'), ('soumis', 'Soumis'), ('corrigé', 'Corrigé'), ('traité', 'Traité'), ('archivé',  'Archivé'), ]

    etudiant = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, limit_choices_to={'role': 'etudiant'})
    titre = models.CharField(max_length=200)
    matiere = models.CharField(max_length=200, default="Python")
    fichier = models.FileField(upload_to='Downloads/task/')
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)

    def __str__(self):
        return self.titre


class Cours(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    enseignant = models.ForeignKey(
        Utilisateur,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'enseignant'},
        related_name='cours_enseignes'  # Nouveau nom pour l'attribut reverse
    )
    etudiant = models.ForeignKey(
        Utilisateur,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'etudiant'},
        default=None  # Spécifiez la valeur par défaut ici
    )
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return self.titre

class Soumission(models.Model):
    etudiant = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, limit_choices_to={'role': 'etudiant'})
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    fichier_soumission = models.FileField(upload_to='Downloads/submission/')
    date_soumission = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Soumission de {self.etudiant} pour le cours {self.cours}"
    
class NoteTravail(models.Model):
    soumission = models.OneToOneField(Soumission, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    avis = models.TextField()

    def __str__(self):
        return f"Note pour {self.soumission.etudiant} - Cours : {self.soumission.cours.titre}"
