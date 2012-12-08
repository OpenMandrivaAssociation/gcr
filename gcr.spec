%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major_gck   0
%define api_gck     1

%define major_gcr   1
%define api_gcr     3

%define libname		%mklibname gcr %{api_gcr} %{major_gcr}
%define libnamebase	%mklibname gcr-base %{api_gcr} %{major_gcr}
%define libnamegck	%mklibname gck %{api_gck} %{major_gck}
%define girname		%mklibname gcr-gir %{major_gcr}
%define girnamegck	%mklibname gck-gir %{major_gck}
%define develname	%mklibname -d gcr 

Summary:    A library for bits of crypto UI and parsing
Name:       gcr
Version:    3.6.2
Release:    1
URL:        http://www.gnome.org/
License:    GPLv2+ and LGPLv2+
Group:      Networking/Remote access
Source0:    http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Source10:   %{name}.rpmlintrc

BuildRequires:  intltool
BuildRequires:  libgcrypt-devel
BuildRequires:  libtasn1-tools
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(p11-kit-1)
BuildRequires:  pkgconfig(libtasn1)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
#Conflicts:  gnome-keyring < 3.3.1

%description
A library for bits of crypto UI and parsing etc.

This package also contains the gcr-viewer binary.

%package -n %{libname}
Group:      System/Libraries
Summary:    Library for integration with the gnome keyring system
Requires:   %{name} = %{version}-%{release}
Conflicts:  %{_lib}gnome-keyring < 2.29.4
Obsoletes:  %{_lib}gcr-3_0 < 3.1.4
Obsoletes:  %{_lib}gcr-3_1 < 3.1.91

%description -n %{libname}
This package contains shared libraries for Gnome keyring.

%package -n %{libnamegck}
Group:      System/Libraries
Summary:    Library for integration with the gnome keyring system

%description -n %{libnamegck}
This package contains shared libraries for Gnome keyring.

%package -n %{libnamebase}
Group:          System/Libraries
Summary:        Library for integration with the gnome keyring system

%description -n %{libnamebase}
This package contains shared libraries for Gnome keyring.

%package -n %{girname}
Summary:        GObject Introspection interface description for Gcr
Group:          System/Libraries

%description -n %{girname}
GObject Introspection interface description for Gcr.

%package -n %{girnamegck}
Summary:        GObject Introspection interface description for Gck
Group:          System/Libraries

%description -n %{girnamegck}
GObject Introspection interface description for Gck.

%package -n %{develname}
Group:      Development/C
Summary:    Development files and headers for %{name}
Requires:   %{libname} = %{version}-%{release}
Requires:   %{libnamegck} = %{version}-%{release}
Requires:   %{libnamebase} = %{version}-%{release}
Requires:   %{girname} = %{version}-%{release}
Requires:   %{girnamegck} = %{version}-%{release}
Provides:   %{name}-devel = %{version}-%{release}
Conflicts:  %{_lib}-gnome-keyring-devel < 2.29.4

%description -n %{develname}
Thi package contains the development files and headers for %{name}.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
    --disable-static \
    --disable-update-mime \
    --disable-schemas-compile \
    --enable-introspection=yes
%make

%install
%makeinstall_std
find %{buildroot} -name "*.la" -exec rm -rf {} \;

rm -f %{buildroot}/%{_datadir}/glib-2.0/schemas/org.gnome.crypto.pgp*.xml

%find_lang %{name}

%files -f %{name}.lang
%doc README NEWS
%{_bindir}/gcr-viewer
%{_libexecdir}/gcr-prompter
%{_libdir}/libmock-test-module.so
%{_datadir}/%{name}-%{api_gcr}/
%{_datadir}/dbus-1/services/org.gnome.keyring.PrivatePrompter.service
%{_datadir}/dbus-1/services/org.gnome.keyring.SystemPrompter.service
%{_datadir}/GConf/gsettings/org.gnome.crypto.pgp*.convert
#%{_datadir}/glib-2.0/schemas/org.gnome.crypto.pgp*.xml
%{_datadir}/applications/gcr-viewer.desktop
%{_datadir}/applications/gcr-prompter.desktop
%{_datadir}/mime/packages/gcr-crypto-types.xml
%{_datadir}/icons/hicolor/*/apps/gcr*.png

%files -n %{libnamegck}
%{_libdir}/libgck-%{api_gck}.so.%{major_gck}*

%files -n %{girnamegck}
%{_libdir}/girepository-1.0/Gck-%{api_gck}.typelib

%files -n %{libnamebase}
%{_libdir}/libgcr-base-%{api_gcr}.so.%{major_gcr}*

%files -n %{libname}
%{_libdir}/libgcr-%{api_gcr}.so.%{major_gcr}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Gcr-%{api_gcr}.typelib

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/*
%{_libdir}/libgck-%{api_gck}.so
%{_libdir}/libgcr-%{api_gcr}.so
%{_libdir}/libgcr-base-%{api_gcr}.so
%{_includedir}/gck-%{api_gck}
%{_includedir}/gcr-%{api_gcr}
%{_libdir}/pkgconfig/gck-%{api_gck}.pc
%{_libdir}/pkgconfig/gcr-%{api_gcr}.pc
%{_libdir}/pkgconfig/gcr-base-%{api_gcr}.pc
%{_datadir}/gir-1.0/Gck-%{api_gck}.gir
%{_datadir}/gir-1.0/Gcr-%{api_gcr}.gir

%changelog
* Fri Sep 28 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Mon Aug 20 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.4.1-2
- temp drop C: gnome-keyring < 3.3.1

* Sat Apr 28 2012 Guilherme Moro <guilherme@mandriva.com> 3.4.1-1
+ Revision: 794360
- Created package structure for 'gcr'.

