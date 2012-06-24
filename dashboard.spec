%define	cvsrel	20040620
Summary:	GNOME Dashboard
Summary(pl):	Dashboard dla GNOME
Name:		dashboard
Version:	0.1
Release:	0.%{cvsrel}.1
License:	GPL?
Group:		Applications/Utilities
Source0:	%{name}-%{version}-%{cvsrel}.tar.bz2
# Source0-md5:	2a4e39c567dd59d5bfc3ba5cbba5a65f
URL:		http://www.nat.org/dashboard/
BuildRequires:	at-spi-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	beagle-devel
BuildRequires:	dotnet-evolution-sharp-devel >= 0.3
BuildRequires:	dotnet-gtk-sharp-devel >= 0.10
BuildRequires:	libtool
BuildRequires:	mono
BuildRequires:	mono-csharp
BuildRequires:	pkgconfig
Requires:	beagle
Requires:	dotnet-evolution-sharp >= 0.3
Requires:	dotnet-gtk-sharp >= 0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The dashboard is a piece of software which performs a continous,
automatic search of your personal information space to show you things
in your life that are related to whatever you happen to be doing with
your computer at the time.

While you read email, browse the web, write a document, or talk to
your friends on IM, dashboard does its best to proactively find
objects that are relevant to your current activity, and to display
them in a friendly way.

%description -l pl
Dashboard to program, kt�ry wykonuje ci�g�e, automatyczne
przeszukiwanie osobistej przestrzeni informacyjnej u�ytkownika, aby
pokaza� rzeczy w �yciu zwi�zane z tym, co robi si� na komputerze.

Podczas czytania poczty elektronicznej, przegl�dania stron WWW,
pisania dokument�w lub rozmawiania z przyjaci�mi przez komunikatory
Dashboard pr�buje jak najlepiej znale�� obiekty powi�zane z bie��cymi
czynno�ciami i wy�wietli� je w przyjazny spos�b.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING MAINTAINERS README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
