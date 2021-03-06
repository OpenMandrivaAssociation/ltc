%define major	11
%define libname	%mklibname %{name} %major
%define devname	%mklibname %{name} -d

Name:		ltc
Version:	1.3.0
Release:	1
Summary:	Linear (or Longitudinal) Time-code is an encoding of SMPTE time-code data
License:	LGPLv3
Group:		System/Libraries
Url:		https://github.com/x42/libltc
Source0:	https://github.com/downloads/x42/libltc/lib%{name}-%{version}.tar.gz

%description
Linear (or Longitudinal) Time-code (LTC) is an encoding of SMPTE time-code data
as a Manchester-Biphase encoded audio signal. The audio signal is commonly
recorded on a VTR track or other storage media. libltc provides functionality
to encode and decode LTC from/to time-code, including SMPTE date support.
libltc is the successor of libltcsmpte.

#---------------------------------
%package -n %{libname}
Summary:	Shared library for LTC
Group:		System/Libraries

%description -n %{libname}
Linear (or Longitudinal) Time-code (LTC) is an encoding of SMPTE time-code data
as a Manchester-Biphase encoded audio signal. The audio signal is commonly
recorded on a VTR track or other storage media. libltc provides functionality
to encode and decode LTC from/to time-code, including SMPTE date support.
libltc is the successor of libltcsmpte.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#---------------------------------
%package -n %{devname}
Summary:	Development files for LTC
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the files for developing applications which
will use lib%{name}.

%files -n %{devname}
%{_mandir}/man3/ltc.h.3.xz
%{_libdir}/lib%{name}.so
%{_includedir}/ltc.h
%{_libdir}/pkgconfig/ltc.pc

#---------------------------------
%prep
%setup -q -n lib%{name}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std
find %{buildroot} -regex ".*\(a\|la\)$" -exec rm '{}' \;
