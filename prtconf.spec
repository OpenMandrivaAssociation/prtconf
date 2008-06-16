Summary:	SPARC OpenPROM dump utility
Name:		prtconf
Version:	1.3
Release:	%mkrel 4
License:	GPL
Group:		System/Kernel and hardware
Source0:	ftp://sunsite.mff.cuni.cz/OS/Linux/Sparc/local/prtconf/%{name}-%{version}.tar.bz2
Patch0:		prtconf-1.3.patch.bz2
URL:		http://ultra.linux.cz/
ExclusiveArch:	%{sunsparc}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A set of utilities to dump OpenPROM device tree and to query
and/or modify OpenPROM options.

%prep
%setup -q
%patch0 -p1

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -m0755 prtconf -D $RPM_BUILD_ROOT%{_sbindir}/prtconf
install -m0755 eeprom -D $RPM_BUILD_ROOT%{_sbindir}/eeprom
install -m0644 prtconf.8 -D $RPM_BUILD_ROOT%{_mandir}/man8/prtconf.8
install -m0644 eeprom.8 -D $RPM_BUILD_ROOT%{_mandir}/man8/eeprom.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sbindir}/%{name}
%{_sbindir}/eeprom
%{_mandir}/man8/prtconf.8*
%{_mandir}/man8/eeprom.8*
