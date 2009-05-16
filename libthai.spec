Summary:	LibThai - Thai language support routines
Summary(pl.UTF-8):	LibThai - biblioteka wspomagająca obsługę języka tajskiego
Name:		libthai
Version:	0.1.11
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://linux.thai.net/pub/thailinux/software/libthai/%{name}-%{version}.tar.gz
# Source0-md5:	f27fd7b67116939b2676ddff7180957a
URL:		http://linux.thai.net/projects/libthai
BuildRequires:	libdatrie-devel >= 0.2
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibThai is a set of Thai language support routines aimed to ease
developers' tasks to incorporate Thai language support in their
applications. It includes important Thai-specific functions e.g. word
breaking, input and output methods as well as basic character and
string supports. LibThai is an Open Source and collaborative effort
initiated by Thai Linux Working Group and opened for all contributors.

%description -l pl.UTF-8
LibThai to zbiór funkcji wspomagających obsługę języka tajskiego,
mających ułatwić programistom wprowadzanie obsługi języka tajskiego w
swoich aplikacjach. Zawiera istotne funkcje specyficzne dla języka
tajskiego, takie jak łamanie słów, metody wejścia i wyjścia, a także
podstawową obsługę znaków i łańcuchów. LibThai ma otwarte źródła i
jest wspólną pracą zapoczątkowaną przez Thai Linux Working Group,
otwartą na każdą współpracę.

%package devel
Summary:	Header files for LibThai library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LibThai
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libdatrie-devel

%description devel
Header files for LibThai library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LibThai.

%package static
Summary:	Static LibThai library
Summary(pl.UTF-8):	Statyczna biblioteka LibThai
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LibThai library.

%description static -l pl.UTF-8
Statyczna biblioteka LibThai.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libthai

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libthai.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libthai.so.0
%{_datadir}/libthai

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libthai.so
%{_libdir}/libthai.la
%{_includedir}/thai
%{_pkgconfigdir}/libthai.pc
%{_mandir}/man3/TAC*.3*
%{_mandir}/man3/th_*.3*
%{_mandir}/man3/th*.h.3*
%{_mandir}/man3/wtt.h.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libthai.a
