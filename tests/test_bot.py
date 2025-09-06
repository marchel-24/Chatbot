import unittest
import sys
import os

# Add the parent directory to the path so we can import the bot module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bot import process_message, reflect_pronouns, find_recipe

class TestRecipeBot(unittest.TestCase):

    def test_01_stir_fry_match(self):
        """Test for a direct stir-fry recipe match."""
        message = "i have chicken, rice, and broccoli"
        response = process_message(message)
        self.assertIn("Stir-fry", response)

    def test_02_pasta_match_case_insensitive(self):
        """Test that matching is case-insensitive."""
        message = "What can I make with PASTA and MARINARA sauce?"
        response = process_message(message)
        self.assertIn("Simple Pasta", response)

    def test_03_omelette_match_with_extra_words(self):
        """Test matching within a longer sentence."""
        message = "i think i have some eggs and maybe some cheese"
        response = process_message(message)
        self.assertIn("Omelette", response)
        
    def test_04_no_recipe_found(self):
        """Test a scenario where no recipe should be found."""
        message = "i have mustard and pickles"
        response = process_message(message)
        self.assertIn("not sure what to make", response)

    def test_05_pronoun_reflection_direct(self):
        """Test the reflect_pronouns function directly."""
        message = "i am looking for my recipe"
        reflection = reflect_pronouns(message)
        self.assertEqual(reflection, "You are looking for your recipe")

    def test_06_pronoun_reflection_in_fallback(self):
        """Test that pronouns are reflected in the fallback message."""
        message = "i have bread and water"
        response = process_message(message)
        self.assertIn("You have bread and water", response)
        
    def test_07_quesadilla_optional_ingredient(self):
        """Test a recipe where one ingredient is optional (chicken)."""
        message = "i have a tortilla and cheese"
        response = process_message(message)
        self.assertIn("Quesadilla", response)

if __name__ == '__main__':
    unittest.main()