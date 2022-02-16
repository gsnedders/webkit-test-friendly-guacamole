# Copyright (C) 2020, 2021 Apple Inc. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1.  Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2.  Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY APPLE INC. AND ITS CONTRIBUTORS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL APPLE INC. OR ITS CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import logging
import platform
import sys

from logging import NullHandler

log = logging.getLogger('webkitcorepy')
log.addHandler(NullHandler())

from webkitcorepy.version import Version
from webkitcorepy.string_utils import BytesIO, StringIO, UnicodeIO, unicode
from webkitcorepy.timeout import Timeout
from webkitcorepy.subprocess_utils import TimeoutExpired, CompletedProcess, run
from webkitcorepy.output_capture import LoggerCapture, OutputCapture, OutputDuplicate
from webkitcorepy.task_pool import TaskPool
from webkitcorepy.terminal import Terminal
from webkitcorepy.environment import Environment
from webkitcorepy.credentials import credentials, delete_credentials
from webkitcorepy.measure_time import MeasureTime
from webkitcorepy.nested_fuzzy_dict import NestedFuzzyDict
from webkitcorepy.call_by_need import CallByNeed
from webkitcorepy.editor import Editor
from webkitcorepy.file_lock import FileLock

version = Version(0, 13, 0)

from webkitcorepy.autoinstall import Package, AutoInstall

name = 'webkitcorepy'
