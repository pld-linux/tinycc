# TODO: Do not strip the executable.
%define		pre	pre2
Summary:	Tiny C Compiler
Summary(pl.UTF-8):	Mały kompilator C
Name:		tinycc
Version:	1.0.0
Release:	0.%{pre}.1
License:	GPL v2
Group:		Development/Languages
Source0:	http://www.landley.net/code/tinycc/downloads/%{name}-%{version}-%{pre}.tar.bz2
# Source0-md5:	c985f07371e5da24c24889826956671a
#Patch0:		%{name}-DESTDIR.patch
ExclusiveArch:	%{ix86}
URL:		http://www.landley.net/code/tinycc/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define		tinyccdir	%{_prefix}/lib/tinycc

%description
Tiny C Compiler - C Scripting Everywhere - The Smallest ANSI C
compiler. This is a fork of the original tcc released under terms
of GPL v2.

%description -l pl.UTF-8
Mały kompilator C - Wszędzie skrypty w C - Najmniejszy kompilator ANSI
C. To jest "fork" oryginalnego tcc wydany na licencji GPL v2.

%prep
%setup -q -n %{name}-%{version}-%{pre}

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
HOST="i386" \
PREFIX="%{_prefix}" \
TINYCC_INSTALLDIR="%{tinyccdir}" make/make.sh i386

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{tinyccdir}/{lib,include}}
install libtinyccrt-*.a libtinycc-*.so $RPM_BUILD_ROOT%{tinyccdir}/lib
install include/* $RPM_BUILD_ROOT%{tinyccdir}/include
install *-tinycc $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc Changelog README TODO www/*
%attr(755,root,root) %{_bindir}/*
%dir %{tinyccdir}
%dir %{tinyccdir}/include
%dir %{tinyccdir}/lib
%{tinyccdir}/include/*
%{tinyccdir}/lib/*.a
%attr(755,root,root) %{tinyccdir}/lib/*.so
