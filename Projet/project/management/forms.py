from django import forms
from .models import *

class CoursForm(forms.ModelForm):
    etudiant = forms.ModelChoiceField(queryset=Utilisateur.objects.filter(role='etudiant'))
    class Meta:
        model = Cours
        fields = ['titre', 'description','enseignant','etudiant','date_debut', 'date_fin']

class AutoriseForm(forms.ModelForm):
    etudiant = forms.ModelChoiceField(queryset=Utilisateur.objects.filter(role='etudiant'))
    class Meta:
        model = Tache
        fields = ['etudiant','titre','matiere','fichier', 'statut']

class SoumissionForm(forms.ModelForm):
    class Meta:
        model = Soumission
        fields = ['fichier_soumission']

class NoteTravailForm(forms.ModelForm):
    class Meta:
        model = NoteTravail
        fields = ['note', 'avis']
