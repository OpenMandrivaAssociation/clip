#define snapshot 20220107

Name:		clip
Version:	3.0.2
Release:	%{?snapshot:0.%{snapshot}.}2
Summary:	Video player and video collection manager
Url:		https://invent.kde.org/maui/clip
Source0:	https://invent.kde.org/maui/clip/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/%{name}-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/%{name}-%{snapshot}.tar.bz2}
License:	GPLv3
Group:		Applications/Video
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5Attica)
BuildRequires: cmake(MauiKit3)
BuildRequires: cmake(MauiKitFileBrowsing3)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(taglib)
BuildRequires: pkgconfig(mpv)

Requires: mpv

%description
Clip is as video player and video collection manager based on Maui Kit.

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang clip

%files -f clip.lang
%{_bindir}/clip
%{_datadir}/applications/org.kde.clip.desktop
%{_datadir}/metainfo/org.kde.clip.appdata.xml
%{_datadir}/icons/*/*/*/*.*
