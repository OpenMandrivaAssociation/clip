%define _disable_ld_no_undefined 1
%define _disable_lto 1

Name:		clip
Version:	1.1.0
Release:	1
Summary:	Video player and video collection manager
Url:      https://invent.kde.org/maui/clip
Source0:	https://invent.kde.org/maui/clip/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
License:	GPLv3
Group:		Applications/Video
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5Attica)
BuildRequires: cmake(MauiKit)
BuildRequires: pkgconfig(mpv)

Requires: mpv

%description
Clip is as video player and video collection manager based on Maui Kit.

%prep
%autosetup -p1 -n %{name}-v%{version}

%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/clip
%{_datadir}/applications/org.maui.clip.desktop
%{_datadir}/icons/*/*/*/*.*
