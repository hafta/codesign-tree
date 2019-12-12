Runs the macOS codesign(1) command on a directory tree

This script runs the codesign(1) command on a directory tree as specified by a
provided JSON mappings file referred to as a map file. The function
codesign_tree does the bulk of the work and is written to be reused when the
code is included as a module. The format of the JSON map file, the script
arguments, and the codesign_tree function are documented in the codesign.py
source.

To run the script on a Firefox.app bundle,

````
$ pwd
/Users/hafta/r/codesign-tree

$ ditto /Applications/Firefox.app/ Firefox.app/

$ xattr -cr Firefox.app

$ python3 codesign-tree.py -v -m examples/01-firefox/codesign-map.json -r ./Firefox.app -d examples/01-firefox/ -s $CSID
JSON map file:          /Users/hafta/r/codesign-tree/examples/01-firefox/codesign-map.json
Entitlement directory:  /Users/hafta/r/codesign-tree/examples/01-firefox
Root directory:         /Users/hafta/r/codesign-tree/Firefox.app
Codesigning identity:   ABCD123456
file pattern "/Contents/MacOS/minidump-analyzer" matches no files
/usr/bin/codesign --force -v --sign NKAGS8LV4B --deep --options runtime /Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/XUL /Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/pingsender /Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libfreebl3.dylib /Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/liblgpllibs.dylib /Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libplugin_child_interpose.dylib /Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libsoftokn3.dylib /Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libmozavutil.dylib /Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libmozglue.dylib /Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libnssdbm3.dylib /Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libmozavcodec.dylib /Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libnssckbi.dylib /Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libnss3.dylib
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/XUL: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/XUL: signed Mach-O thin (x86_64) [XUL]
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/pingsender: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/pingsender: signed Mach-O thin (x86_64) [pingsender]
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libfreebl3.dylib: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libfreebl3.dylib: signed Mach-O thin (x86_64) [libfreebl3]
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/liblgpllibs.dylib: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/liblgpllibs.dylib: signed Mach-O thin (x86_64) [liblgpllibs]
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libplugin_child_interpose.dylib: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libplugin_child_interpose.dylib: signed Mach-O thin (x86_64) [libplugin_child_interpose]
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libsoftokn3.dylib: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libsoftokn3.dylib: signed Mach-O thin (x86_64) [libsoftokn3]
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libmozavutil.dylib: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libmozavutil.dylib: signed Mach-O thin (x86_64) [libmozavutil]
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libmozglue.dylib: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libmozglue.dylib: signed Mach-O thin (x86_64) [libmozglue]
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libnssdbm3.dylib: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libnssdbm3.dylib: signed Mach-O thin (x86_64) [libnssdbm3]
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libmozavcodec.dylib: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libmozavcodec.dylib: signed Mach-O thin (x86_64) [libmozavcodec]
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libnssckbi.dylib: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libnssckbi.dylib: signed Mach-O thin (x86_64) [libnssckbi]
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libnss3.dylib: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/libnss3.dylib: signed Mach-O thin (x86_64) [libnss3]
/usr/bin/codesign --force -v --sign NKAGS8LV4B --deep --options runtime /Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/crashreporter.app
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/crashreporter.app: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/crashreporter.app: signed app bundle with Mach-O thin (x86_64) [org.mozilla.crashreporter]
/usr/bin/codesign --force -v --sign NKAGS8LV4B --deep --options runtime /Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/updater.app
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/updater.app: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/updater.app: signed app bundle with Mach-O thin (x86_64) [org.mozilla.updater]
/usr/bin/codesign --force -v --sign NKAGS8LV4B --deep --options runtime --entitlements /Users/hafta/r/codesign-tree/examples/01-firefox/browser.production.entitlements.xml /Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/firefox-bin /Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/firefox
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/firefox-bin: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/firefox-bin: signed Mach-O thin (x86_64) [firefox-bin]
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/firefox: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/firefox: signed app bundle with Mach-O thin (x86_64) [org.mozilla.firefox]
/usr/bin/codesign --force -v --sign NKAGS8LV4B --deep --options runtime /Users/hafta/r/codesign-tree/Firefox.app/Contents/Resources/gmp-clearkey/ /Users/hafta/r/codesign-tree/Firefox.app/Contents/Resources/gmp-clearkey/0.1 /Users/hafta/r/codesign-tree/Firefox.app/Contents/Resources/gmp-clearkey/0.1/libclearkey.dylib.sig /Users/hafta/r/codesign-tree/Firefox.app/Contents/Resources/gmp-clearkey/0.1/manifest.json /Users/hafta/r/codesign-tree/Firefox.app/Contents/Resources/gmp-clearkey/0.1/libclearkey.dylib
/Users/hafta/r/codesign-tree/Firefox.app/Contents/Resources/gmp-clearkey/: bundle format unrecognized, invalid, or unsuitable
/usr/bin/codesign --force -v --sign NKAGS8LV4B --deep --options runtime --entitlements /Users/hafta/r/codesign-tree/examples/01-firefox/browser.production.entitlements.xml /Users/hafta/r/codesign-tree/Firefox.app/
/Users/hafta/r/codesign-tree/Firefox.app/: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/: signed app bundle with Mach-O thin (x86_64) [org.mozilla.firefox]
/usr/bin/codesign --force -v --sign NKAGS8LV4B --deep --options runtime --entitlements /Users/hafta/r/codesign-tree/examples/01-firefox/plugin-container.production.entitlements.xml /Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/plugin-container.app
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/plugin-container.app: replacing existing signature
/Users/hafta/r/codesign-tree/Firefox.app/Contents/MacOS/plugin-container.app: signed app bundle with Mach-O thin (x86_64) [org.mozilla.plugincontainer]
````
