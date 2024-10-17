%define name pccts
%define version 1.33mr33
%define release 11

Name: %{name}
Summary: Purdue Compiler Construction Tool
Version: %{version}
Release:	1
Source: %{name}-%{version}.tar.bz2
Patch0: %{name}-stdarg_usage.patch.bz2
Patch1: pccts-1.33mr33-mdv-fix-str-fmt.patch
Group: Development/Other
URL: https://www.polhode.com/pccts.html
BuildRoot: %{_tmppath}/%{name}-buildroot
License: Public domain


%description
PCCTS is a set of public domain software tools designed to facilate
the implementation of compilers and other translation systems.

%package devel
Group: Development/Other
Summary: Purdue Compiler Construction Tool Headers files

%description devel
PCCTS is a set of public domain software tools designed to facilate
the implementation of compilers and other translation systems.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%patch0 -p1
%patch1 -p1 -b .strfmt

%build

export PCCTS_USE_STDARG=1

make COTHER="$RPM_OPT_FLAGS" PREFIX="%{_prefix}" 

%install

mkdir -p $RPM_BUILD_ROOT%_bindir
mkdir -p $RPM_BUILD_ROOT%_mandir/man1
install -m 755 bin/{antlr,dlg,genmk,sor} $RPM_BUILD_ROOT%_bindir/
install -m 644 antlr/antlr.1 $RPM_BUILD_ROOT%_mandir/man1/.
install -m 644 dlg/dlg.1 $RPM_BUILD_ROOT%_mandir/man1/.

mkdir -p $RPM_BUILD_ROOT%_includedir/pccts
install -m 644 h/* $RPM_BUILD_ROOT%_includedir/pccts/

%clean
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc CHANGES_FROM_131.txt CHANGES_FROM_133.txt 
%doc CHANGES_FROM_133_BEFORE_MR13.txt
%doc KNOWN_PROBLEMS.txt MPW_Read_Me README
%doc RIGHTS history.txt
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr (-,root,root)
%dir %{_includedir}/pccts
%{_includedir}/pccts/*


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.33mr33-10mdv2011.0
+ Revision: 614488
- the mass rebuild of 2010.1 packages

* Tue Dec 08 2009 Jérôme Brenier <incubusss@mandriva.org> 1.33mr33-9mdv2010.1
+ Revision: 474827
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.33mr33-7mdv2009.0
+ Revision: 241138
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 1.33mr33-5mdv2008.0
+ Revision: 69931
- use %%mkrel

  + Adam Williamson <awilliamson@mandriva.org>
    - Import pccts



* Wed Jul 06 2005 Lenny Cartier <lenny@mandriva.com> 1.33mr33-4mdk
- rebuild

* Mon May 24 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.33mr33-3mdk
- add Patch0 stdarg_usage 

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.33mr33-2mdk
- rebuild

* Mon Jun 24 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.33mr33-1mdk
- updated to maintenace release 33

* Thu Jan 24 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.33mr31-1mdk
- updated to maintenance release 31

* Wed Aug 22 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.33mr25-1mdk
- updated to maintenance release 25

* Mon Apr 09 2001  Lenny Cartier <lenny@mandrakesoft.com> 1.33mr22-1mdk
- updated to maintenance release 22

* Wed Jan 24 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.33mr19-4mdk
- rebuild

* Mon Sep 11 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.33mr19-3mdk
- build release

* Wed May 03 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.33mr19-2mdk
- fix group
- fix files section

* Mon Oct 11 1999 Lenny Cartier <lenny@mandrakesoft.com>
- Little adaptation of the specfile 
