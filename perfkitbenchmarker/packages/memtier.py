# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Module containing iperf installation and cleanup functions."""

GIT_REPO = 'git clone git://github.com/RedisLabs/memtier_benchmark'
GIT_TAG = '1.2.0'
LIBEVENT_TAR = 'libevent-2.0.21-stable.tar.gz'
LIBEVENT_URL = 'https://github.com/downloads/libevent/libevent/' + LIBEVENT_TAR
LIBEVENT_DIR = 'pkb/libevent-2.0.21-stable'
MEMTIER_DIR = 'pkb/memtier_benchmark'
APT_PACKAGES = ('autoconf automake libpcre3-dev '
                'libevent-dev pkg-config zlib-dev')
YUM_PACKAGES = 'zlib-devel pcre-devel libmemcached-devel'


def YumInstall(vm):
  """Installs the iperf package on the VM."""
  vm.Install('build_tools')
  vm.InstallPackages(YUM_PACKAGES)
  vm.RemoteCommand('wget {0} -P pkb'.format(LIBEVENT_URL))
  vm.RemoteCommand('cd {0} && ./configure && sudo make install'.format(LIBEVENT_DIR )
  vm.RemoteCommand('git clone {0} {1}'.format(GIT_REPO, MEMTIER_DIR))
  vm.RemoteCommand('cd {0} && autoreconf -ivf && ./configure && make')


def AptInstall(vm):
  """Installs the iperf package on the VM."""
  vm.Install('build_tools')
  vm.InstallPackages(APT_PACKAGES)
  vm.RemoteCommand('git clone {0} {1}'.format(GIT_REPO, MEMTIER_DIR))
  vm.RemoteCommand('cd {0} && autoreconf -ivf && ./configure && make')
