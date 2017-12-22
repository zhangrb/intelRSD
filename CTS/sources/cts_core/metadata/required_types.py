"""
 * @section LICENSE
 *
 * @copyright
 * Copyright (c) 2017 Intel Corporation
 *
 * @copyright
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * @copyright
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * @copyright
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * @section DESCRIPTION
"""
from cts_core.commons.preconditions import Requirement
from cts_core.metadata.metadata_constants import MetadataConstants2_1, MetadataConstants2_2

RequiredTypes_PSME_2_1 = [
             Requirement(MetadataConstants2_1.CHASSIS, min=1),
             Requirement(MetadataConstants2_1.CHASSIS_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.COMPUTER_SYSTEM, min=1),
             Requirement(MetadataConstants2_1.COMPOSED_SYSTEM_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.ETHERNET_INTERFACE, min=1),
             Requirement(MetadataConstants2_1.EVENT_DESTINATION_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.EVENT_SERVICE, min=1),
             Requirement(MetadataConstants2_1.MANAGER, min=1),
             Requirement(MetadataConstants2_1.MANAGER_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.MEMORY, min=1),
             Requirement(MetadataConstants2_1.MEMORY_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.PROCESSOR, min=1),
             Requirement(MetadataConstants2_1.PROCESSOR_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.SERVICE_ROOT, min=1, max=1),
             Requirement(MetadataConstants2_1.TASK_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.TASK_SERVICE, min=1),
             Requirement(MetadataConstants2_1.VLAN_NETWORK_INTERFACE_COLLECTION, min=1),
        ]

RequiredTypes_Storage_2_1 = [
             Requirement(MetadataConstants2_1.COMPOSED_SYSTEM_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.EVENT_DESTINATION_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.EVENT_SERVICE, min=1),
             Requirement(MetadataConstants2_1.MANAGER, min=1),
             Requirement(MetadataConstants2_1.MANAGER_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.REMOTE_TARGET, min=1),
             Requirement(MetadataConstants2_1.REMOTE_TARGET_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.SERVICE_ROOT, min=1, max=1),
             Requirement(MetadataConstants2_1.STORAGE_SERVICE, min=1),
             Requirement(MetadataConstants2_1.STORAGE_SERVICE_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.TASK_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.TASK_SERVICE, min=1),
        ]

RequiredTypes_PODM_2_1 = [
             Requirement(MetadataConstants2_1.CHASSIS, min=1),
             Requirement(MetadataConstants2_1.CHASSIS_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.COMPOSED_NODE, min=1),
             Requirement(MetadataConstants2_1.COMPOSED_NODE_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.COMPUTER_SYSTEM, min=1),
             Requirement(MetadataConstants2_1.COMPOSED_SYSTEM_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.ETHERNET_INTERFACE, min=1),
             Requirement(MetadataConstants2_1.ETHERNET_SWITCH_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.FABRIC_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.MANAGER, min=1),
             Requirement(MetadataConstants2_1.MANAGER_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.MEMORY, min=1),
             Requirement(MetadataConstants2_1.MEMORY_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.POWER_ZONE_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.PROCESSOR, min=1),
             Requirement(MetadataConstants2_1.PROCESSOR_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.REMOTE_TARGET, min=1),
             Requirement(MetadataConstants2_1.REMOTE_TARGET_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.SERVICE_ROOT, min=1, max=1),
             Requirement(MetadataConstants2_1.THERMAL_ZONE_COLLECTION, min=1),
             Requirement(MetadataConstants2_1.VLAN_NETWORK_INTERFACE_COLLECTION, min=1),
        ]

RequiredTypes_PSME_2_2 = [
             Requirement(MetadataConstants2_2.CHASSIS, min=1),
             Requirement(MetadataConstants2_2.CHASSIS_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.COMPUTER_SYSTEM, min=1, optional=True),
             Requirement(MetadataConstants2_2.COMPOSED_SYSTEM_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.ETHERNET_INTERFACE, min=1),
             Requirement(MetadataConstants2_2.EVENT_DESTINATION_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.EVENT_SERVICE, min=1),
             Requirement(MetadataConstants2_2.MANAGER, min=1),
             Requirement(MetadataConstants2_2.MANAGER_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.MEMORY, min=1, optional=True),
             Requirement(MetadataConstants2_2.MEMORY_COLLECTION, min=1, optional=True),
             Requirement(MetadataConstants2_2.PROCESSOR, min=1, optional=True),
             Requirement(MetadataConstants2_2.PROCESSOR_COLLECTION, min=1, optional=True),
             Requirement(MetadataConstants2_2.SERVICE_ROOT, min=1, max=1),
             Requirement(MetadataConstants2_2.TASK_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.TASK_SERVICE, min=1),
             Requirement(MetadataConstants2_2.VLAN_NETWORK_INTERFACE_COLLECTION, min=1, optional=True),
        ]

RequiredTypes_Storage_2_2 = [
             Requirement(MetadataConstants2_2.COMPOSED_SYSTEM_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.EVENT_DESTINATION_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.EVENT_SERVICE, min=1),
             Requirement(MetadataConstants2_2.MANAGER, min=1),
             Requirement(MetadataConstants2_2.MANAGER_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.REMOTE_TARGET, min=1),
             Requirement(MetadataConstants2_2.REMOTE_TARGET_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.SERVICE_ROOT, min=1, max=1),
             Requirement(MetadataConstants2_2.STORAGE_SERVICE, min=1),
             Requirement(MetadataConstants2_2.STORAGE_SERVICE_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.TASK_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.TASK_SERVICE, min=1),
        ]

RequiredTypes_PODM_2_2 = [
             Requirement(MetadataConstants2_2.CHASSIS, min=1),
             Requirement(MetadataConstants2_2.CHASSIS_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.COMPOSED_NODE, min=1),
             Requirement(MetadataConstants2_2.COMPOSED_NODE_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.COMPUTER_SYSTEM, min=1),
             Requirement(MetadataConstants2_2.COMPOSED_SYSTEM_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.ETHERNET_INTERFACE, min=1),
             Requirement(MetadataConstants2_2.ETHERNET_SWITCH_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.FABRIC_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.MANAGER, min=1),
             Requirement(MetadataConstants2_2.MANAGER_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.MEMORY, min=1),
             Requirement(MetadataConstants2_2.MEMORY_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.POWER_ZONE_COLLECTION, min=1, optional=True),
             Requirement(MetadataConstants2_2.PROCESSOR, min=1),
             Requirement(MetadataConstants2_2.PROCESSOR_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.REMOTE_TARGET, min=1),
             Requirement(MetadataConstants2_2.REMOTE_TARGET_COLLECTION, min=1),
             Requirement(MetadataConstants2_2.SERVICE_ROOT, min=1, max=1),
             Requirement(MetadataConstants2_2.THERMAL_ZONE_COLLECTION, min=1, optional=True),
             Requirement(MetadataConstants2_2.VLAN_NETWORK_INTERFACE_COLLECTION, min=1),
        ]
