
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
- Related: #2123641

* Mon Feb 27 2023 Jindrich Novy <jnovy@redhat.com> - 63-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/63
- Related: #2123641

* Wed Feb 08 2023 Jindrich Novy <jnovy@redhat.com> - 62-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/62
- Related: #2123641

* Thu Jan 26 2023 Jindrich Novy <jnovy@redhat.com> - 61-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/61
- Related: #2123641

* Fri Jan 13 2023 Jindrich Novy <jnovy@redhat.com> - 60-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/60
- Related: #2123641

* Mon Jan 02 2023 Jindrich Novy <jnovy@redhat.com> - 59-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/59
- Related: #2123641

* Fri Dec 02 2022 Jindrich Novy <jnovy@redhat.com> - 58-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/58
- Related: #2123641

* Fri Nov 18 2022 Jindrich Novy <jnovy@redhat.com> - 57-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/57
- Related: #2123641

* Tue Nov 08 2022 Jindrich Novy <jnovy@redhat.com> - 56-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/56
- Related: #2123641

* Wed Oct 19 2022 Jindrich Novy <jnovy@redhat.com> - 55-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/55
- Related: #2123641

* Mon Sep 26 2022 Jindrich Novy <jnovy@redhat.com> - 54-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/54
- Related: #2123641

* Wed Sep 07 2022 Jindrich Novy <jnovy@redhat.com> - 53-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/53
- Related: #2123641

* Wed Aug 24 2022 Jindrich Novy <jnovy@redhat.com> - 52-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/52
- Related: #2061390

* Tue Jul 26 2022 Jindrich Novy <jnovy@redhat.com> - 51.1-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/51.1
- Related: #2061390

* Mon Jun 27 2022 Jindrich Novy <jnovy@redhat.com> - 50-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/50
- Related: #2061390

* Thu Jun 09 2022 Jindrich Novy <jnovy@redhat.com> - 49.1-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/49.1
- Related: #2061390

* Thu May 26 2022 Jindrich Novy <jnovy@redhat.com> - 48-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/48
- Related: #2061390

* Fri Apr 29 2022 Jindrich Novy <jnovy@redhat.com> - 47-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/47
- Related: #2061390

* Mon Apr 25 2022 Jindrich Novy <jnovy@redhat.com> - 46-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/46
- Related: #2061390

* Fri Mar 25 2022 Jindrich Novy <jnovy@redhat.com> - 44-2
- use spec file from the upstream source
- Related: #2061390

* Thu Mar 24 2022 Jindrich Novy <jnovy@redhat.com> - 44-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/44
- Related: #2061390

* Mon Mar 07 2022 Jindrich Novy <jnovy@redhat.com> - 43-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/43
- Related: #2061390

* Thu Feb 17 2022 Jindrich Novy <jnovy@redhat.com> - 42-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/42
- Related: #2001445

* Thu Feb 03 2022 Jindrich Novy <jnovy@redhat.com> - 41-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/41
- Related: #2001445

* Mon Jan 24 2022 Jindrich Novy <jnovy@redhat.com> - 40-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/40
- Related: #2001445

* Wed Jan 05 2022 Jindrich Novy <jnovy@redhat.com> - 39-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/39
- Related: #2001445

* Fri Dec 10 2021 Jindrich Novy <jnovy@redhat.com> - 38-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/38
- Related: #2001445

* Fri Nov 26 2021 Jindrich Novy <jnovy@redhat.com> - 37-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/37
- Related: #2001445

* Thu Nov 11 2021 Jindrich Novy <jnovy@redhat.com> - 36-2
- revert the ansible change to fix gating tests
- Related: #2001445

* Wed Nov 10 2021 Jindrich Novy <jnovy@redhat.com> - 36-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/36
- Related: #2001445

* Fri Sep 17 2021 Jindrich Novy <jnovy@redhat.com> - 35-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/35
- Related: #2001445

* Fri Sep 10 2021 Jindrich Novy <jnovy@redhat.com> - 34-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/34
- Related: #2001445

* Thu Aug 05 2021 Jindrich Novy <jnovy@redhat.com> - 33-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/33
- Related: #1934415

* Wed Jul 21 2021 Jindrich Novy <jnovy@redhat.com> - 32-2
- attempt to fix gating tests - thanks for Matej Marusak
- Related: #1934415

* Mon Jul 05 2021 Jindrich Novy <jnovy@redhat.com> - 32-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/32
- Related: #1934415

* Wed May 26 2021 Jindrich Novy <jnovy@redhat.com> - 31-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/31
- Related: #1934415

* Mon Apr 26 2021 Jindrich Novy <jnovy@redhat.com> - 30-1
- fix gating test failure for cockpit-podman
- Related: #1934415

* Thu Mar 11 2021 Jindrich Novy <jnovy@redhat.com> - 29-3
- fix gating test failure for cockpit-podman
- Related: #1934415

* Thu Mar 04 2021 Jindrich Novy <jnovy@redhat.com> - 29-2
- gating test fix - properly install browser
- Related: #1934415

* Mon Feb 22 2021 Jindrich Novy <jnovy@redhat.com> - 29-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/29
- Related: #1883490

* Fri Feb 12 2021 Jindrich Novy <jnovy@redhat.com> - 28.1-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/28.1
- Related: #1883490

* Wed Feb 10 2021 Jindrich Novy <jnovy@redhat.com> - 28-4
- readd cockpit-system
Related: #1914884

* Mon Feb 08 2021 Jindrich Novy <jnovy@redhat.com> - 28-3
- fix gating tests for cockpit-podman - thanks for Matej Marusak
- Related: #1883490

* Sat Feb 06 2021 Jindrich Novy <jnovy@redhat.com> - 28-2
- remove applied patch and cockpit-shell dependency
- Related: #1883490

* Sat Feb 06 2021 Jindrich Novy <jnovy@redhat.com> - 28-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/28
- Related: #1883490

* Mon Jan 18 2021 Jindrich Novy <jnovy@redhat.com> - 27.1-4
- fix "Fix gating tests of container-tools for 8.4.0"
- Related: #1883490

* Fri Jan 15 2021 Jindrich Novy <jnovy@redhat.com> - 27.1-3
- another gating test fix - don't remove all containers but only admin ones
  thanks to Matej Marusak
- Related: #1883490

* Fri Jan 08 2021 Jindrich Novy <jnovy@redhat.com> - 27.1-2
- gating tests - always set VM password
- Related: #1883490

* Thu Jan 07 2021 Jindrich Novy <jnovy@redhat.com> - 27.1-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/27.1
- Related: #1883490

* Thu Jan 07 2021 Jindrich Novy <jnovy@redhat.com> - 27-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/27
- Related: #1883490

* Thu Dec 10 2020 Jindrich Novy <jnovy@redhat.com> - 26-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/26
- Related: #1883490

* Thu Dec 03 2020 Jindrich Novy <jnovy@redhat.com> - 25-4
- replace docker.io with quay.io for gating tests due do
  docker.io new pull rate limit requirements
- Related: #1883490

* Sat Nov 07 2020 Jindrich Novy <jnovy@redhat.com> - 25-3
- test: Cleanup images before pulling the ones we need - thanks to Matej Marusak
- Related: #1883490

* Tue Nov 03 2020 Jindrich Novy <jnovy@redhat.com> - 25-2
- remove hack in tests
- Related: #1883490

* Wed Oct 21 2020 Jindrich Novy <jnovy@redhat.com> - 25-1
- synchronize with stream-container-tools-rhel8
- Related: #1883490

* Sun Jul 26 2020 Jindrich Novy <jnovy@redhat.com> - 18.1-2
- revert back to 18.1 as this version is aimed at 8.3.0
- Related: #1821193

* Wed Jul 15 2020 Jindrich Novy <jnovy@redhat.com> - 19-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/19
- Related: #1821193

* Wed Jul 15 2020 Martin Pitt <mpitt@redhat.com> - 18.1-1
- Fix AppStream metainfo (rhbz#1854673)

* Mon Jun 15 2020 Jindrich Novy <jnovy@redhat.com> - 18-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/v18
- Related: #1821193

* Fri May 15 2020 Jindrich Novy <jnovy@redhat.com> - 17-1
- update to https://github.com/cockpit-project/cockpit-podman/releases/tag/17
- Related: #1821193

* Tue May 12 2020 Jindrich Novy <jnovy@redhat.com> - 16-1
- synchronize containter-tools 8.3.0 with 8.2.1
- Related: #1821193

* Mon Apr 20 2020 Matej Marusak <mmarusak@redhat.com> - 15-1
- Drop obsolete functionality for Fedora Atomic
- Localize dates and times
- Make tests non-destructive, to support gating
- Fix crash on filtering anonymous images
- Translation updates
- Show historical logs

* Thu Jan 09 2020 Matej Marusak <mmarusak@redhat.com> - 12-1
- Configure CPU share for system containers
- Translation updates

* Thu Nov 28 2019 Matej Marusak <mmarusak@redhat.com> - 11-1
- Fix Alert notification in Image Search Modal
- Allow more than a single Error Notification for Container action errors
- Various Alert cleanups
- Translation updates

* Wed Nov 13 2019 Matej Marusak <mmarusak@redhat.com> - 10-1
- Support for user containers
- Show list of containers that use given image
- Show placeholder while loading containers and images
- Fix setting memory limit rhbz#1732713
- Add container Terminal rhbz#1703245

* Wed Jun 26 2019 Martin Pitt <mpitt@redhat.com> - 4-1
- Fix regression in container commit
- Fix AppStream ID rhbz#1734809

* Mon Jun 17 2019 Martin Pitt <mpitt@redhat.com> - 3-1
- Enable Commit button for running containers
- Fix race condition with container deletion
- Stop fetching all containers/images for each container/image event

* Sun Jun 09 2019 Martin Pitt <mpitt@redhat.com> - 2-2
- Fix podman dependency

* Mon May 27 2019 Martin Pitt <mpitt@redhat.com> - 2-1
- Update to upstream 2 release
- Support podman API 1.3
- Support running commands with arguments
- Show the default command coming from image
- Implement filtering of images and containers

* Wed Apr 17 2019 Cockpit Project <cockpituous@gmail.com> - 1-2
- Update to upstream 1 release

