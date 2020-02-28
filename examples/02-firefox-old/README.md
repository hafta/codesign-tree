This example uses a map file to sign the Firefox.app bundle in a way that
closely matches how Firefox is signed today in automation (as of Feb 2020).

```
$ cd codesign-tree
$ ditto /Applications/Firefox.app Firefox.app
```

Clear extended attributes before signing.
```
$ xattr -c -r Firefox.app
```

Run codesign-tree which will sign files as dictated by the codesign-map.json file.
```
$ python3 codesign-tree.py -v -m ./examples/02-firefox-old/production.codesign-map.json -r ./Firefox.app/ -d ./examples/02-firefox-old/ -s $CSID
JSON map file:          /Users/haftandilian/r/codesign-tree/examples/02-firefox-old/production.codesign-map.json
Entitlement directory:  /Users/haftandilian/r/codesign-tree/examples/02-firefox-old
Root directory:         /Users/haftandilian/r/codesign-tree/Firefox.app
Codesigning identity:   D2C9222U5Z
Override:               sign: D2C9222U5Z
/usr/bin/codesign -v --force --sign D --options runtime --entitlements /Users/haftandilian/r/codesign-tree/examples/02-firefox-old/production.entitlements.xml /Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/crashreporter.app
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/crashreporter.app: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/crashreporter.app: signed app bundle with Mach-O thin (x86_64) [org.mozilla.crashreporter]
/usr/bin/codesign -v --force --sign D --options runtime --entitlements /Users/haftandilian/r/codesign-tree/examples/02-firefox-old/production.entitlements.xml /Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/updater.app
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/updater.app: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/updater.app: signed app bundle with Mach-O thin (x86_64) [org.mozilla.updater]
/usr/bin/codesign -v --force --sign D --options runtime --entitlements /Users/haftandilian/r/codesign-tree/examples/02-firefox-old/production.entitlements.xml /Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/plugin-container.app
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/plugin-container.app: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/plugin-container.app: signed app bundle with Mach-O thin (x86_64) [org.mozilla.plugincontainer]
/usr/bin/codesign -v --force --sign D --options runtime --entitlements /Users/haftandilian/r/codesign-tree/examples/02-firefox-old/production.entitlements.xml /Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/XUL /Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/pingsender /Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/minidump-analyzer /Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libfreebl3.dylib /Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/liblgpllibs.dylib /Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libplugin_child_interpose.dylib /Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libsoftokn3.dylib /Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libmozavutil.dylib /Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libmozglue.dylib /Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libmozavcodec.dylib /Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libnssckbi.dylib /Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libnss3.dylib
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/XUL: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/XUL: signed Mach-O thin (x86_64) [XUL]
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/pingsender: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/pingsender: signed Mach-O thin (x86_64) [pingsender]
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/minidump-analyzer: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/minidump-analyzer: signed Mach-O thin (x86_64) [minidump-analyzer]
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libfreebl3.dylib: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libfreebl3.dylib: signed Mach-O thin (x86_64) [libfreebl3]
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/liblgpllibs.dylib: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/liblgpllibs.dylib: signed Mach-O thin (x86_64) [liblgpllibs]
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libplugin_child_interpose.dylib: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libplugin_child_interpose.dylib: signed Mach-O thin (x86_64) [libplugin_child_interpose]
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libsoftokn3.dylib: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libsoftokn3.dylib: signed Mach-O thin (x86_64) [libsoftokn3]
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libmozavutil.dylib: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libmozavutil.dylib: signed Mach-O thin (x86_64) [libmozavutil]
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libmozglue.dylib: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libmozglue.dylib: signed Mach-O thin (x86_64) [libmozglue]
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libmozavcodec.dylib: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libmozavcodec.dylib: signed Mach-O thin (x86_64) [libmozavcodec]
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libnssckbi.dylib: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libnssckbi.dylib: signed Mach-O thin (x86_64) [libnssckbi]
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libnss3.dylib: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/libnss3.dylib: signed Mach-O thin (x86_64) [libnss3]
/usr/bin/codesign -v --force --sign D --options runtime --entitlements /Users/haftandilian/r/codesign-tree/examples/02-firefox-old/production.entitlements.xml /Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/firefox-bin
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/firefox-bin: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/MacOS/firefox-bin: signed Mach-O thin (x86_64) [firefox-bin]
/usr/bin/codesign -v --force --sign D --options runtime --entitlements /Users/haftandilian/r/codesign-tree/examples/02-firefox-old/production.entitlements.xml /Users/haftandilian/r/codesign-tree/Firefox.app/Contents/Resources/gmp-clearkey/0.1/libclearkey.dylib
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/Resources/gmp-clearkey/0.1/libclearkey.dylib: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/Contents/Resources/gmp-clearkey/0.1/libclearkey.dylib: signed Mach-O thin (x86_64) [libclearkey]
/usr/bin/codesign -v --force --sign D --options runtime --entitlements /Users/haftandilian/r/codesign-tree/examples/02-firefox-old/production.entitlements.xml /Users/haftandilian/r/codesign-tree/Firefox.app/
/Users/haftandilian/r/codesign-tree/Firefox.app/: replacing existing signature
/Users/haftandilian/r/codesign-tree/Firefox.app/: signed app bundle with Mach-O thin (x86_64) [org.mozilla.firefox]
```
