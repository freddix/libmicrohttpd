Summary:	Embeded HTTP server library
Name:		libmicrohttpd
Version:	0.9.29
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/libmicrohttpd/%{name}-%{version}.tar.gz
# Source0-md5:	ead86d88e8b71ad99a2273bca438536c
URL:		http://www.gnu.org/software/libmicrohttpd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	gnutls-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# FIXME
%define		skip_post_check_so	libmicrospdy.so.*

%description
GNU libmicrohttpd is a small C library that is supposed to make it
easy to run an HTTP server as part of another application.

%package devel
Summary:	Header files to develop libmicrohttpd applications
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files to develop libmicrohttpd applications.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--enable-curl		\
	--enable-https		\
	--enable-largefile	\
	--enable-messages	\
	--with-pic
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%post	devel -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libmicrohttpd.so.10
%attr(755,root,root) %{_libdir}/libmicrohttpd.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmicrohttpd.so
%{_libdir}/libmicrohttpd.la
%{_includedir}/microhttpd.h
%{_infodir}/libmicrohttpd.info*
%{_infodir}/libmicrohttpd-tutorial.info*
%{_mandir}/man3/libmicrohttpd.3*
%{_pkgconfigdir}/libmicrohttpd.pc

%if 0
/usr/bin/demo
/usr/bin/microspdy2http
/usr/include/microspdy.h
/usr/lib/libmicrospdy.la
/usr/lib/libmicrospdy.so
/usr/lib/libmicrospdy.so.0
/usr/lib/libmicrospdy.so.0.0.0
%endif

