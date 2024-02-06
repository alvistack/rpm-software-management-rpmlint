# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: rpmlint
Epoch: 100
Version: 2.4.0
Release: 0%{?dist}
BuildArch: noarch
Summary: Tool for checking common errors in RPM packages
License: GPLv2+
URL: https://github.com/rpm-software-management/rpmlint/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: bash
Requires: binutils
Requires: bzip2
Requires: cpio
Requires: dash
Requires: desktop-file-utils
Requires: devscripts
Requires: file
Requires: findutils
Requires: hunspell-cs
Requires: hunspell-en-US
Requires: libappstream-glib
Requires: python3-enchant
Requires: python3-importlib-metadata
Requires: python3-magic
Requires: python3-pybeam
Requires: python3-pyxdg
Requires: python3-rpm
Requires: python3-tomli
Requires: python3-tomli-w
Requires: python3-zstandard
Requires: rpm-build

%description
rpmlint is a tool for checking common errors in RPM packages. Binary
and source packages as well as spec files can be checked.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}%{_sysconfdir}/xdg/rpmlint
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150000
cp -rfT configs/openSUSE %{buildroot}%{_sysconfdir}/xdg/rpmlint
%endif
%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
cp -rfT configs/Fedora %{buildroot}%{_sysconfdir}/xdg/rpmlint
%endif
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%files
%license COPYING
%dir %{_sysconfdir}/xdg/rpmlint
%{_bindir}/*
%{_sysconfdir}/xdg/rpmlint/*
%{python3_sitelib}/*

%changelog
