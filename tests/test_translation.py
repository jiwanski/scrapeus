import pytest
from .context import TranslationPage

url = "https://context.reverso.net/translation/portuguese-english/enxergo"

@pytest.fixture(scope="class")
def translation_page(chrome_headless):
    return TranslationPage(chrome_headless)

@pytest.fixture(scope="module", autouse=True)
def fix_geturl(chrome_headless) -> None:
    chrome_headless.get(url)


class TestTranslation:
    """Test class for translation page."""

    expected_highlight = 'rgba(255, 255, 185, 1)'

    def test_every_verb_in_examples_is_highlighted(self, translation_page):
        """Example sentences should contain highlighted verb.
           This should pass."""
        atrs = translation_page.get_highlight_css_for_verb()
        assert atrs == {self.expected_highlight}

    @pytest.mark.skip
    def test_verify_toolbar_on_hover_example_src(self, translation_page):  # TODO
        """Hover over example (source) should display pronunciation icon.
           This should pass."""
        pass

    def test_verb_in_search_field(self, translation_page):
        """Search field should contain the verb from page title.
           This should pass."""
        verb_from_title = translation_page.get_verb_from_title()
        verb_in_search_field = translation_page.get_verb_in_search_field()
        assert verb_in_search_field == verb_from_title
