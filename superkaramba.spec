Summary:	Put Karamba applets to the desktop with Python
Name:		superkaramba
Version:	4.12.1
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2+
Url:		http://utils.kde.org/projects/superkaramba
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(qimageblitz)
BuildRequires:	python-devel
Obsoletes:	%{name}-devel < 4.11.0

%description
SuperKaramba is a tool that allows you to easily create interactive
widgets on your KDE desktop.

%files
%{_kde_appsdir}/superkaramba
%{_kde_bindir}/superkaramba
%{_kde_iconsdir}/*/*/apps/superkaramba.*
%{_kde_applicationsdir}/superkaramba.desktop
%{_kde_libdir}/kde4/plasma_package_superkaramba.so
%{_kde_libdir}/kde4/plasma_scriptengine_superkaramba.so
%{_kde_services}/plasma-package-superkaramba.desktop
%{_kde_services}/plasma-scriptengine-superkaramba.desktop
%{_kde_configdir}/superkaramba.knsrc
%{_kde_datadir}/dbus-1/interfaces/org.kde.superkaramba.xml

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
%cmake_kde4
%make

%install
%makeinstall_std -C build

# We don't need it because there are no headers anyway
rm -f %{buildroot}%{_kde_libdir}/libsuperkaramba.so

%changelog
* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.0-1
- New version 4.11.0
- Drop merged in upstream plasma patch
- Drop devel package

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.1-1
- New version 4.9.1

* Thu Aug 30 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.0-1
- New version 4.9.0

* Tue Jul 10 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.0-69.1mib2010.2
+ Revision: 762509
- Backport to 2010.2 for MIB users
- Add python-devel to BuildRequires
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.8.0-1
+ Revision: 762509
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.97-1
+ Revision: 758094
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.95-1
+ Revision: 744573
- New upstream tarball
- New upstream tarball $NEW_VERSION

* Wed Nov 30 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.80-1
+ Revision: 735578
- imported package superkaramba

