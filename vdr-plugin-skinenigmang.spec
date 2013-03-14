
%define plugin	skinenigmang
%define name	vdr-plugin-%plugin
%define version	0.1.0
%define rel	4

Summary:	VDR plugin: EnigmaNG skin
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://andreas.vdr-developer.org/enigmang/
Source:		http://andreas.vdr-developer.org/enigmang/download/vdr-%plugin-%version.tgz
# TODO: packages lowcolor icons too, maybe use alternatives?
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
%setup -q -n %plugin-%version -a 1
mv %plugin/HISTORY HISTORY.logos
mv %plugin/README README.logos
%vdr_plugin_prep

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
VDR_PLUGIN_EXTRA_FLAGS="$(pkg-config --cflags ImageMagick++)"
%vdr_plugin_build \
	SKINENIGMA_USE_PLUGIN_EPGSEARCH=1 \
	SKINENIGMA_USE_PLUGIN_AVARDS=1 \
	SKINENIGMA_USE_PLUGIN_MAILBOX=1 \
	HAVE_IMAGEMAGICK=1 \
	HAVE_FREETYPE=1

%install
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_themedir}
install -m644 themes/*.theme %{buildroot}%{_vdr_themedir}

install -d -m755 %{buildroot}%{_vdr_plugin_datadir}
cp -a %{plugin} %{buildroot}%{_vdr_plugin_datadir}

install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}
ln -s %{_vdr_plugin_datadir}/%{plugin} %{buildroot}%{_vdr_plugin_cfgdir}/%{plugin}

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* HISTORY*
%{_vdr_plugin_datadir}/%{plugin}
%{_vdr_plugin_cfgdir}/%{plugin}
%{_vdr_themedir}/*.theme


%changelog
* Thu Jul 15 2010 Funda Wang <fwang@mandriva.org> 0.1.0-3mdv2011.0
+ Revision: 553585
- rebuild

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0-2mdv2010.0
+ Revision: 401088
- rebuild for new VDR
- adapt for vdr compilation flags handling changes, bump buildrequires

* Tue Jul 14 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0-1mdv2010.0
+ Revision: 395754
- new version

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.6-5mdv2009.1
+ Revision: 359364
- rebuild for new vdr

* Thu Jan 29 2009 Götz Waschk <waschk@mandriva.org> 0.0.6-4mdv2009.1
+ Revision: 335087
- rebuild for new libmagick

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sun Oct 12 2008 Anssi Hannula <anssi@mandriva.org> 0.0.6-3mdv2009.1
+ Revision: 292795
- rebuild for new imagemagick (libmagick major was not changed despite
  breaking ABI)
- use backward-compatible pkg-config call for libmagick

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.6-2mdv2009.0
+ Revision: 197976
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.6-1mdv2009.0
+ Revision: 197721
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- update URL
- build with support for extra features with other plugins
- fix build with recent libmagick

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.5-4mdv2008.1
+ Revision: 145200
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.5-3mdv2008.1
+ Revision: 103210
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.5-2mdv2008.0
+ Revision: 50044
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.5-1mdv2008.0
+ Revision: 49915
- initial Mandriva release

