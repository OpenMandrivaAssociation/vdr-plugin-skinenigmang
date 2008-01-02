
%define plugin	skinenigmang
%define name	vdr-plugin-%plugin
%define version	0.0.5
%define rel	3

Summary:	VDR plugin: EnigmaNG skin
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://andreas.vdr-developer.org/
Source:		http://andreas.vdr-developer.org/enigmang/download/vdr-%plugin-%version.tgz
# TODO: packages lowcolor icons too, maybe use alternatives?
Source1:	http://andreas.vdr-developer.org/enigmang/download/skinenigmang-logos-xpm-hi-20070702.tgz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
BuildRequires:	libMagick-devel
BuildRequires:	freetype2-devel
BuildRequires:	epgsearch-devel
Requires:	vdr-abi = %vdr_abi

%description
"EnigmaNG" is a standalone VDR skin based on the "Enigma" text2skin
addon.

%vdr_chanlogo_notice

%prep
%setup -q -n %plugin-%version -a 1
mv %plugin/HISTORY HISTORY.logos
mv %plugin/README README.logos

sed -i 's,"../epgsearch/services.h",<vdr/epgsearch/services.h>,' enigma.c

%vdr_plugin_params_begin %plugin
# Channel logo directory
var=LOGODIR
param="-l LOGODIR"
default=%{_vdr_chanlogodir}
# Set directory where truetype fonts are stored
var=FONTSDIR
param="-f FONTSDIR"
# Set directory where epgimages are stored
var=IMAGESDIR
param="-i IMAGESDIR"
default=%{_vdr_plugin_cachedir}/epgimages
%vdr_plugin_params_end

cat > README.install.urpmi <<EOF
%vdr_chanlogo_notice
EOF

%build
%vdr_plugin_build SKINENIGMA_HAVE_EPGSEARCH=1 HAVE_IMAGEMAGICK=1 \
	HAVE_FREETYPE=1

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_themedir}
install -m644 themes/*.theme %{buildroot}%{_vdr_themedir}

install -d -m755 %{buildroot}%{_vdr_plugin_datadir}
cp -a %{plugin} %{buildroot}%{_vdr_plugin_datadir}

install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}
ln -s %{_vdr_plugin_datadir}/%{plugin} %{buildroot}%{_vdr_plugin_cfgdir}/%{plugin}

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* HISTORY*
%{_vdr_plugin_datadir}/%{plugin}
%{_vdr_plugin_cfgdir}/%{plugin}
%{_vdr_themedir}/*.theme
