Name:           k9s
Version:        0.24.3
Release:        1%{?dist}
Summary:        Kubernetes CLI To Manage Your Clusters In Style!
License:        Apache-2.0
URL:            https://k9scli.io/
#Source0:        https://github.com/derailed/k9s/archive/v%{version}.tar.gz
Source0:        https://github.com/derailed/k9s/archive/master.tar.gz
BuildRequires:  make, git, go >= 1.13

# there's no debug files in this build
%define debug_package %{nil}

%description
K9s provides a terminal UI to interact with your Kubernetes clusters. The aim of this project is to make it easier to navigate, observe and manage your applications in the wild. K9s continually watches Kubernetes for changes and offers subsequent commands to interact with your observed resources.

%prep
%autosetup -n %{name}-master

%build
go version
make build

%install
install -D -m 0755 %{_builddir}/%{name}-master/execs/%{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
* Mon Mar 22 2021 Guilherme Cardoso <gjc@ua.pt> 0.24.3
- Build directly from master instead of the tagged version due to the dev bugfixing without releases

* Mon Nov  9 2020 Guilherme Cardoso <gjc@ua.pt> 0.23.9
- First release
