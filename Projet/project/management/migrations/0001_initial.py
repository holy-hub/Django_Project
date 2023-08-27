# Generated by Django 4.2.1 on 2023-08-26 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nom', models.CharField(max_length=100)),
                ('sexe', models.CharField(choices=[('feminin', 'Feminin'), ('masculin', 'Masculin')], default=None, max_length=100)),
                ('password', models.CharField(default=1234, max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_naissance', models.DateField()),
                ('numero_utilisateur', models.CharField(max_length=20, unique=True)),
                ('role', models.CharField(choices=[('etudiant', 'Étudiant'), ('enseignant', 'Enseignant'), ('administrateur', 'Administrateur')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('matiere', models.CharField(default='Python', max_length=200)),
                ('fichier', models.FileField(upload_to='Downloads/task/')),
                ('statut', models.CharField(choices=[('en_cours', 'En cours'), ('soumis', 'Soumis'), ('corrigé', 'Corrigé'), ('traité', 'Traité'), ('archivé', 'Archivé')], max_length=20)),
                ('etudiant', models.ForeignKey(limit_choices_to={'role': 'etudiant'}, on_delete=django.db.models.deletion.CASCADE, to='management.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Soumission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichier_soumission', models.FileField(upload_to='Downloads/submission/')),
                ('date_soumission', models.DateTimeField(auto_now_add=True)),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.cours')),
                ('etudiant', models.ForeignKey(limit_choices_to={'role': 'etudiant'}, on_delete=django.db.models.deletion.CASCADE, to='management.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=200)),
                ('matiere', models.CharField(max_length=200)),
                ('fichier_projet', models.FileField(upload_to='projets/')),
                ('statut', models.CharField(choices=[('en_cours', 'En cours'), ('soumis', 'Soumis'), ('corrigé', 'Corrigé'), ('traite', 'Traité'), ('archive', 'A0rchivé')], max_length=20)),
                ('notes_avis', models.TextField(blank=True)),
                ('instructeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='NoteTravail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('avis', models.TextField()),
                ('soumission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='management.soumission')),
            ],
        ),
        migrations.AddField(
            model_name='cours',
            name='enseignant',
            field=models.ForeignKey(limit_choices_to={'role': 'enseignant'}, on_delete=django.db.models.deletion.CASCADE, related_name='cours_enseignes', to='management.utilisateur'),
        ),
        migrations.AddField(
            model_name='cours',
            name='etudiant',
            field=models.ForeignKey(default=None, limit_choices_to={'role': 'etudiant'}, on_delete=django.db.models.deletion.CASCADE, to='management.utilisateur'),
        ),
    ]
