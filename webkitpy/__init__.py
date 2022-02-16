# Required for Python to search this directory for module files

# Keep this file free of any code or import statements that could
# cause either an error to occur or a log message to be logged.
# This ensures that calling code can import initialization code from
# webkitpy before any errors or log messages due to code in this file.
# Initialization code can include things like version-checking code and
# logging configuration code.
#
# We do not execute any version-checking code or logging configuration
# code in this file so that callers can opt-in as they want.  This also
# allows different callers to choose different initialization code,
# as necessary.

import os
import platform
import sys

# We always want the real system version
os.environ['SYSTEM_VERSION_COMPAT'] = '0'

libraries = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'libraries')
webkitcorepy_path = os.path.join(libraries, 'webkitcorepy')
if webkitcorepy_path not in sys.path:
    sys.path.insert(0, webkitcorepy_path)
import webkitcorepy

if sys.platform == 'darwin':
    is_root = not os.getuid()
    does_own_libraries = os.stat(libraries).st_uid == os.getuid()
    if (is_root or not does_own_libraries):
        libraries = os.path.expanduser('~/Library/webkitpy')

from webkitcorepy import AutoInstall, Package, Version
AutoInstall.set_directory(os.path.join(libraries, 'autoinstalled', 'python-{}-{}'.format(sys.version_info[0], platform.machine())))


import webkitscmpy
