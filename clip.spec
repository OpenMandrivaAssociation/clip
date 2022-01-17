%define snapshot 20220107

Name:		clip
Version:	2.1.1
Release:	%{?snapshot:0.%{snapshot}.}2
Summary:	Video player and video collection manager
Url:		https://invent.kde.org/maui/clip
Source0:	https://invent.kde.org/maui/clip/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/%{name}-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/%{name}-%{snapshot}.tar.bz2}
Patch0:		clip-ffmpeg-5.0.patch
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
BuildRequires: cmake(MauiKitFileBrowsing)
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

%files
%{_bindir}/clip
%{_datadir}/applications/org.kde.clip.desktop
%{_datadir}/icons/*/*/*/*.*
