import csv

from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Player


class PlayerAPITest(TestCase):
    def setUp(self):
        # user = User.objects.create_user('test_user', 'test@example.com', 'password')
        # self.client.force_login(user)
        self.client = APIClient()

    def test_valid_csv_data(self):
        """Ensure the initial provided data can be validated."""
        with open('Player.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                response = self.client.post('/api/players/', row, format='json')
                self.assertEqual(response.status_code, 201, f'row: {row}\nError: {response.data}')

        players_len = 19370
        self.assertEqual(Player.objects.count(), players_len)
        response = self.client.get('/api/players/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), players_len)

    def test_create_player(self):
        player_id = 'player1'
        name_last = 'Cohen'
        response = self.client.post('/api/players/', {'playerID': player_id, 'nameLast': name_last}, format='json')

        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(Player.objects.count(), 1)
        response = self.client.get(f'/api/players/{player_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['playerID'], player_id)
        self.assertEqual(response.data['nameLast'], name_last)

    def test_get_player(self):
        player = Player.objects.create(playerID='player1', nameLast='Cohen')

        response = self.client.get(f'/api/players/{player.playerID}/')
        self.assertEqual(response.status_code, 200)

        # Assert that the response data matches the created player
        self.assertEqual(response.data['playerID'], player.playerID)
        self.assertEqual(response.data['nameLast'], player.nameLast)

    def test_patch_player(self):
        player = Player.objects.create(playerID='player1', nameLast='Cohen')

        response = self.client.patch(f'/api/players/{player.playerID}/', {'birthYear': 30}, format='json')

        self.assertEqual(response.status_code, 200)

        # Refresh the player instance from the database
        player.refresh_from_db()
        # Assert that the player's age has been updated
        self.assertEqual(player.birthYear, 30)

    def test_delete_player(self):
        player = Player.objects.create(playerID='player1', nameLast='Cohen')

        response = self.client.delete(f'/api/players/{player.playerID}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Player.objects.count(), 0)
