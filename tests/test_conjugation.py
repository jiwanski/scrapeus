import pytest
from .context import ConjugationPage

url = "http://conjugator.reverso.net/conjugation-portuguese.html"

@pytest.fixture(scope="module")
def conjugation_page(chrome_headless):
    return ConjugationPage(chrome_headless)

@pytest.fixture(scope="module", autouse=True)
def fix_geturl(chrome_headless, conjugation_page) -> None:
    chrome_headless.get(url)
    conjugation_page.close_privacy_popup2()


class TestConjugationVerbOfTheDay:
    """Test class for verb of the day."""

    @pytest.fixture(scope='class')
    def fix_verb_of_the_day(self, conjugation_page) -> str:
        verb_of_the_day = conjugation_page.get_verb_of_the_day()
        return verb_of_the_day
 
    def test_verb_of_the_day(self, fix_verb_of_the_day):
        assert fix_verb_of_the_day == 'zangar'

    def test_verb_of_the_day_ending(self, fix_verb_of_the_day):
        assert fix_verb_of_the_day[-2:] in ['ar', 'er']


class TestConjugationPopularVerbs:
    """Test class for popular verbs."""

    popular_verbs_expected = ['ter', 'ser', 'estar', 'poder', 'fazer', 'ir',
                              'haver', 'dizer', 'dar', 'ver', 'saber', 'querer',
                              'ficar', 'passar', 'vir', 'chegar', 'falar', 'partir',
                              'morrer', 'sentir', 'seguir', 'sair', 'perder',
                              'pedir', 'pôr', 'ouvir', 'comprar', 'viver',
                              'acontecer', 'ler']

    @pytest.fixture(scope='class')
    def fix_popular_verbs(self, conjugation_page) -> list:
        popular_verbs = conjugation_page.get_popular_verbs()
        return popular_verbs

    def test_most_popular_verbs_length(self, fix_popular_verbs):
        assert len(fix_popular_verbs) == 30

    def test_most_popular_verbs_content(self, fix_popular_verbs):
        assert set(fix_popular_verbs) == set(self.popular_verbs_expected)

    def test_frequent_verb_in_most_popular(self, fix_popular_verbs):
        assert 'estar' in fix_popular_verbs

    def test_rare_verb_not_in_most_popular(self, fix_popular_verbs):
        assert 'zangar' not in fix_popular_verbs


class TestConjugationMenuMoreProducts:
    """Test class for menu => more products."""

    more_products_expected = ['Synonyms', 'Documents', 'Dictionary', 'Collaborative Dictionary', 'Grammar', 'Expressio', 'Reverso for Business']

    @pytest.fixture(scope='class')
    def fix_more_products(self, conjugation_page) -> list:
        more_products = conjugation_page.get_more_products()
        return more_products

    def test_more_products_titles(self, fix_more_products):
        assert fix_more_products[1:] == self.more_products_expected[1:]  # REVIEW
