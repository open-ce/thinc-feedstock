# *****************************************************************
#
# Licensed Materials - Property of IBM
#
# (C) Copyright IBM Corp. 2020. All Rights Reserved.
#
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with IBM Corp.
#
# *****************************************************************

import os
import sys
import pytest
import thinc

PACKAGE_DIR = os.path.abspath(os.path.dirname(thinc.__file__))
sys.exit(pytest.main([PACKAGE_DIR]))
