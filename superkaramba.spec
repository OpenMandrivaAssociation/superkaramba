Summary:	Put Karamba applets to the desktop with Python
Name:		superkaramba
Version:	15.08.0
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://utils.kde.org/projects/superkaramba
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(qimageblitz) < 5.0.0
Obsoletes:	%{name}-devel < 4.11.0

%description
SuperKaramba is a tool that allows you to easily create interactive
widgets on your KDE desktop.

%files
%{_datadir}/apps/superkaramba                                                                          
%{_bindir}/superkaramba                                                                                
%{_iconsdir}/*/*/apps/superkaramba.*                                                                   
%{_datadir}/applications/kde4/superkaramba.desktop                                                     
%{_libdir}/kde4/plasma_package_superkaramba.so                                                         
%{_libdir}/kde4/plasma_scriptengine_superkaramba.so                                                    
%{_datadir}/kde4/services/plasma-package-superkaramba.desktop                                          
%{_datadir}/kde4/services/plasma-scriptengine-superkaramba.desktop                                     
%{_datadir}/config/superkaramba.knsrc                                                                  
%{_datadir}/dbus-1/interfaces/org.kde.superkaramba.xml 

#---------------------------------------------

%define libsuperkaramba_major 4
%define libsuperkaramba %mklibname superkaramba %{libsuperkaramba_major}

%package -n %{libsuperkaramba}
Summary:	Runtime library for superkaramba
Group:		System/Libraries

%description -n %{libsuperkaramba}
Runtime library for superkaramba.

%files -n %{libsuperkaramba}
%{_kde_libdir}/libsuperkaramba.so.%{libsuperkaramba_major}*

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

# We don't need it because there are no headers anyway
rm -f %{buildroot}%{_kde_libdir}/libsuperkaramba.so

