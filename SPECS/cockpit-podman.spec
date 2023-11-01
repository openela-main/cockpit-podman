
Name:           cockpit-podman
Version: 63.1
Release:        1%{?dist}
Summary:        Cockpit component for Podman containers
License:        LGPLv2+
URL:            https://github.com/cockpit-project/cockpit-podman

Source0:        https://github.com/cockpit-project/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires: gettext
%if 0%{?rhel} && 0%{?rhel} <= 8
BuildRequires: libappstream-glib-devel
%endif

Requires:       cockpit-bridge >= 138
Requires:       podman >= 2.0.4

%description
The Cockpit user interface for Podman containers.

%prep
%setup -q -n %{name}

%build
# Nothing to build

%install
%make_install
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

%files
%doc README.md
%license LICENSE dist/index.js.LICENSE.txt.gz
%{_datadir}/cockpit/*
%{_datadir}/metainfo/*

%changelog
* Tue Feb 28 2023 Jindrich Novy <jnovy@redhat.com> - 63.1-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/63.1
- Related: #2124478

* Mon Feb 27 2023 Jindrich Novy <jnovy@redhat.com> - 63-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/63
- Related: #2124478

* Wed Feb 08 2023 Jindrich Novy <jnovy@redhat.com> - 62-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/62
- Related: #2124478

* Thu Jan 26 2023 Jindrich Novy <jnovy@redhat.com> - 61-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/61
- Related: #2124478

* Wed Jan 18 2023 Jindrich Novy <jnovy@redhat.com> - 60-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/60
- Related: #2124478

* Mon Jan 02 2023 Jindrich Novy <jnovy@redhat.com> - 59-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/59
- Related: #2124478

* Fri Dec 02 2022 Jindrich Novy <jnovy@redhat.com> - 58-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/58
- Related: #2124478

* Wed Nov 16 2022 Jindrich Novy <jnovy@redhat.com> - 57-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/57
- Related: #2124478

* Tue Nov 08 2022 Jindrich Novy <jnovy@redhat.com> - 56-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/56
- Related: #2124478

* Wed Oct 19 2022 Jindrich Novy <jnovy@redhat.com> - 55-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/55
- Related: #2124478

* Tue Oct 18 2022 Jindrich Novy <jnovy@redhat.com> - 54-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/54
- Related: #2124478

* Fri Sep 16 2022 Jindrich Novy <jnovy@redhat.com> - 53-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/53
- Related: #2062589

* Tue Aug 23 2022 Jindrich Novy <jnovy@redhat.com> - 52-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/52
- Related: #2061316

* Tue Jul 26 2022 Jindrich Novy <jnovy@redhat.com> - 51.1-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/51.1
- Related: #2061316

* Mon Jun 27 2022 Jindrich Novy <jnovy@redhat.com> - 50-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/50
- Related: #2061316

* Thu Jun 09 2022 Jindrich Novy <jnovy@redhat.com> - 49.1-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/49.1
- Related: #2061316

* Wed May 25 2022 Jindrich Novy <jnovy@redhat.com> - 48-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/48
- Related: #2061316

* Fri Apr 29 2022 Jindrich Novy <jnovy@redhat.com> - 47-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/47
- Related: #2061316

* Wed Apr 13 2022 Jindrich Novy <jnovy@redhat.com> - 46-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/46
- Related: #2061316

* Wed Mar 30 2022 Jindrich Novy <jnovy@redhat.com> - 45-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/45
- Related: #2061316

* Fri Mar 25 2022 Jindrich Novy <jnovy@redhat.com> - 44-2
- use spec file from the upstream source
- Related: #2061316

* Thu Mar 24 2022 Jindrich Novy <jnovy@redhat.com> - 44-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/44
- Related: #2061316

* Wed Mar 02 2022 Jindrich Novy <jnovy@redhat.com> - 43-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/43
- Related: #2017345

* Thu Feb 17 2022 Jindrich Novy <jnovy@redhat.com> - 42-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/42
- Related: #2000051

* Thu Feb 03 2022 Jindrich Novy <jnovy@redhat.com> - 41-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/41
- Related: #2000051

* Mon Jan 24 2022 Jindrich Novy <jnovy@redhat.com> - 40-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/40
- Related: #2000051

* Wed Jan 05 2022 Jindrich Novy <jnovy@redhat.com> - 39-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/39
- Related: #2000051

* Fri Dec 10 2021 Jindrich Novy <jnovy@redhat.com> - 38-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/38
- Related: #2000051

* Thu Nov 25 2021 Jindrich Novy <jnovy@redhat.com> - 37-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/37
- Related: #2000051

* Wed Nov 10 2021 Jindrich Novy <jnovy@redhat.com> - 36-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/36
- Related: #2000051

* Wed Sep 15 2021 Jindrich Novy <jnovy@redhat.com> - 35-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/35
- Related: #2000051

* Mon Sep 06 2021 Jindrich Novy <jnovy@redhat.com> - 34-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/34
- Related: #2000051

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 33-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Aug 05 2021 Jindrich Novy <jnovy@redhat.com> - 33-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/33
- Related: #1970747

* Mon Jul 05 2021 Jindrich Novy <jnovy@redhat.com> - 32-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/32
- Related: #1970747

* Mon Jun 14 2021 Jindrich Novy <jnovy@redhat.com> - 31-2
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/31
- Related: #1970747

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 29-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Fri Feb 19 2021 Martin Pitt <martin@piware.de> - 29-1

- PatternFly 4 updates for a more consistent UI
- Accessibility fixes
- Add FMF tests for sharing tests with up- and downstream

* Thu Feb 11 2021 Matej Marusak <mmarusak@redhat.com> - 28.1-1

- Improve tests to be more robust against unstable Podman API

* Thu Feb 04 2021 Matej Marusak <mmarusak@redhat.com> - 28-1

- Drop cockpit-system dependency
- Correctly show selected option for SELinux labels

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Matej Marusak <mmarusak@redhat.com> - 27.1-1

- test: Drop forgotten sit() to make tests work in gating

* Thu Jan 07 2021 Matej Marusak <mmarusak@redhat.com> - 27-1

- images: Indicate that force deletion is in progress
- images: Fix handling of errors on pull
- Use packaged sassc instead of node-sass
- tests: Adjust to new Podman versions and robustify them

* Wed Dec 09 2020 Marius Vollmer <mvollmer@redhat.com> - 26-1
- run: Make hostPort optional
- run: Enable setting up IP address for exposed ports

* Wed Oct 14 2020 Sanne Raymaekers <sanne.raymaekers@gmail.com> - 25-1

- Listen for image build event

* Wed Sep 30 2020 Marius Vollmer <mvollmer@redhat.com> - 24-1

- Use sentence case in the UI

* Wed Sep 02 2020 Martin Pitt <martin@piware.de> - 23-1

- Translation updates

* Wed Aug 19 2020 Marius Vollmer <mvollmer@redhat.com> - 22-1

- Support for pod group deletion

* Wed Aug 05 2020 Matej Marusak <mmarusak@redhat.com> - 21-1

- Support for pod groups
- Support checkpoint and restore
- Registry selection in "download image" dialog
- Selected tag removal during deletion

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Katerina Koukiou <kkoukiou@redhat.com> - 20-1

- Show networking information for containers
- Enable filtering images and containers by owner
- Optionally show intermediate images
- Enable setting up SELinux label when mounting volumes

* Wed Jul 15 2020 Matej Marusak <mmarusak@redhat.com> - 19-1

- Switch to the new Podman REST API
- Improve displaying on small screens

* Mon Jun 15 2020 Matej Marusak <mmarusak@redhat.com> - 18-1

- Bump NPM dependencies to their latest versions
- Stop importing cockpit's deprecated base1/patternfly.css
- Synchronize style with the newest Cockpit

* Thu May 14 2020 Matej Marusak <mmarusak@redhat.com> - 17-1

- Translation updates
- Adjust tests to changed Services page in Cockpit 218

* Wed Apr 29 2020 Martin Pitt <martin@piware.de> - 16-1

- Restyle buttons and dropdowns to be consistent with Cockpit
- Disable button and show a spinner while delete operation is in progress
- Translation updates

* Thu Apr 16 2020 Martin Pitt <martin@piware.de> - 15-3

- Drop obsolete functionality for Fedora Atomic
- Localize dates and times
- Make tests non-destructive, to support Fedora gating

* Wed Mar 04 2020 Martin Pitt <martin@piware.de> - 14-1

- Fix crash on filtering anonymous images
- Translation updates

* Wed Feb 05 2020 sanne raymaekers <sanne.raymaekers@gmail.com> - 13-1

- Show historical logs

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Katerina Koukiou <kkoukiou@redhat.com> - 12-1

- Configure CPU share for system containers

* Wed Nov 27 2019 Martin Pitt <martin@piware.de> - 11-1

- Fix Alert notification in Image Search Modal
- Allow more than a single Error Notification for Container action errors
- Various Alert cleanups
- Translation updates

* Wed Oct 30 2019 Sanne Raymaekers <sanne.raymaekers@gmail.com> - 10-1

- Support for user containers

* Wed Oct 02 2019 Martin Pitt <martin@piware.de> - 9-1

- Minimize CSS in production builds
- Bump NPM dependencies to latest versions

* Wed Sep 04 2019 Martin Pitt <martin@piware.de> - 8-1

- Show list of containers that use given image
- Show placeholder while loading containers and images
- Fix setting memory limit

* Wed Jul 31 2019 Martin Pitt <martin@piware.de> - 7-1

- Fix AppStream ID
- Adjust tests to changed Cockpit Services page

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Martin Pitt <martin@piware.de> - 6-1

- Fix various UI regressions from Cockpit's PatternFly 4 switch
- Add packit configuration (https://packit.dev/)

* Wed Jul 10 2019 Martin Pitt <martin@piware.de> - 5-1

- Add container Terminal

* Wed Jun 26 2019 Katerina Koukiou <kkoukiou@redhat.com> - 4-1

- Fix regression in container commit

* Mon Jun 17 2019 Martin Pitt <martin@piware.de> - 3-1

- Enable Commit button for running containers
- Fix race condition with container deletion
- Stop fetching all containers/images for each container/image event

* Fri May 24 2019 Cockpit Project <cockpituous@gmail.com> - 2-1
- Update to upstream 2 release

* Wed Apr 17 2019 Cockpit Project <cockpituous@gmail.com> - 1-2
- Update to upstream 1 release

