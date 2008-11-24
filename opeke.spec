Summary:	Playing with virtual bricks
Name:		opeke
Version: 	0.3.1
Release: 	%mkrel 1
Source0: 	http://opeke.noughmad.org/source/%{name}_%{version}_src.tar.gz
License: 	GPLv2+
Group: 		Graphics
Url: 		http://opeke.noughmad.org/wiki/doku.php
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdelibs4-devel

%description 
Opeke is a KDE4 application for building structures with virtual bricks.
It uses OpenGL to render you objects in three dimensions, so you can see
what you've built.

%if %mdkversion < 200900
%post
%update_menus

%postun
%update_menus
%endif

%files
%defattr(-,root,root)
%_kde_bindir/*
%_kde_datadir/applications/kde4/*.desktop
%_kde_appsdir/%name
%_kde_datadir/config.kcfg/*.kcfg

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
rm -rf %{buildroot}
