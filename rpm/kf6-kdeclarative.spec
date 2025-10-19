%global  kf_version 6.6.0

Name:    kf6-kdeclarative
Version: 6.18.0
Release: 0%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon for Qt declarative
License: CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND MIT
URL:     https://invent.kde.org/frameworks/kdeclarative
Source0:    %{name}-%{version}.tar.bz2

Patch0:  0001-sailfish-no-kglobalaccel.patch

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{kf_version}
BuildRequires:  gcc-c++
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kguiaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-kwidgetsaddons-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtshadertools-devel
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel

%description
KDE Frameworks 6 Tier 3 addon for Qt declarative

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf6-kconfig-devel
#Requires:       cmake(KF6Package)
Requires:       qt6-qtdeclarative-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6 -DSAILFISHOS=ON
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6CalendarEvents.so.*
%{_kf6_libdir}/libkquickcontrolsprivate.so.*
%dir %{_kf6_qmldir}/org/
%dir %{_kf6_qmldir}/org/kde/
%{_kf6_qmldir}/org/kde/draganddrop/
%{_kf6_qmldir}/org/kde/graphicaleffects/
%{_kf6_qmldir}/org/kde/kquickcontrols/
%{_kf6_qmldir}/org/kde/private/kquickcontrols/
%{_kf6_qmldir}/org/kde/kquickcontrolsaddons/

%files devel
%{_kf6_includedir}/KDeclarative/
%{_kf6_libdir}/libKF6CalendarEvents.so
%{_kf6_libdir}/cmake/KF6Declarative/
