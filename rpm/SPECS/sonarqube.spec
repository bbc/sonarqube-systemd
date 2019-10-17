%define debug_package %{nil}
%define __jar_repack 0

Name: sonarqube
Version: %{ver}
Release: 1
License: Apache License 2.0. Copyright 2019 British Broadcasting Corporation.
URL: https://www.sonarqube.org/
Source: sonarqube-%{ver}.zip
Source1: sonarqube.service
Summary: SonarQube Community Edition
BuildRequires: systemd
BuildArch: x86_64
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
SonarQube is an automatic code review tool to detect bugs, vulnerabilities and code smells in your code, written by SonarSource.
This third-party package allows to install the Community Edition as a systemd service. 

%prep
%setup -q -n sonarqube-%{ver}

%pre
/usr/bin/getent group sonarqube || /usr/sbin/groupadd -r sonarqube || :
/usr/bin/getent passwd sonarqube || /usr/sbin/useradd -r -d /opt/sonarqube/ -s /sbin/nologin -g sonarqube sonarqube || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_unitdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/sonarqube.service

mkdir -p %{buildroot}/opt/sonarqube/
cp -r %{_builddir}/sonarqube-%{ver}/* %{buildroot}/opt/sonarqube/

%post
%systemd_post sonarqube.service
systemctl enable sonarqube.service

%preun
%systemd_preun sonarqube.service

%postun
%systemd_postun_with_restart sonarqube.service
if [ "$1" = "0" ]; then
   /usr/sbin/userdel sonarqube || :
fi

%files
%defattr(0644,sonarqube,sonarqube,0755)
/opt/sonarqube
%config(noreplace) /opt/sonarqube/conf/sonar.properties
%config(noreplace) /opt/sonarqube/conf/wrapper.conf

%attr(0755,sonarqube,sonarqube) /opt/sonarqube/bin/linux-x86-64/sonar.sh
%attr(0755,sonarqube,sonarqube) /opt/sonarqube/bin/linux-x86-64/wrapper
%attr(0755,sonarqube,sonarqube) /opt/sonarqube/elasticsearch/bin/elasticsearch

%attr(0644,root,root) %{_unitdir}/sonarqube.service
