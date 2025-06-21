from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']

        # Populate users
        users = [
            {'username': 'john_doe', 'email': 'john_doe@example.com', 'password': 'password123'},
            {'username': 'jane_doe', 'email': 'jane_doe@example.com', 'password': 'password123'},
        ]
        # Adding test data for users, teams, activities, leaderboard, and workouts
        for user in users:
            db.users.update_one({'email': user['email']}, {'$set': user}, upsert=True)

        # Populate teams
        teams = [
            {'team_id': 1, 'name': 'Team Alpha', 'members': ['john_doe', 'jane_doe']},
        ]
        for team in teams:
            db.teams.update_one({'name': team['name']}, {'$set': team}, upsert=True)

        # Populate activities
        activities = [
            {'user': 'john_doe', 'activity_type': 'Running', 'duration': '01:00:00'},
            {'user': 'jane_doe', 'activity_type': 'Cycling', 'duration': '02:00:00'},
        ]
        for activity in activities:
            db.activities.update_one({'user': activity['user'], 'activity_type': activity['activity_type']}, {'$set': activity}, upsert=True)

        # Populate leaderboard
        leaderboard = [
            {'leaderboard_id': 1, 'user': 'john_doe', 'score': 100},
            {'leaderboard_id': 2, 'user': 'jane_doe', 'score': 150},
        ]
        for entry in leaderboard:
            db.leaderboard.update_one({'leaderboard_id': entry['leaderboard_id']}, {'$set': entry}, upsert=True)

        # Populate workouts
        workouts = [
            {'workout_id': 1, 'name': 'Morning Run', 'description': 'A quick run to start the day'},
            {'workout_id': 2, 'name': 'Evening Yoga', 'description': 'Relaxing yoga session'},
        ]
        for workout in workouts:
            db.workouts.update_one({'workout_id': workout['workout_id']}, {'$set': workout}, upsert=True)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
