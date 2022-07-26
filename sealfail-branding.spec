Name:           sealfail-branding
Version:        1
Release:        1
Summary:        The SEALFAIL branding things
License:        GPLv3

Source0: 	%{name}.tar.xz

BuildArch:      noarch

%description
The SEALFAIL branding things

%prep
%setup -q -n %{name}
mkdir -p /usr/share/backgrounds/
mkdir -p /usr/share/glib-2.0/schemas/

%build

%install
mkdir -p %{buildroot}/usr/share/backgrounds
mkdir -p %{buildroot}/usr/share/glib-2.0/schemas

#Install the wallpapers
install -m 0644 SEALFAIL.xml %{buildroot}/usr/share/backgrounds/SEALFAIL.xml
install -m 0644 SEALFAIL-1800x1440.jpg %{buildroot}/usr/share/backgrounds/SEALFAIL-1800x1440.jpg
install -m 0644 SEALFAIL-2048x1536.jpg %{buildroot}/usr/share/backgrounds/SEALFAIL-2048x1536.jpg
install -m 0644 SEALFAIL-2560x1440.jpg %{buildroot}/usr/share/backgrounds/SEALFAIL-2560x1440.jpg
install -m 0644 SEALFAIL-2560x1440.jpg %{buildroot}/usr/share/backgrounds/SEALFAIL-2560x1080.jpg
install -m 0644 SEALFAIL-2560x1600.jpg %{buildroot}/usr/share/backgrounds/SEALFAIL-2560x1600.jpg
install -m 0644 SEALFAIL-3440x1440.jpg %{buildroot}/usr/share/backgrounds/SEALFAIL-3440x1440.jpg

#Install the GNOME overrides
install -m 0644 10_org.gnome.desktop.screensaver.default.gschema.override %{buildroot}/usr/share/glib-2.0/schemas/10_org.gnome.desktop.screensaver.default.gschema.override
install -m 0644 10_org.gnome.desktop.background.default.gschema.override %{buildroot}/usr/share/glib-2.0/schemas/10_org.gnome.desktop.background.default.gschema.override

%files
%attr(0644,root,root) /usr/share/backgrounds/SEALFAIL.xml
%attr(0644,root,root) /usr/share/backgrounds/SEALFAIL-1800x1440.jpg
%attr(0644,root,root) /usr/share/backgrounds/SEALFAIL-2048x1536.jpg
%attr(0644,root,root) /usr/share/backgrounds/SEALFAIL-2560x1080.jpg
%attr(0644,root,root) /usr/share/backgrounds/SEALFAIL-2560x1440.jpg
%attr(0644,root,root) /usr/share/backgrounds/SEALFAIL-2560x1600.jpg
%attr(0644,root,root) /usr/share/backgrounds/SEALFAIL-3440x1440.jpg
%attr(0644,root,root) /usr/share/glib-2.0/schemas/10_org.gnome.desktop.screensaver.default.gschema.override
%attr(0644,root,root) /usr/share/glib-2.0/schemas/10_org.gnome.desktop.background.default.gschema.override


%changelog
* Tue Jul 26 2022 Sasha Emily Chelsea Murgia - 1-1
- Initial release
