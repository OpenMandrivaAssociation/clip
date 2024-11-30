#define snapshot 20220107

Name:		clip
Version:	4.0.0
Release:	%{?snapshot:0.%{snapshot}.}2
Summary:	Video player and video collection manager
Url:		https://invent.kde.org/maui/clip
Source0:	https://invent.kde.org/maui/clip/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/maui-%{name}-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/maui-%{name}-%{snapshot}.tar.bz2}
License:	GPLv3
Group:		Applications/Video
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Attica)
BuildRequires: cmake(MauiKit4)
BuildRequires: cmake(MauiKitFileBrowsing4)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(taglib)
BuildRequires: pkgconfig(mpv)

Requires: mpv

%description
Clip is as video player and video collection manager based on Maui Kit.

%prep
%autosetup -p1 -n maui-%{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
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
