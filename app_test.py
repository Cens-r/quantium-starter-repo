from app import app

import os
from webdriver_manager.chrome import ChromeDriverManager

ELEMENT_WAIT_TIMEOUT = 60

# Install chrome driver and add to current session's PATH
chrome_driver = ChromeDriverManager().install()
os.environ["PATH"] += os.pathsep + os.path.dirname(chrome_driver)

def test_header(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element_by_id("graph-title", timeout=ELEMENT_WAIT_TIMEOUT)

def test_graph(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element_by_id("pink-morsel-graph", timeout=ELEMENT_WAIT_TIMEOUT)

def test_region_filter(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element_by_id("region-filter", timeout=ELEMENT_WAIT_TIMEOUT)