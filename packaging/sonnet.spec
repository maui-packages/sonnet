# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       sonnet

# >> macros
# << macros

Summary:    KDE Frameworks 5 Tier 1 solution for spell checking
Version:    5.3.0
Release:    2
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  sonnet.yaml
Source101:  sonnet-rpmlintrc
Requires:   kf5-filesystem
Requires:   sonnet-core%{?_isa} = %{version}-%{release}
Requires:   sonnet-gui%{?_isa} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(aspell)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  qt5-qttools-linguist
BuildRequires:  libupnp-devel
BuildRequires:  gettext-devel

%description
KDE Frameworks 5 Tier 1 solution for spell checking.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%package core
Summary:    Non-GUI part of the Sonnet framework
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description core
Non-GUI part of the Sonnet framework provides low-level spell checking tools.


%package gui
Summary:    GUI part of the Sonnet framework
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description gui
GUI part of the Sonnet framework provides low-level spell checking tools.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
%find_lang sonnet5_qt --with-qt --all-name || :
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/sonnet_version.h
%{_kf5_includedir}/SonnetCore
%{_kf5_includedir}/SonnetUi
%{_kf5_libdir}/libKF5SonnetCore.so
%{_kf5_libdir}/libKF5SonnetUi.so
%{_kf5_cmakedir}/KF5Sonnet
%{_kf5_mkspecsdir}/qt_SonnetCore.pri
%{_kf5_mkspecsdir}/qt_SonnetUi.pri
# >> files devel
# << files devel

%files core
%defattr(-,root,root,-)
%{_kf5_libdir}/libKF5SonnetCore.so.*
%{_kf5_plugindir}/*
%{_kf5_datadir}/sonnet/trigrams.map
# >> files core
# << files core

%files gui -f sonnet5_qt.lang
%defattr(-,root,root,-)
%{_kf5_libdir}/libKF5SonnetUi.so.*
# >> files gui
# << files gui
