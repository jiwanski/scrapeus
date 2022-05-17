import pytest
from selenium.webdriver.common.by import By
from .context import VerbPage

url = "https://conjugator.reverso.net/conjugation-portuguese-verb-encetar.html"

@pytest.fixture(scope="module")
def verb_page(chrome_headless):
    return VerbPage(chrome_headless)

@pytest.fixture(scope="module", autouse=True)
def fix_geturl(chrome_headless) -> None:
    chrome_headless.get(url)


class TestVerb:
    """Test class for verb page."""

    def test_verb_in_search_field(self, verb_page):
        """Search field should contain the verb from page title.
           This should pass."""
        verb_from_title = verb_page.get_verb_from_title()
        verb_in_search_field = verb_page.get_verb_in_search_field()
        assert verb_in_search_field == verb_from_title

    def test_infinitive_flag(self, verb_page):
        """Flag before inifitive should match current language.
           This should pass."""
        atr = verb_page.get_infinitive_flag_url()
        assert 'pt.svg' in atr   

    def test_print_function_call_in_printable_page(self, verb_page):  
        """Printable popup should have call to print window.
           This should pass."""
        atr = verb_page.get_body_onload()
        assert atr == 'setTimeout(function(){window.print();}, 500);'

    @pytest.mark.skip
    def test_print_button(self):  # TODO
        """Print button should open print popup.
           This should pass."""
        pass

    @pytest.mark.skip
    def test_tooltip_over_(self):  # TODO
        """Tooltip over infinitive should have text from tooltip attribute.
           This should pass."""
        pass

    @pytest.mark.skip
    def test_print_function(self, verb_page):  # FIXME
        """Print popup should load print function.
           This should pass."""
        verb_page.open_print_popup()
        verb_page.switch_to_print_window()
        atr = verb_page.get_base_attribute()
        assert atr == 'chrome://print'
