%define name pccts
%define version 1.33mr33
%define release 4mdk

Name: %{name}
Summary: Purdue Compiler Construction Tool
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.bz2
Patch0: %{name}-stdarg_usage.patch.bz2
Group: Development/Other
URL: http://www.polhode.com/pccts.html
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
