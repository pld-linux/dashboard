%define cvsrel 20030909
Summary:	Gnome Dashboard
Name:		dashboard
Version:	0.0
Release:	0.%{cvsrel}.1
License:	GPL?
Group:		Applications/Utilities
Source0:	%{name}-cvs-%{cvsrel}.tar.gz
# Source0-md5:	e9b1c069d01ae5898bc032109df5408f
URL:		http://www.nat.org/dashboard/
BuildRequires:	mono
BuildRequires:	gtk-sharp-devel
BuildRequires:	at-spi-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnome Dashboard

%prep
%setup -q -n %{name}

%build
%{__aclocal}
%{__autoconf}
%{__libtoolize}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
