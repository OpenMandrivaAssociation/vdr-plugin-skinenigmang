%define plugin	skinenigmang

Summary:	VDR plugin: EnigmaNG skin
Name:		vdr-plugin-%plugin
Version:	0.1.2
Release:	1
Group:		Video
License:	GPL+
URL:		http://andreas.vdr-developer.org/enigmang/
Source:		http://andreas.vdr-developer.org/enigmang/download/vdr-%plugin-%{version}.tgz
Source1:	http://andreas.vdr-developer.org/enigmang/download/skinenigmang-logos-xpm-hi-20070702.tgz
BuildRequires:	vdr-devel >= 1.6.0-7
BuildRequires:	imagemagick-devel
BuildRequires:	freetype2-devel
Requires:	vdr-abi = %vdr_abi

%description
"EnigmaNG" is a standalone VDR skin based on the "Enigma" text2skin
addon.

%vdr_chanlogo_notice

%prep
%setup -q -n %plugin-%{version} -a 1
mv %plugin/HISTORY HISTORY.logos
mv %plugin/README README.logos
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# Channel logo directory
var=LOGODIR
param="-l LOGODIR"
default=%{vdr_chanlogodir}
# Set directory where epgimages are stored
var=IMAGESDIR
param="-i IMAGESDIR"
default=%{vdr_plugin_cachedir}/epgimages
%vdr_plugin_params_end

cat > README.install.urpmi <<EOF
%vdr_chanlogo_notice
EOF

%build
VDR_PLUGIN_EXTRA_FLAGS="$(pkg-config --cflags ImageMagick++)"
%vdr_plugin_build \
	SKINENIGMA_USE_PLUGIN_EPGSEARCH=1 \
	SKINENIGMA_USE_PLUGIN_AVARDS=1 \
	SKINENIGMA_USE_PLUGIN_MAILBOX=1 \
	HAVE_IMAGEMAGICK=1 \
	HAVE_FREETYPE=1

%install
%vdr_plugin_install

install -d -m755 %{buildroot}%{vdr_themedir}
install -m644 themes/*.theme %{buildroot}%{vdr_themedir}

install -d -m755 %{buildroot}%{vdr_plugin_datadir}
cp -a %{plugin} %{buildroot}%{vdr_plugin_datadir}

install -d -m755 %{buildroot}%{vdr_plugin_cfgdir}
ln -s %{vdr_plugin_datadir}/%{plugin} %{buildroot}%{vdr_plugin_cfgdir}/%{plugin}

%files -f %plugin.vdr
%doc README* HISTORY*
%{vdr_plugin_datadir}/%{plugin}
%{vdr_plugin_cfgdir}/%{plugin}
%{vdr_themedir}/*.theme


