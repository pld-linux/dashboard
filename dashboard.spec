%define	cvsrel	20040813
Summary:	GNOME Dashboard
Summary(pl):	Dashboard dla GNOME
Name:		dashboard
Version:	0.1
Release:	0.%{cvsrel}.1
License:	GPL?
Group:		Applications/Utilities
Source0:	%{name}-%{version}-%{cvsrel}.tar.bz2
# Source0-md5:	51a6f10eee27d9c452e956c0d8cf20e5
Patch0:		%{name}-BeagleBackend.patch
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
Dashboard to program, który wykonuje ci±g³e, automatyczne
przeszukiwanie osobistej przestrzeni informacyjnej u¿ytkownika, aby
pokazaæ rzeczy w ¿yciu zwi±zane z tym, co robi siê na komputerze.

Podczas czytania poczty elektronicznej, przegl±dania stron WWW,
pisania dokumentów lub rozmawiania z przyjació³mi przez komunikatory
Dashboard próbuje jak najlepiej znale¼æ obiekty powi±zane z bie¿±cymi
czynno¶ciami i wy¶wietliæ je w przyjazny sposób.

%prep
%setup -q
%patch0 -p0

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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
