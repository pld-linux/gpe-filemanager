Summary:	GPE File manager
Summary(pl.UTF-8):	Zarządca plików GPE
Name:		gpe-filemanager
Version:	0.25
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.gz
# Source0-md5:	625cb4e7a316c3a17f5cedca90dc3cb7
URL:		http://gpe.linuxtogo.org/
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	libgpewidget-devel
BuildRequires:	pkgconfig
Requires:	gpe-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPE file manager, for embedded devices.

%description -l pl.UTF-8
Zarządca plików GPE dla urządzeń wbudowanych.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

install -D gpe-filemanager.1 $RPM_BUILD_ROOT%{_mandir}/man1/gpe-filamanager.1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/gpe-filemanager
%{_desktopdir}/gpe-filemanager.desktop
%dir %{_datadir}/gpe/pixmaps/default/filemanager
%dir %{_datadir}/gpe/pixmaps/default/filemanager/document-icons
%{_datadir}/gpe/pixmaps/default/filemanager/document-icons/*.png
%{_pixmapsdir}/gpe-filemanager.png
%{_mandir}/man1/gpe-filemanager.1*
