Summary:	Playing with virtual bricks
Name:		opeke
Version: 	0.4
Release: 	%mkrel 2
Source0: 	http://downloads.sourceforge.net/opeke/Opeke-%version.tar.gz
License: 	GPLv2+
Group: 		Graphics
Url: 		http://opeke.sourceforge.net/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdelibs4-devel
BuildRequires:	ogre-devel

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
%setup -q -n Opeke

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
rm -rf %{buildroot}
