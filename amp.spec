Summary:	Command-line mp3 player based on smpeg
Summary(pl):	Odtwarzacz mp3 wywo³ywany z linii poleceñ
Name:		amp
Version:	0.7.6
Release:	2
Group:		Applications/Sound
License:	distributable (see README)
Vendor: 	Tomislav Uzelac <tuzelac@rasip.fer.hr>
# working URL: ftp://ftp.clara.net/pub/unix/Audio/%{name}-%{version}.tar.gz
# or: http://www.go.dlr.de/fresh/linux/src/%{name}-%{version}.tgz
Source0:	ftp://ftp.rasip.fer.hr/pub/mpeg/%{name}-%{version}.tgz
# Source0-md5:	c12a27ac84b417bdac3330c3aa366122
Patch0:		%{name}-debian.patch
Patch1:		%{name}-ppc.patch
URL:		http://www.rasip.fer.hr/research/compress/algorithms/tools/amp/amp.html
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This audio program will play MPEG (I/II) Audio Layer II & III files
in realtime. This release of amp has support for the Sajber Jukebox
and POSIX 1.b realtime extensions. 

%description -l pl
Program odtwarzaj±cy w czasie rzeczywistym pliki MPEG (I/II) Audio
Layer II i III. Ta wersja ampa ma obs³ugê Sajber Jukebox i rozszerzeñ
czasu rzeczywistego POSIX 1.b.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install amp $RPM_BUILD_ROOT%{_bindir}
install amp.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* BUGS CHANGES README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
