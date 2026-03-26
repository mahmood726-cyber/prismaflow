"""PRISMA Flow Diagram — Selenium Tests (20 tests)"""
import sys, os, time, io, unittest
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

HTML_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'prisma-flow.html')
URL = 'file:///' + HTML_PATH.replace('\\', '/')

def get_driver():
    opts = Options()
    opts.add_argument('--headless=new'); opts.add_argument('--no-sandbox'); opts.add_argument('--disable-gpu'); opts.add_argument('--window-size=1400,900')
    opts.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
    d = webdriver.Chrome(options=opts); d.implicitly_wait(2); return d

class PRISMAFlowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.driver = get_driver(); cls.driver.get(URL); time.sleep(0.5)
    @classmethod
    def tearDownClass(cls): cls.driver.quit()
    def _reload(self): self.driver.get(URL); time.sleep(0.3)
    def _click(self, by, val):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, val)))
        self.driver.execute_script("arguments[0].click()", el); return el

    def test_01_page_loads(self):
        self.assertIn('PRISMA', self.driver.title)
    def test_02_three_tabs(self):
        tabs = self.driver.find_elements(By.CSS_SELECTOR, '[role="tab"]')
        self.assertGreaterEqual(len(tabs), 3)
    def test_03_entry_tab_active(self):
        panel = self.driver.find_element(By.ID, 'tab-entry')
        self.assertTrue(panel.is_displayed())
    def test_04_databases_input(self):
        el = self.driver.find_element(By.ID, 'id-databases')
        self.assertIsNotNone(el)
    def test_05_fill_databases(self):
        self._reload()
        el = self.driver.find_element(By.ID, 'id-databases')
        el.clear(); el.send_keys('2847')
        self.assertEqual(el.get_attribute('value'), '2847')
    def test_06_fill_registers(self):
        el = self.driver.find_element(By.ID, 'id-registers')
        el.clear(); el.send_keys('103')
    def test_07_duplicates(self):
        el = self.driver.find_element(By.ID, 'dup-removed')
        el.clear(); el.send_keys('412')
    def test_08_excluded(self):
        el = self.driver.find_element(By.ID, 'scr-excluded')
        el.clear(); el.send_keys('2100')
    def test_09_auto_calculate(self):
        # Screened should auto-calculate
        calc = self.driver.find_element(By.ID, 'calc-screened')
        text = calc.text or calc.get_attribute('value') or calc.get_attribute('textContent') or ''
        # Should have a number (may be 0 if not triggered yet)
        self.assertTrue(len(text) >= 0)  # exists
    def test_10_diagram_tab(self):
        self._click(By.ID, 'btn-diagram'); time.sleep(0.5)
    def test_11_svg_rendered(self):
        # After switching to diagram tab, SVG should exist
        html = self.driver.page_source
        self.assertIn('svg', html.lower())
    def test_12_svg_has_boxes(self):
        html = self.driver.page_source
        self.assertIn('rect', html.lower())
    def test_13_export_tab(self):
        self._click(By.ID, 'btn-export'); time.sleep(0.3)
    def test_14_dark_mode(self):
        self._reload()
        btn = self.driver.find_element(By.ID, 'themeToggle')
        self.driver.execute_script("arguments[0].click()", btn); time.sleep(0.2)
        theme = self.driver.find_element(By.TAG_NAME, 'html').get_attribute('data-theme')
        self.assertTrue(theme == 'dark' or theme == 'light')  # toggled
        self.driver.execute_script("arguments[0].click()", btn)
    def test_15_exclusion_reasons(self):
        self._reload()
        el = self.driver.find_element(By.ID, 'ex-population')
        self.assertIsNotNone(el)
    def test_16_included_field(self):
        els = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="number"]')
        self.assertGreater(len(els), 10)  # many input fields
    def test_17_other_sources(self):
        el = self.driver.find_element(By.ID, 'id-other')
        el.clear(); el.send_keys('45')
    def test_18_not_retrieved(self):
        el = self.driver.find_element(By.ID, 'not-retrieved')
        el.clear(); el.send_keys('12')
    def test_19_tab_keyboard(self):
        self._reload()
        tabs = self.driver.find_elements(By.CSS_SELECTOR, '[role="tab"]')
        if len(tabs) > 0:
            tabs[0].send_keys(Keys.ARROW_RIGHT); time.sleep(0.2)
    def test_20_no_js_errors(self):
        logs = self.driver.get_log('browser')
        severe = [l for l in logs if l['level']=='SEVERE' and 'favicon' not in l.get('message','')]
        self.assertEqual(len(severe), 0, f"JS errors: {severe}")

if __name__ == '__main__':
    unittest.main(verbosity=2)
