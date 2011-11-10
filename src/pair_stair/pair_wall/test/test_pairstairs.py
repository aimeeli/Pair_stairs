import unittest
from django.test import Client
from numpy.lib.function_base import delete
from pair_stair.pair_wall.models import Programmer, Pair

class TestProjectProfile(unittest.TestCase):

    def setUp(self):
        self.client = Client()


    def test_pairstairs_add_programmer_url(self):
        response = self.client.get('/addprogrammer/')
        self.assertEqual(response.status_code, 200)


    def test_should_not_add_duplicated_programmer(self):
        self.client.post('/addprogrammer/',{'programmer': 'Aimee'})
        self.client.post('/addprogrammer/',{'programmer': 'Aimee'})
        self.assertEqual(len(Programmer.objects.filter(name ='Aimee')),1)


    def test_create_pairs_by_add_new_programmer(self):
        Pair.objects.filter(first_member='Aimee').delete()
        Pair.objects.filter(second_member='Aimee').delete()
        Programmer.objects.filter(name='Aimee').delete()
        numbers_of_programmers = len(Programmer.objects.all())
        numbers_of_pairs_before = len(Pair.objects.all())
        self.client.post('/addprogrammer/',{'programmer': 'Aimee'})
        numbers_of_pairs_after = len(Pair.objects.all())
        self.assertEqual(numbers_of_pairs_after, numbers_of_pairs_before + numbers_of_programmers)


    def test_create_pairs_by_add_existing_programmer(self):
        self.client.post('/addprogrammer/',{'programmer': 'Aimee'})
        numbers_of_pairs_before = len(Pair.objects.all())
        self.client.post('/addprogrammer/',{'programmer': 'Aimee'})
        numbers_of_pairs_after = len(Pair.objects.all())
        self.assertEqual(numbers_of_pairs_after, numbers_of_pairs_before)


    def test_add_count(self):
        self.client.post('/addprogrammer/',{'programmer': 'Aaa'})
        self.client.post('/addprogrammer/',{'programmer': 'Bbb'})
        pairs = Pair.objects.all()
        for pair in pairs:
            if pair.first_member == 'Aaa' and pair.second_member == 'Bbb':
                count_before = pair.count
                self.client.post('/addcount/Aaa&Bbb/')
                count_after = pair.count
                self.assertEqual(count_after, count_before + 1)


    def test_pairstairs_display__url(self):
        response = self.client.get('/pairstairs/')
        self.assertEqual(response.status_code, 200)


    def test_pairstairs_display_render_to_right_page(self):
        response = self.client.get('/pairstairs/')
        self.assertIn()


    def test_add_programmer_redirect_to_pairstairs_display(self):
        response = self.client.get('/addprogrammer/', {'programmer': 'Aaa'}, follow=True)
        self.assertRedirects(response, '/pairstairs/')
        self.assertEqual(response.status_code, 302)



        
        




    #def test_pairstairs_display_names(self):
