Summary:	Digital thermometer using DS1820 1-wire sensors
Summary(pl.UTF-8):	Termometr cyfrowy używający czujników Dallasa DS1820
Name:		digitemp
Version:	3.5.0
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://www.digitemp.com/software/linux/%{name}-%{version}.tar.gz
# Source0-md5:	72bda9c8a66b017aa969c19dedb3225b
Source1:	http://www.brianlane.com/linux/dthowto.txt
# Source1-md5:	313824e3f211c1983971913ce785f4f7
Source2:	DS9097_Schematic.gif
Patch0:		%{name}-opt.patch
URL:		http://www.digitemp.com/
BuildRequires:	libusb-devel
BuildRequires:	lockdev-devel
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DigiTemp is a simple to use interface to the Dallas Semiconductor
DS18S20, DS1822, and DS18B20 1-wire digital temperature sensors. You
can use DigiTemp in a wide variety of applications, such as heating
control, process monitoring, weather station, indor/outdoor
temperature logging, etc. It includes a couple of useful Perl, Python
and RRD Tool scripts for crating graphs and dynamic signatures.

%description -l pl.UTF-8
DigiTemp jest prostym interfejsem dla cyfrowych 1-przewodowych
czujników temperatury: DS18S20, DS1822 i DS18B20 firmy Dallas
Semiconductor. DigiTemp może mieć wiele zastosowań, takich jak
kontrola ogrzewania, monitorowanie procesów, stacje meteorologiczne,
wewnętrzne/zewnętrzne monitorowanie temperatury. Pakiet zawiera kilka
użytecznych skryptów Perla, Pytona i RRD do tworzenia wykresów i
dynamicznych wpisów.

%prep
%setup -q
%patch0 -p1

cp %{SOURCE1} %{SOURCE2} .

%build
export OPT="%{rpmcflags}"
%{__make} ds9097
%{__make} ds9097u
%{__make} ds2490

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version},%{_mandir}/man1}

install digitemp_DS* $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -rf perl python rrdb $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS DS9097_S* FAQ README TODO dthowto.txt
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man1/*
