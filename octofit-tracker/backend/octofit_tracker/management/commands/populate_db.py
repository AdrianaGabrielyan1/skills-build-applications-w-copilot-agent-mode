from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker import models
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        User.objects.all().delete()
        models.Team.objects.all().delete()
        models.Activity.objects.all().delete()
        models.Leaderboard.objects.all().delete()
        models.Workout.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = models.Team.objects.create(name='Marvel')
        dc = models.Team.objects.create(name='DC')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        captain = User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        models.Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        models.Activity.objects.create(user=captain, type='cycle', duration=60, distance=20)
        models.Activity.objects.create(user=batman, type='swim', duration=45, distance=2)
        models.Activity.objects.create(user=superman, type='run', duration=50, distance=10)

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        models.Workout.objects.create(name='Morning Cardio', description='Run and cycle combo', duration=60)
        models.Workout.objects.create(name='Strength Training', description='Weights and resistance', duration=45)

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        models.Leaderboard.objects.create(user=ironman, score=100)
        models.Leaderboard.objects.create(user=superman, score=120)
        models.Leaderboard.objects.create(user=batman, score=90)
        models.Leaderboard.objects.create(user=captain, score=110)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
