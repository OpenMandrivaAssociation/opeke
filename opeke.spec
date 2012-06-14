Summary:	Playing with virtual bricks
Name:		opeke
Version: 	0.4
Release: 	5
Source0: 	http://downloads.sourceforge.net/opeke/Opeke-%version.tar.gz
License: 	GPLv2+
Group: 		Graphics
Url: 		http://opeke.sourceforge.net/

BuildRequires: 	kdelibs4-devel
BuildRequires:	ogre-devel

%description 
Opeke is a KDE4 application for building structures with virtual bricks.
It uses OpenGL to render you objects in three dimensions, so you can see
what you've built.

%prep
%setup -qn Opeke

%build
%cmake_kde4
%make

%install
%{makeinstall_std} -C build

%files
%_kde_bindir/*
%_kde_datadir/applications/kde4/*.desktop
%_kde_appsdir/%{name}
%_kde_datadir/config.kcfg/*.kcfg
