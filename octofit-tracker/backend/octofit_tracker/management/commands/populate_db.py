from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', universe='Marvel')
        dc = Team.objects.create(name='DC', universe='DC')

        # Users (superheroes)
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True)
        spiderman = User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='Marvel', is_superhero=True)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='DC', is_superhero=True)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='DC', is_superhero=True)

        # Activities
        Activity.objects.create(user='Iron Man', type='Running', duration=30, date='2026-01-01')
        Activity.objects.create(user='Spider-Man', type='Cycling', duration=45, date='2026-01-02')
        Activity.objects.create(user='Batman', type='Swimming', duration=60, date='2026-01-03')
        Activity.objects.create(user='Superman', type='Flying', duration=120, date='2026-01-04')

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=150)
        Leaderboard.objects.create(team='DC', points=180)

        # Workouts
        Workout.objects.create(name='Push Ups', description='Do 20 push ups', difficulty='Easy')
        Workout.objects.create(name='Pull Ups', description='Do 10 pull ups', difficulty='Medium')
        Workout.objects.create(name='Flying Sprints', description='Sprint while flying', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
