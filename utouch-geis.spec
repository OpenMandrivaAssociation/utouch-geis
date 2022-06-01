#define Werror_cflags %nil
%define _disable_ld_no_undefined 1
%define major 1
%define libname %mklibname  %{name} %{major}
%define develname   %mklibname  %{name} -d
%define oname geis
 
Name:           utouch-geis
Version:        2.2.17
Release:        1
License:        GPLv2,LGPLv3
Summary:        Gesture engine interface and support
Url:            http://launchpad.net/geis
Group:          System/Libraries
Source0:        https://launchpad.net/geis/trunk/%{version}/+download/%{oname}-%{version}.tar.xz
Patch1:		geis-2.2.14-configureac.patch
Patch2:		geis-2.2.17-gcc7.patch

BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(grail)
BuildRequires:  pkgconfig(frame)
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xi)
 
%description
GEIS is a library for applications and toolkit programmers which provides a
consistent platform independent interface for any system-wide input gesture
recognition mechanism.
 
%package -n %{libname}
Summary:        Gesture engine interface and support
Group:          System/Libraries
 
%description -n %{libname}
GEIS is a library for applications and toolkit programmers which provides a
consistent platform independent interface for any system-wide input gesture
recognition mechanism.

%package -n python-geis
Summary:		Python bindings for GEIS
Group:			Development/Python
 
%description -n python-geis
This package provides the python bindings for GEIS.

%package -n %{develname}
Summary:        Development files for the GEIS interface implementation
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
 
%description -n %{develname}
GEIS is a library for applications and toolkit programmers which provides a
consistent platform independent interface for any system-wide input gesture
recognition mechanism.
 
%prep
%autosetup -n %{oname}-%{version} -p1
 
%build
export CC=gcc
export CXX=g++
autoreconf -fi
%configure \
  --disable-static
%make_build
 
%install
%make_install
 
 
%files
%doc ChangeLog README COPYING
%{_bindir}/geis-server
%{_bindir}/geistest
%{_bindir}/geisview
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop
%{_datadir}/geisview/*.ui
%{_datadir}/pixmaps/*.xpm
 
%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n python-geis
%{_bindir}/pygeis
%{py_puresitedir}/geis*
%{py_platsitedir}/*.so
 
%files -n %{develname}
%{_includedir}/geis/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

