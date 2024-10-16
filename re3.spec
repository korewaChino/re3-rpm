%global git_commit 310dd8637147c4db643107b69d603902abc78141
%global shortcommit %(c=%{git_commit}; echo ${c:0:7})


Name:           re3
Version:        git~%{shortcommit}
Release:        1%{?dist}
Summary:        Re-implementation of GTA 3 in C++

License:        UNLICENSED
URL:            https://github.com/halpz/re3

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
BuildRequires:       mold

Source0:             %{name}.desktop

%description
Re-implementation of GTA 3 in C++

%prep
rm -rf %{build_dir}
git clone %{url} %{build_dir}
cd %{build_dir}
git checkout %{git_commit}
git submodule update --init --recursive

# let's configure the build for performance
# uncomment ifdef FINAL and MASTER in src/core/config.h
sed -i 's/\/\/#define FINAL/#define FINAL/' src/core/config.h
sed -i 's/\/\/#define MASTER/#define MASTER/' src/core/config.h
sed -i 's/\/\/#define SQUEEZE_PERFORMANCE/#define SQUEEZE_PERFORMANCE/' src/core/config.h

%build
cd %{build_dir}
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix} . -B redhat-linux-build -DLIBRW_PLATFORM=GL3 -DCMAKE_CXX_FLAGS="-std=c++11 -fuse-ld=mold %optflags"
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
%{_datadir}/applications/%{name}.desktop




%changelog
* Wed Oct 16 2024 Cappy Ishihara <cappy@cappuchino.xyz>
- 
