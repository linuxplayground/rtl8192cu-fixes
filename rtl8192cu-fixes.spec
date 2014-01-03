#
# spec file for rtl8192cu-fixes
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           rtl8192cu-fixes
Version:        1.8
Release:        1.0
License:        GPL2
Summary:        Kernel Module for rtl8192cu fixed to compile successfully on new kernels.
Url:            https://github.com/linuxplayground/rtl8192cu-fixes
Group:          Kernel/Drivers
Source:         rtl8192cu-fixes-1.8.tgz
BuildRequires:  kernel-desktop-devel kernel-devel make gcc
Provides:       8192cu.ko
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       dkms
%define kernelversion $(uname -r)

%description
This is a port of Realtek's own 8192cu driver for USB Wifi chipsets, ported to kernel 3.11 as ships with Ubuntu 13.10 and openSUSE 13.1.

It was initially based on Timothy Phillips's work as published here: https://code.google.com/p/realtek-8188cus-wireless-drivers-3444749-ubuntu-1304/, though no longer.

This package will place the driver in /lib/modules/%{kernelversion}/%{name}
%prep
%setup -q

%build
make %{?_smp_mflags}

%install
%make_install

%post
cp -vr %{build_root}/%{name} /usr/src/%{name}
dkms add /usr/src/%{name}
depmod -a
modprobe 8192cu
cp -v %{build_root}/%{name}/blacklist-native-rtl8192.conf /etc/modprobe.d/

%files
%defattr(-,root,root)
%doc README.md COPYING

%changelog

