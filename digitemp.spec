Summary:	Digital thermometer using DS1820 1-wire sensors
Summary(pl):	Termometr cyfrowy u�ywaj�cy czujnik�w Dallasa DS1820
Name:		digitemp
Version:	3.3.2
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://www.digitemp.com/software/linux/%{name}-%{version}.tar.gz
# Source0-md5:	0b6cfb36d198767836de54d9fb11bbdb
Source1:	http://www.brianlane.com/linux/dthowto.txt
# Source1-md5:	31f67f7dba103988d10478566599cb3e
Patch0:		%{name}-opt.patch
URL:		http://www.digitemp.com/
BuildRequires:  libusb-devel
BuildRequires:	lockdev
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DigiTemp is a simple to use interface to the Dallas Semiconductor
DS18S20, DS1822, and DS18B20 1-wire digital temperature sensors. You
can use DigiTemp in a wide variety of applications, such as heating
control, process monitoring, weather station, indor/outdoor
temperature logging, etc. It includes a couple of useful Perl, Python
and RRD Tool scripts for crating graphs and dynamic signatures.

%description -l pl
DigiTemp jest prostym interfejsem dla cyfrowych 1-przewodowych
czujnik�w temperatury: DS18S20, DS1822 i DS18B20 firmy Dallas
Semiconductor. DigiTemp mo�e mie� wiele zastosowa�, takich jak
kontrola ogrzewania, monitorowanie proces�w, stacje metorologiczne,
wewn�trzne/zewn�trzne monitorowanie temperatury. Pakiet zawiera kilka
u�ytecznych skrypt�w Perla, Pytona i RRD do tworzenia wykres�w i
dynamicznych wpis�w.

%prep
%setup -q
%patch0 -p1

cp %{SOURCE1} .

%build
export OPT="%{rpmcflags}"
%{__make} ds9097
%{__make} ds9097u
%{__make} ds2490 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name},%{_mandir}/man1}

install digitemp_DS* $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -rf perl python rrdb $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS FAQ README TODO dthowto.txt
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/*
%{_mandir}/man1/*
