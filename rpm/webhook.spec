%global provider        github
%global provider_tld    com
%global project         adnanh
%global repo            webhook
# https://github.com/adnanh/webhook
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}

# set via `rpmbuild --define "_fooo bar" ...
%if 0%{?_commit:1}
%global commit          %{_commit}
%else
%global commit          unknown
%endif

%if 0%{?_version:1}
%global version          %{_version}
%else
%global version          unknown
%endif
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           %{repo}
Version:        %{version}
Release:        %{_commitcount}_%{shortcommit}%{?dist}
Summary:        webhook is a lightweight configurable webhook server written in Go
License:        MIT
URL:            https://%{provider_prefix}

%description
%{summary}

%prep

%build

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 %{_topdir}/%{name} %{buildroot}%{_bindir}
install -d -p %{buildroot}%{_sysconfdir}/webhook/
install -p -m 0640 %{_topdir}/hooks.json.example %{buildroot}%{_sysconfdir}/%{name}/
install -d -p %{buildroot}%{_docdir}/%{name}-%{version}/
install -p -m 0640 %{_topdir}/README.md %{buildroot}%{_docdir}/%{name}-%{version}/
install -p -m 0640 %{_topdir}/hooks.json.example %{buildroot}%{_docdir}/%{name}-%{version}/
install -d -p %{buildroot}%{_licensedir}/%{name}-%{version}/
install -p -m 0640 %{_topdir}/LICENSE %{buildroot}%{_licensedir}/%{name}-%{version}/

%files
%license LICENSE
%doc README.md hooks.json.example
%config(noreplace)%{_sysconfdir}/webhook/*
%{_bindir}/webhook
