import pandas as pd
from datetime import datetime
import pytz

def ch_now(rounding='s'):
    """
    Returns current Swiss time as pandas timestamp without timezone suffix
    Args:
        rounding (str): Time unit to floor to (e.g. 'min', 'H', 's'). Default is 's' (second)
    """
    swiss_tz = pytz.timezone('Europe/Zurich')
    current_time = datetime.now(swiss_tz)
    ts = pd.Timestamp(current_time.replace(tzinfo=None))
    
    return ts.floor(rounding) if rounding else ts

from streamlit.components.v1 import html

def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)