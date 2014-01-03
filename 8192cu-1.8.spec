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

Name:           8192cu
Version:        1.8
Release:        1.0
License:        GPL2
Summary:        Kernel Module for rtl8192cu fixed to compile successfully on new kernels.
Url:            https://github.com/linuxplayground/rtl8192cu-fixes
Group:          Kernel/Drivers
Source:         8192cu-1.8.tgz
Provides:       8192cu.ko
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:	dkms kernel-devel kernel-headers make gcc

%description
This is a port of Realtek's own 8192cu driver for USB Wifi chipsets, ported to kernel 3.11 as ships with Ubuntu 13.10 and openSUSE 13.1.

It was initially based on Timothy Phillips's work as published here: https://code.google.com/p/realtek-8188cus-wireless-drivers-3444749-ubuntu-1304/, though no longer.

The package relies on DKMS to maintain AND install the driver.  Find DKMS for RHEL systems at rpmforge.

%clean
rm -rfv  $RPM_BUILD_ROOT
rm -rfv  $RPM_BUILD_DIR

%prep
%setup -q

%build

%install
#Make sure the build root is empty now.
rm -frv $RPM_BUILD_ROOT/*

#copy important files...
mv -v $RPM_BUILD_DIR/%{name}-%{version}/usr $RPM_BUILD_ROOT/
mv -v $RPM_BUILD_DIR/%{name}-%{version}/etc $RPM_BUILD_ROOT/

%post
dkms add -m 8192cu -v 1.8
dkms build -m 8192cu -v 1.8
dkms install -m 8192cu -v 1.8

%preun
# Remove the dkms module on uninstall
dkms remove -m 8192cu -v 1.8 --all

%files
%defattr(-,root,root)
%doc README.md COPYING
/etc/modprobe.d/blacklist-native-rtl8192.conf
/usr/src/%{name}-%{version}

%changelog

