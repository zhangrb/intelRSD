/*!
 * @brief ManagementController configuration interface.
 *
 * @header{License}
 * @copyright Copyright (c) 2017-2018 Intel Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * @header{Filesystem}
 * @file ipmi/connection_data.cpp
 */

#include "ipmi/connection_data.hpp"

using namespace ipmi;

ConnectionData::ConnectionData(const std::string& _interface_type) : interface_type(_interface_type) { }

ConnectionData::~ConnectionData() { }

const std::string& ConnectionData::get_interface_type() const {
    return interface_type;
}
