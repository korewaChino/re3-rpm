%global git_commit 37e9ec0d19cbd3cd25823089380fcdae558bee0b
%global shortcommit %(c=%{git_commit}; echo ${c:0:7})


Name:           reVC
Version:        git~%{shortcommit}
Release:        1%{?dist}
Summary:        Re-implementation of GTA Vice City in C++

License:        UNLICENSED
URL:            https://github.com/halpz/re3
%define build_dir %{name}-%{version}

BuildRequires:       openal-devel
BuildRequires:       libsndfile-devel
BuildRequires:       opus-devel
BuildRequires:       libvorbis-devel
BuildRequires:       mpg123-devel
BuildRequires:       glfw-devel
BuildRequires:       gcc-c++
BuildRequires:       cmake
BuildRequires:       make
BuildRequires:       pkg-config
BuildRequires:       git
Source0:             %{name}.desktop



%description
Re-implementation of GTA Vice City in C++

%prep
rm -rf %{build_dir}
git clone %{url} %{build_dir}
cd %{build_dir}
git checkout %{git_commit}
git submodule update --init --recursive



%build
cd %{build_dir}
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix} . -B redhat-linux-build -DLIBRW_PLATFORM=GL3 -DCMAKE_CXX_FLAGS="-std=c++11 %optflags"
make -C redhat-linux-build %{?_smp_mflags}



%install
cd %{build_dir}
install -m755 redhat-linux-build/src/%{name} -Dt %{buildroot}%{_bindir}
install -D {res/images/logo,%{buildroot}%{_datadir}/pixmaps/%{name}}.svg
install -D %{SOURCE0} %{buildroot}%{_datadir}/applications/%{name}.desktop
cp -r gamefiles %{buildroot}%{_datadir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.svg
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*




%changelog
* Wed Oct 16 2024 Cappy Ishihara <cappy@cappuchino.xyz>
- 
