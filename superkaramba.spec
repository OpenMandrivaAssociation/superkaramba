Name:    superkaramba
Summary: Put Karamba applets to the desktop with Python
Version: 4.7.97
Release: 1
Group:   Graphical desktop/KDE
License: LGPLv2
URL:     http://www.kde.org/
Source:  ftp://ftp.kde.org/pub/kde/stable/%version/src/%{name}-%version.tar.bz2

BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: qimageblitz-devel

%description
SuperKaramba is a tool that allows you to easily create interactive
widgets on your KDE desktop.

%files
%_kde_appsdir/superkaramba
%_kde_bindir/superkaramba
%_kde_iconsdir/*/*/apps/superkaramba.*
%_kde_datadir/applications/kde4/superkaramba.desktop
%_kde_libdir/kde4/plasma_package_superkaramba.so
%_kde_libdir/kde4/plasma_scriptengine_superkaramba.so
%_kde_datadir/kde4/services/plasma-package-superkaramba.desktop
%_kde_datadir/kde4/services/plasma-scriptengine-superkaramba.desktop
%_kde_datadir/config/superkaramba.knsrc
%_kde_datadir/dbus-1/interfaces/org.kde.superkaramba.xml

#---------------------------------------------

%define libsuperkaramba_major 4
%define libsuperkaramba %mklibname superkaramba %{libsuperkaramba_major}

%package -n %libsuperkaramba
Summary: Runtime library for superkaramba
Group: System/Libraries
URL: http://utils.kde.org/projects/superkaramba

%description -n %libsuperkaramba
Runtime library for superkaramba

%files -n %libsuperkaramba
%_kde_libdir/libsuperkaramba.so.%{libsuperkaramba_major}*

#---------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: %libsuperkaramba = %EVRD

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%_kde_libdir/libsuperkaramba.so

#----------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
	
%make

%install
%makeinstall_std -C build

