Summary:	Digital thermometer using DS1820 1-wire sensors
Summary(pl):	Termometr cyfrowy u¿ywaj±cy czujników Dallasa DS1820
Name:		digitemp
Version:	3.1.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.brianlane.com/linux/%{name}-%{version}.tar.gz
Source1:	http://www.brianlane.com/linux/dthowto.txt
URL:		http://www.brianlane.com/digitemp.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DigiTemp is a simple to use interface to the Dallas Semiconductor
DS18S20, DS1822, and DS18B20 1-wire digital temperature sensors. You
can use DigiTemp in a wide variety of applications, such as heating
control, process monitoring, weather station, indor/outdoor
temperature logging, etc. It includes a couple of useful Perl, Python
and RRD Tool scripts for crating graphs and dynamic signatures.

This package has been compiled for the DS9097 passive 1-wire adapter.

%description -l pl
DigiTemp jest prostym interfejsem dla cyfrowych 1-przewodowych
czujników temperatury: DS18S20, DS1822 i DS18B20 firmy Dallas
Semiconductor. DigiTemp mo¿e mieæ wiele zastosowañ, takich jak
kontrola ogrzewania, monitorowanie procesów, stacje metorologiczne,
wewnêtrzne/zewnêtrzne monitorowanie temperatury. Pakiet zawiera kilka
u¿ytecznych skryptów Perla, Pytona i RRD do tworzenia wykresów i
dynamicznych wpisów.

Ten pakiet zosta³ skompilowany dla pasywnego 1-przewodowego
przetwornika DS9097.

%prep
%setup -q

cp %{SOURCE1} .

%build
%{__make} ds9097

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install digitemp $RPM_BUILD_ROOT%{_bindir}/digitemp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO FAQ perl python rrdb dthowto.txt
%attr(755,root,root) %{_bindir}/digitemp
