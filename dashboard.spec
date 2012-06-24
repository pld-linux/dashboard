%define	cvsrel	20030909
Summary:	GNOME Dashboard
Summary(pl):	Dashboard dla GNOME
Name:		dashboard
Version:	0.0
Release:	0.%{cvsrel}.1
License:	GPL?
Group:		Applications/Utilities
Source0:	%{name}-cvs-%{cvsrel}.tar.gz
# Source0-md5:	e9b1c069d01ae5898bc032109df5408f
URL:		http://www.nat.org/dashboard/
BuildRequires:	at-spi-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk-sharp-devel
BuildRequires:	libtool
BuildRequires:	mono
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
%setup -q -n %{name}

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
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
