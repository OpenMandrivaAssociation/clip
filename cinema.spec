Name:		cinema
Version:	1.1.1
Release:	1
Summary:	Video player and video collection manager
Url:      https://invent.kde.org/maui/cinema
Source0:	https://invent.kde.org/maui/cinema/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
License:	GPLv3
Group:		Applications/Video
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(ECM)
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

%description
Cinema is as video player and video collection manager based on Maui Kit.

%prep
%autosetup -p1 -n %{name}-v%{version}

%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
