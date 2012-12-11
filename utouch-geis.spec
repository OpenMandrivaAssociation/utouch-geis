#define Werror_cflags %nil
%define major 1
%define libname %mklibname  %{name} %{major}
%define develname   %mklibname  %{name} -d
 
Name:           utouch-geis
Version:        2.2.1
Release:        2
License:        GPLv2,LGPLv3
Summary:        Gesture engine interface and support
Url:            http://launchpad.net/utouch-geis
Group:          System/Libraries
Source0:		%{name}-%{version}.tar.gz
Patch0:			utouch-geis-2.2.0-remove-Werror.patch
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(utouch-grail)
BuildRequires:  pkgconfig(utouch-frame)
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(xi)
BuildRequires:  python-pyxml
 
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
%setup -q
%patch0 -p1
 
%build
autoreconf -fi
%configure2_5x \
  --disable-static
%make
 
%install
%makeinstall_std
 
 
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

