#!/usr/bin/env python
#
# Copyright (C) 2016 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os

from .network_handler import NetworkHandler
from .project_handler import ProjectHandler
from .dynamips_device_handler import DynamipsDeviceHandler
from .dynamips_vm_handler import DynamipsVMHandler
from .qemu_handler import QEMUHandler
from .virtualbox_handler import VirtualBoxHandler
from .vpcs_handler import VPCSHandler
from .vmware_handler import VMwareHandler
from .config_handler import ConfigHandler
from .file_handler import FileHandler
from .version_handler import VersionHandler


if sys.platform.startswith("linux") or hasattr(sys, "_called_from_test") or os.environ.get("PYTEST_BUILD_DOCUMENTATION") == "1":
    # IOU runs only on Linux but testsuite work on UNIX platform
    if not sys.platform.startswith("win"):
        from .iou_handler import IOUHandler
        from .docker_handler import DockerHandler
