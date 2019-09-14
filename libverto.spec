#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libverto
Version  : 0.3.0
Release  : 5
URL      : https://github.com/latchset/libverto/releases/download/0.3.0/libverto-0.3.0.tar.gz
Source0  : https://github.com/latchset/libverto/releases/download/0.3.0/libverto-0.3.0.tar.gz
Summary  : Event loop abstraction interface
Group    : Development/Tools
License  : MIT
Requires: libverto-lib = %{version}-%{release}
Requires: libverto-license = %{version}-%{release}
BuildRequires : libev-dev
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libevent)

%description
libverto
===============================================================================

%package dev
Summary: dev components for the libverto package.
Group: Development
Requires: libverto-lib = %{version}-%{release}
Provides: libverto-devel = %{version}-%{release}
Requires: libverto = %{version}-%{release}

%description dev
dev components for the libverto package.


%package lib
Summary: lib components for the libverto package.
Group: Libraries
Requires: libverto-license = %{version}-%{release}

%description lib
lib components for the libverto package.


%package license
Summary: license components for the libverto package.
Group: Default

%description license
license components for the libverto package.


%prep
%setup -q -n libverto-0.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568247618
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --with-tevent=no
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1568247618
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libverto
cp COPYING %{buildroot}/usr/share/package-licenses/libverto/COPYING
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/include/verto.h
rm -f %{buildroot}/usr/include/verto-module.h
rm -f %{buildroot}/usr/lib64/libverto.so

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/verto-glib.h
/usr/include/verto-libevent.h
/usr/lib64/libverto-glib.so
/usr/lib64/libverto-libevent.so
/usr/lib64/pkgconfig/libverto-glib.pc
/usr/lib64/pkgconfig/libverto-libevent.pc
/usr/lib64/pkgconfig/libverto.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libverto-glib.so.1
/usr/lib64/libverto-glib.so.1.0.0
/usr/lib64/libverto-libevent.so.1
/usr/lib64/libverto-libevent.so.1.0.0
/usr/lib64/libverto.so.1
/usr/lib64/libverto.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libverto/COPYING
