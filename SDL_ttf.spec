Summary: Simple DirectMedia Layer TrueType Font library
Name: SDL_ttf
Version: 2.0.6
Release: 5

URL: http://www.libsdl.org/projects/SDL_ttf/
Source0: http://www.libsdl.org/projects/SDL_ttf/release/SDL_ttf-2.0.6.tar.gz
Patch0: %{name}-%{version}-openstream.patch
Patch1: %{name}-%{version}-ft2-build.patch
License: LGPL
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: SDL-devel >= 1.2.4
BuildRequires: freetype-devel >= 2.0
BuildRequires: zlib-devel

%description
This library allows you to use TrueType fonts to render text in SDL
applications.

%package devel
Summary: Files to develop SDL applications which use TrueType fonts
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This library allows you to use TrueType fonts to render text in SDL
applications. This package provides the libraries, include files and other
resources needed for developing SDL_ttf applications.

%prep
%setup -q
%patch -p1
%patch1 -p1 -b .ft2

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README CHANGES COPYING
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/SDL/

%changelog
* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Mar 21 2004 Panu Matilainen <pmatilai@welho.com> 0:2.0.6-0.fdr.4
- fix build on FC2-test (bug #1436

* Mon Nov 10 2003 Panu Matilainen <pmatilai@welho.com> 0:2.0.6-0.fdr.3
- add missing buildreq zlib-devel

* Sun Aug 24 2003 Panu Matilainen <pmatilai@welho.com> 0:2.0.6-0.fdr.2
- address issues in #631
- add full URL to source
- better description for -devel package

* Sat Aug 23 2003 Panu Matilainen <pmatilai@welho.com> 0:2.0.6-0.fdr.1
- Fedoraize
- patch to compile on RH9

* Wed Jan 19 2000 Sam Lantinga
- converted to get package information from configure
* Sun Jan 16 2000 Hakan Tandogan <hakan@iconsult.com>
- initial spec file

